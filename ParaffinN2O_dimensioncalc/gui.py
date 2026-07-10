"""
Simple desktop GUI for the N2O / paraffin hybrid motor sizing tool.

Built with tkinter (ships with standard CPython on Windows — no extra install).

Layout:
  Left  — labeled entry fields for design inputs + Run / Clear buttons
  Right — scrollable text area with the same summary the CLI prints

On Run:
  1. Read and convert field values to SI MotorInputs
  2. Call run_motor(...) from model.py
  3. Show the text summary
  4. Save CSV/PNG under motorsim_output/ and open matplotlib plots

Launch:
  python -m ParaffinN2O_dimensioncalc
  or double-click "Run Motor GUI.bat"
"""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, scrolledtext, ttk

# Reuse CLI helpers so GUI and command-line stay consistent.
from ParaffinN2O_dimensioncalc.cli import format_summary, make_plots, save_csv
from ParaffinN2O_dimensioncalc.model import MotorInputs, run_motor

# ---------------------------------------------------------------------------
# Field definitions: (internal key, label shown in UI, default text)
# Keys must match what format_summary expects and what _collect_inputs uses.
# G_ox is intentionally absent — the solver computes it.
# ---------------------------------------------------------------------------
FIELDS: list[tuple[str, str, str]] = [
    ("case_od_mm", "Case outer diameter [mm]", "152.4"),
    ("wall_mm", "Wall / liner thickness [mm]", "3"),
    ("fuel_mass", "Fuel mass [kg]", "1.5"),
    ("burn_time", "Burn time [s]", "10"),
    ("pc_bar", "Chamber pressure [bar]", "30"),
    ("of_ratio", "O/F ratio [-]", "6"),
    ("total_impulse_kn_s", "Total impulse [kN·s]", "20"),
    ("density", "Fuel density [kg/m³]", "834"),
    ("dt", "Time step [s]", "0.01"),
]


class MotorApp(tk.Tk):
    """
    Main application window.

    Inherits from tk.Tk so `self` *is* the root window. Calling mainloop()
    starts the event loop (clicks, typing, redraws).
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Hybrid Motor Sizing — N2O / Paraffin")
        self.minsize(720, 560)
        # Maps field key -> Entry widget so we can read values later.
        self._entries: dict[str, tk.Entry] = {}
        self._build()

    def _build(self) -> None:
        """Create and grid all widgets. Called once at startup."""
        # Outer padding frame fills the window and stretches with resize.
        root = ttk.Frame(self, padding=12)
        root.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # Column 0 = form (fixed-ish), column 1 = results (expands).
        root.columnconfigure(0, weight=0)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        # ----- Input form (left) -----
        form = ttk.LabelFrame(root, text="Inputs", padding=10)
        form.grid(row=0, column=0, sticky="nw", padx=(0, 12))

        for i, (key, label, default) in enumerate(FIELDS):
            ttk.Label(form, text=label).grid(row=i, column=0, sticky="w", pady=3, padx=(0, 8))
            entry = ttk.Entry(form, width=14)
            entry.insert(0, default)
            entry.grid(row=i, column=1, sticky="e", pady=3)
            self._entries[key] = entry

        btn_row = ttk.Frame(form)
        btn_row.grid(row=len(FIELDS), column=0, columnspan=2, pady=(12, 0), sticky="ew")
        # command= binds the button click to a method (no parentheses — pass the function).
        ttk.Button(btn_row, text="Run", command=self._on_run).pack(side="left")
        ttk.Button(btn_row, text="Clear results", command=self._clear_results).pack(
            side="left", padx=(8, 0)
        )

        # ----- Results pane (right) -----
        right = ttk.Frame(root)
        right.grid(row=0, column=1, rowspan=2, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(0, weight=1)

        out_frame = ttk.LabelFrame(right, text="Results", padding=8)
        out_frame.grid(row=0, column=0, sticky="nsew")
        out_frame.columnconfigure(0, weight=1)
        out_frame.rowconfigure(0, weight=1)

        # Disabled text widget: user can scroll/select but not edit the report.
        self.results = scrolledtext.ScrolledText(
            out_frame,
            wrap="word",
            width=60,
            height=28,
            font=("Consolas", 10),
            state="disabled",
        )
        self.results.grid(row=0, column=0, sticky="nsew")

        hint = ttk.Label(
            root,
            text="Plots open in a separate window. CSV/PNG also saved to the motorsim_output/ folder.",
            foreground="#444444",
        )
        hint.grid(row=1, column=0, sticky="sw", pady=(8, 0))

    def _read_float(self, key: str) -> float:
        """Parse one entry as float; commas (e.g. 1,500) are stripped."""
        raw = self._entries[key].get().strip().replace(",", "")
        return float(raw)

    def _collect_inputs(self) -> tuple[MotorInputs, dict[str, float]]:
        """
        Read every field, convert to SI, and also keep a 'vals' dict in UI units
        for format_summary (which prints mm / bar / kN·s).
        """
        vals = {key: self._read_float(key) for key, _, _ in FIELDS}
        inp = MotorInputs(
            case_od_m=vals["case_od_mm"] * 1e-3,
            wall_thickness_m=vals["wall_mm"] * 1e-3,
            fuel_mass_kg=vals["fuel_mass"],
            burn_time_s=vals["burn_time"],
            chamber_pressure_pa=vals["pc_bar"] * 1e5,
            of_ratio=vals["of_ratio"],
            total_impulse_n_s=vals["total_impulse_kn_s"] * 1e3,  # kN·s -> N·s
            dt_s=vals["dt"],
            fuel_density_kg_m3=vals["density"],
        )
        return inp, vals

    def _set_results(self, text: str) -> None:
        """Replace the results text. Must briefly enable the widget to edit it."""
        self.results.configure(state="normal")
        self.results.delete("1.0", "end")
        self.results.insert("1.0", text)
        self.results.configure(state="disabled")

    def _clear_results(self) -> None:
        self._set_results("")

    def _on_run(self) -> None:
        """
        Run button callback.

        Errors are shown in message boxes so the user is not left staring at
        a blank results pane. Sizing ValueErrors (impossible geometry, etc.)
        are distinguished from unexpected crashes.
        """
        try:
            inp, vals = self._collect_inputs()
        except ValueError:
            messagebox.showerror("Invalid input", "All fields must be valid numbers.")
            return

        try:
            result = run_motor(inp)
        except ValueError as exc:
            # Expected physics/geometry failures from model.size_motor, etc.
            messagebox.showerror("Sizing error", str(exc))
            return
        except Exception as exc:  # noqa: BLE001 — surface anything else to the user
            messagebox.showerror("Error", f"Unexpected error:\n{exc}")
            return

        # Text report in the right-hand pane.
        summary = format_summary(vals, result)
        self._set_results(summary)

        # Persist time history and open plots (matplotlib window is separate).
        out_dir = Path("motorsim_output")
        try:
            save_csv(out_dir / "burn_history.csv", result)
            make_plots(result, out_dir=out_dir, show=True)
        except Exception as exc:  # noqa: BLE001
            messagebox.showwarning(
                "Results computed",
                f"Model ran, but saving/plotting failed:\n{exc}\n\nText results are still shown.",
            )


def main() -> int:
    """Create the window and enter the tkinter event loop."""
    app = MotorApp()
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
