"""
Desktop GUI for the 9-state rocket trajectory simulator.

================================================================================
WHAT THIS MODULE DOES
================================================================================
Tkinter front-end that wires user inputs → physics → animation:

  1. Collect vehicle / aero / goal fields from the form (mm and kg as typed).
  2. Load MotorData from the motor output folder (CSV + JSON).
  3. Call simulate.simulate(...) to integrate the flight.
  4. Hand the TrajectoryResult to animate.attach_animation on an embedded
     matplotlib FigureCanvasTkAgg.
  5. Let camera radio buttons call set_camera_mode while the loop runs.

================================================================================
LAYOUT
================================================================================
  Left  — ttk inputs, Run / Load motor folder, camera-mode radios
  Right — embedded matplotlib 3D canvas with looping animation
  Title — window title "Rocket Trajectory Analysis"

================================================================================
PATH BOOTSTRAP
================================================================================
The folder is named "Model Trajectory" (space), so it is not a normal
importable package. We insert this directory on sys.path so sibling modules
(atmosphere, dynamics, …) import as top-level names. Same pattern as __main__.py.

Launch:
  double-click "Run Trajectory GUI.bat"
  or: python "Model Trajectory/gui.py"
"""

from __future__ import annotations

import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

# Path bootstrap: folder name has a space, so we are not a normal importable package.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import matplotlib

# Must set the backend *before* importing pyplot / figure classes when embedding
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from animate import CAMERA_LABELS, AnimationHandles, CameraMode, attach_animation
from motor_import import load_motor
from simulate import SimInputs, TrajectoryResult, simulate

# (internal key, label shown in UI, default text)
# Keys are read in _collect_inputs; mm fields are converted to meters there.
FIELDS: list[tuple[str, str, str]] = [
    ("diameter_mm", "Vehicle outer diameter [mm]", "152.4"),
    ("length_mm", "Vehicle length [mm]", "2000"),
    ("propellant_kg", "Propellant mass [kg]", "10"),
    ("mass_dry_kg", "Vehicle mass (dry) [kg]", "25"),
    ("cd", "Cd (AoA = 0) [-]", "0.45"),
    ("altitude_goal_m", "Altitude goal [m]", "3000"),
    ("mach_goal", "Max Mach goal [-]", "1.0"),
    ("motor_folder", "Motor output folder", "motorsim_output"),
]

_CAMERA_MODES: list[tuple[CameraMode, str]] = [
    ("orbit", CAMERA_LABELS["orbit"]),
    ("follow", CAMERA_LABELS["follow"]),
    ("nose", CAMERA_LABELS["nose"]),
]


class TrajectoryApp(tk.Tk):
    """
    Main window: form + embedded 3D trajectory animation.

    Inherits from tk.Tk so `self` *is* the root window. mainloop() runs the
    event loop (button clicks, redraws, animation timer via matplotlib).
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Rocket Trajectory Analysis")
        self.minsize(1100, 680)

        self._entries: dict[str, ttk.Entry] = {}
        self._camera_var = tk.StringVar(value="orbit")
        self._anim_handles: AnimationHandles | None = None
        self._result: TrajectoryResult | None = None

        self._fig: Figure | None = None
        self._ax = None
        self._canvas: FigureCanvasTkAgg | None = None

        self._build()

    def _build(self) -> None:
        """Create and grid all widgets. Called once at startup."""
        root = ttk.Frame(self, padding=12)
        root.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=0)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

        # ----- Left: inputs -----
        left = ttk.Frame(root)
        left.grid(row=0, column=0, sticky="nsw", padx=(0, 12))

        form = ttk.LabelFrame(left, text="Inputs", padding=10)
        form.grid(row=0, column=0, sticky="nw")

        for i, (key, label, default) in enumerate(FIELDS):
            ttk.Label(form, text=label).grid(row=i, column=0, sticky="w", pady=3, padx=(0, 8))
            entry = ttk.Entry(form, width=18)
            entry.insert(0, default)
            entry.grid(row=i, column=1, sticky="e", pady=3)
            self._entries[key] = entry

        btn_row = ttk.Frame(form)
        btn_row.grid(row=len(FIELDS), column=0, columnspan=2, pady=(12, 0), sticky="ew")
        # command= takes the function object — do not write self._on_run()
        ttk.Button(btn_row, text="Run", command=self._on_run).pack(side="left")
        ttk.Button(btn_row, text="Load motor folder", command=self._on_load_motor).pack(
            side="left", padx=(8, 0)
        )

        cam = ttk.LabelFrame(left, text="Camera", padding=10)
        cam.grid(row=1, column=0, sticky="nw", pady=(12, 0))
        for mode, label in _CAMERA_MODES:
            ttk.Radiobutton(
                cam,
                text=label,
                value=mode,
                variable=self._camera_var,
                command=self._on_camera_change,
            ).pack(anchor="w", pady=2)

        hint = ttk.Label(
            left,
            text="Run Motor GUI.bat first so motorsim_output/\n"
            "has burn_history.csv + motor_export.json.\n"
            "Frame: y up, xz ground, launch at origin.",
            foreground="#444444",
            justify="left",
        )
        hint.grid(row=2, column=0, sticky="sw", pady=(12, 0))

        # ----- Right: 3D canvas -----
        right = ttk.LabelFrame(root, text="Trajectory", padding=4)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(0, weight=1)

        self._fig = Figure(figsize=(7.5, 6.2), dpi=100, facecolor="#1a1a1a")
        self._ax = self._fig.add_subplot(111, projection="3d", facecolor="#1a1a1a")
        self._style_axes(self._ax)
        # Placeholder labels until the first Run remaps axes in attach_animation
        self._ax.set_xlabel("x [m]")
        self._ax.set_ylabel("y [m] (up)")
        self._ax.set_zlabel("z [m]")
        self._ax.text2D(
            0.5,
            0.5,
            "Press Run to simulate",
            transform=self._ax.transAxes,
            ha="center",
            va="center",
            color="#888888",
            fontsize=11,
        )

        self._canvas = FigureCanvasTkAgg(self._fig, master=right)
        self._canvas.draw()
        self._canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        toolbar_frame = ttk.Frame(right)
        toolbar_frame.grid(row=1, column=0, sticky="ew")
        NavigationToolbar2Tk(self._canvas, toolbar_frame)

    @staticmethod
    def _style_axes(ax) -> None:
        """Light tick/label colors on the dark figure background."""
        ax.tick_params(colors="#cccccc")
        ax.xaxis.label.set_color("#cccccc")
        ax.yaxis.label.set_color("#cccccc")
        ax.zaxis.label.set_color("#cccccc")

    def _read_float(self, key: str) -> float:
        """Parse one Entry as float; allow thousand-separators as commas."""
        raw = self._entries[key].get().strip().replace(",", "")
        return float(raw)

    def _collect_inputs(self) -> SimInputs:
        """
        Read the form, validate, convert mm → m, return SimInputs.

        Raises ValueError on bad numbers or non-physical values (shown in a
        message box by _on_run).
        """
        diameter_mm = self._read_float("diameter_mm")
        length_mm = self._read_float("length_mm")
        propellant_kg = self._read_float("propellant_kg")
        mass_dry_kg = self._read_float("mass_dry_kg")
        cd = self._read_float("cd")
        altitude_goal_m = self._read_float("altitude_goal_m")
        mach_goal = self._read_float("mach_goal")
        motor_folder = self._entries["motor_folder"].get().strip() or "motorsim_output"

        if diameter_mm <= 0 or length_mm <= 0:
            raise ValueError("Diameter and length must be > 0.")
        if mass_dry_kg <= 0:
            raise ValueError("Vehicle mass (dry) must be > 0.")
        if propellant_kg < 0:
            raise ValueError("Propellant mass must be ≥ 0.")
        if cd < 0:
            raise ValueError("Cd must be ≥ 0.")

        return SimInputs(
            diameter_m=diameter_mm * 1e-3,
            length_m=length_mm * 1e-3,
            mass_dry_kg=mass_dry_kg,
            mass_propellant_kg=propellant_kg,
            cd=cd,
            altitude_goal_m=altitude_goal_m,
            mach_goal=mach_goal,
            motor_folder=motor_folder,
        )

    def _on_load_motor(self) -> None:
        """Browse for a motorsim_output-style folder and sanity-check the files."""
        initial = self._entries["motor_folder"].get().strip() or "."
        path = filedialog.askdirectory(
            title="Select motor output folder",
            initialdir=initial if Path(initial).is_dir() else ".",
        )
        if not path:
            return
        self._entries["motor_folder"].delete(0, "end")
        self._entries["motor_folder"].insert(0, path)
        try:
            motor = load_motor(path)
        except (FileNotFoundError, ValueError, OSError) as exc:
            messagebox.showerror("Motor load failed", str(exc))
            return
        messagebox.showinfo(
            "Motor loaded",
            f"Loaded burn history ({len(motor.time_s)} samples).\n"
            f"Burn time: {motor.burn_time_s:.2f} s\n"
            f"Total propellant (motor): {motor.total_propellant_kg:.3f} kg\n"
            f"Folder: {motor.source_dir}",
        )

    def _on_camera_change(self) -> None:
        """Radio button callback — switches camera without re-running the sim."""
        if self._anim_handles is None:
            return
        mode = self._camera_var.get()
        if mode in ("orbit", "follow", "nose"):
            self._anim_handles.set_camera_mode(mode)  # type: ignore[arg-type]

    def _stop_animation(self) -> None:
        """Stop the previous FuncAnimation timer before starting a new Run."""
        if self._anim_handles is not None:
            try:
                self._anim_handles.anim.event_source.stop()
            except Exception:  # noqa: BLE001
                pass
            self._anim_handles = None

    def _on_run(self) -> None:
        """
        Main button: validate → load motor → integrate → start animation.

        Errors are shown in message boxes so the user is not dumped to a
        console traceback when launching from the .bat file.
        """
        try:
            inputs = self._collect_inputs()
        except ValueError as exc:
            messagebox.showerror("Invalid input", str(exc) or "All numeric fields must be valid numbers.")
            return

        try:
            motor = load_motor(inputs.motor_folder)
        except FileNotFoundError as exc:
            messagebox.showerror("Motor output missing", str(exc))
            return
        except (ValueError, OSError) as exc:
            messagebox.showerror("Motor load failed", str(exc))
            return

        try:
            result = simulate(inputs, motor=motor)
        except Exception as exc:  # noqa: BLE001
            messagebox.showerror("Simulation error", f"Unexpected error:\n{exc}")
            return

        self._result = result
        self._start_animation(result)

    def _start_animation(self, result: TrajectoryResult) -> None:
        """Clear the axes, attach a new looping animation, keep a strong ref."""
        assert self._fig is not None and self._ax is not None and self._canvas is not None

        self._stop_animation()
        self._ax.cla()
        self._style_axes(self._ax)

        # Remove previous HUD fig.text artists (attach_animation adds new ones)
        for txt in list(self._fig.texts):
            try:
                txt.remove()
            except Exception:  # noqa: BLE001
                pass

        mode = self._camera_var.get()
        if mode not in ("orbit", "follow", "nose"):
            mode = "orbit"

        self._anim_handles = attach_animation(
            self._fig,
            self._ax,
            result,
            camera_mode=mode,  # type: ignore[arg-type]
        )
        # Keep strong references so GC does not kill the FuncAnimation
        self._canvas.mpl_connect("draw_event", lambda _evt: None)
        self._fig._trajectory_anim = self._anim_handles.anim  # type: ignore[attr-defined]
        self._canvas.draw_idle()


def main() -> int:
    """
    Entry used by __main__.py and `python gui.py`.

    Changes CWD to the project root so a relative motorsim_output/ path
    resolves the same way as when launching from Run Trajectory GUI.bat.
    """
    project_root = _HERE.parent
    try:
        import os

        os.chdir(project_root)
    except OSError:
        pass

    app = TrajectoryApp()
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
