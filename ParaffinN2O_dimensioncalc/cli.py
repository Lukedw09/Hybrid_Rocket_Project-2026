#!/usr/bin/env python3
"""
Command-line interface for the N2O / paraffin hybrid motor model.

Run from the project root:

    python -m ParaffinN2O_dimensioncalc.cli --case-od-mm 100 --wall-mm 3 ...

Or use the GUI instead (default when you run the package):

    python -m ParaffinN2O_dimensioncalc

This module also exposes helpers (format_summary, save_csv,
save_motor_export_json, make_plots) that the GUI reuses so both front-ends
print/save the same results.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt

from ParaffinN2O_dimensioncalc.model import MotorInputs, MotorResult, run_motor


def build_parser() -> argparse.ArgumentParser:
    """Define all CLI flags. Diameters are entered in mm; pressure in bar."""
    p = argparse.ArgumentParser(
        description=(
            "Size an N2O/paraffin hybrid motor and run a 1D circular-port burn model. "
            "Port/G_ox are solved for burn time; c* and Isp from frozen nozzle "
            "(gamma=1.25, Pe=1 atm)."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--case-od-mm", type=float, required=True, help="Motor case outer diameter [mm]")
    p.add_argument("--wall-mm", type=float, required=True, help="Case wall + liner thickness [mm]")
    p.add_argument("--fuel-mass", type=float, required=True, help="Fuel mass [kg]")
    p.add_argument("--burn-time", type=float, required=True, help="Target burn time [s]")
    p.add_argument("--pc-bar", type=float, required=True, help="Target chamber pressure [bar]")
    p.add_argument("--of", type=float, required=True, dest="of_ratio", help="Oxidizer-to-fuel mass ratio [-]")
    p.add_argument(
        "--total-impulse-kn-s",
        type=float,
        default=20.0,
        help=(
            "Design total impulse [kN·s]. Sets F_avg = I_total / t_burn for throat sizing. "
            "Default 20 kN·s (= 20,000 N·s)."
        ),
    )
    p.add_argument("--density", type=float, default=834.0, help="Paraffin fuel density [kg/m^3]")
    p.add_argument("--dt", type=float, default=0.01, help="Integration time step [s]")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path("motorsim_output"),
        help="Directory for plots and CSV time history",
    )
    p.add_argument("--no-show", action="store_true", help="Save plots without opening a window")
    p.add_argument("--no-save", action="store_true", help="Show plots without writing files")
    return p


def inputs_from_args(args: argparse.Namespace) -> MotorInputs:
    """
    Convert argparse values (mm, bar, kN·s) into the SI MotorInputs dataclass.

    Conversions:
      mm  -> m     (* 1e-3)
      bar -> Pa    (* 1e5)
      kN·s -> N·s  (* 1e3)
    """
    return MotorInputs(
        case_od_m=args.case_od_mm * 1e-3,
        wall_thickness_m=args.wall_mm * 1e-3,
        fuel_mass_kg=args.fuel_mass,
        burn_time_s=args.burn_time,
        chamber_pressure_pa=args.pc_bar * 1e5,
        of_ratio=args.of_ratio,
        total_impulse_n_s=args.total_impulse_kn_s * 1e3,
        dt_s=args.dt,
        fuel_density_kg_m3=args.density,
    )


def format_summary(vals: dict[str, float], result: MotorResult) -> str:
    """
    Build a human-readable text report of inputs, solved geometry, nozzle, and burn.

    `vals` uses the same keys as the GUI field list (mm / bar / kN·s friendly units)
    so both CLI and GUI can share one formatter.
    """
    g = result.geometry
    p = result.performance
    n = p.nozzle
    h = result.history

    # Guard empty histories (should not happen in normal runs).
    t_end = float(h.time_s[-1]) if len(h.time_s) else 0.0
    fuel_end = float(h.fuel_consumed_kg[-1]) if len(h.fuel_consumed_kg) else 0.0
    gox_final = float(h.gox_kg_s_m2[-1]) if len(h.gox_kg_s_m2) else 0.0

    burn_time = vals["burn_time"]
    fuel_mass = vals["fuel_mass"]
    total_impulse_kn_s = vals["total_impulse_kn_s"]

    lines = [
        "=" * 60,
        "N2O / paraffin hybrid motor - sizing & 1D burn",
        "=" * 60,
        "Inputs",
        f"  Case OD              : {vals['case_od_mm']:.2f} mm",
        f"  Wall / liner         : {vals['wall_mm']:.2f} mm",
        f"  Fuel mass            : {fuel_mass:.4f} kg",
        f"  Target burn time     : {burn_time:.3f} s",
        f"  Chamber pressure     : {vals['pc_bar']:.2f} bar",
        f"  O/F ratio            : {vals['of_ratio']:.3f}",
        f"  Total impulse        : {total_impulse_kn_s:.3f} kN*s",
        f"  Fuel density         : {vals['density']:.1f} kg/m^3",
        "",
        # Geometry section: port and G_ox are *solved*, not user inputs.
        "Geometry (solved)",
        f"  Grain OD             : {g.grain_od_m*1e3:.2f} mm",
        f"  Initial port ID      : {g.port_diameter_m*1e3:.2f} mm",
        f"  Grain length         : {g.grain_length_m*1e3:.2f} mm",
        f"  Web thickness        : {g.web_thickness_m*1e3:.2f} mm",
        f"  Initial G_ox         : {g.gox_initial_kg_s_m2:.1f} kg/(s*m^2)",
        f"  Final G_ox           : {gox_final:.1f} kg/(s*m^2)",
        f"  Oxidizer mass        : {g.oxidizer_mass_kg:.4f} kg",
        f"  m_dot_ox (constant)  : {g.m_dot_ox_kg_s:.5f} kg/s",
        "",
        "Frozen nozzle (gamma=1.25, Pe=Pa=1 atm)",
        f"  Design O/F           : {n.of_ratio:.3f}",
        f"  Exit Mach            : {n.exit_mach:.3f}",
        f"  Expansion ratio Ae/At: {n.expansion_ratio:.3f}",
        f"  Throat diameter      : {n.throat_diameter_m*1e3:.2f} mm",
        f"  Exit diameter        : {n.exit_diameter_m*1e3:.2f} mm",
        f"  C_F (sea level)      : {n.cf_sea_level:.4f}",
        f"  C_F (chamber/vac)    : {n.cf_chamber:.4f}",
        f"  c* (P_c*A_t/m_dot)   : {n.c_star_m_s:.1f} m/s",
        f"  I_sp sea level       : {n.isp_sea_level_s:.1f} s",
        f"  I_sp chamber         : {n.isp_chamber_s:.1f} s",
        f"  Design thrust (avg)  : {n.thrust_avg_n:.1f} N",
        f"  m_dot_avg            : {n.m_dot_avg_kg_s:.5f} kg/s",
        f"  Total propellant     : {p.total_propellant_kg:.4f} kg",
        "",
        "Simulation",
        f"  Simulated duration   : {t_end:.3f} s",
        f"  Fuel consumed        : {fuel_end:.4f} kg / {fuel_mass:.4f} kg",
        f"  Final port diameter  : {h.port_diameter_m[-1]*1e3:.2f} mm",
        f"  Burnout reason       : {h.burnout_reason}",
    ]

    # Soft warning if the time-march did not land near the design burn time.
    if abs(t_end - burn_time) > 0.05 * burn_time:
        lines.append(
            f"  NOTE: simulated burn ({t_end:.3f} s) differs from target "
            f"({burn_time:.3f} s). Check fuel mass vs web volume or time step."
        )
    lines.append("=" * 60)
    return "\n".join(lines)


def print_summary(args: argparse.Namespace, result: MotorResult) -> None:
    """CLI wrapper: map argparse fields into the shared format_summary dict."""
    vals = {
        "case_od_mm": args.case_od_mm,
        "wall_mm": args.wall_mm,
        "fuel_mass": args.fuel_mass,
        "burn_time": args.burn_time,
        "pc_bar": args.pc_bar,
        "of_ratio": args.of_ratio,
        "total_impulse_kn_s": args.total_impulse_kn_s,
        "density": args.density,
    }
    print(format_summary(vals, result))


def save_motor_export_json(path: Path, result: MotorResult) -> None:
    """
    Write motor_export.json for trajectory / altitude thrust correction.

    CSV remains the source of truth for the full burn series; this file mirrors
    the thrust and m_dot columns plus nozzle scalars needed downstream.
    """
    h = result.history
    n = result.performance.nozzle
    payload = {
        "time_s": [float(x) for x in h.time_s],
        "thrust_N": [float(x) for x in h.thrust_n],
        "m_dot_total_kg_s": [float(x) for x in h.m_dot_total_kg_s],
        "exit_area_m2": float(n.exit_area_m2),
        "exit_pressure_pa": float(n.exit_pressure_pa),
        "throat_area_m2": float(n.throat_area_m2),
        "isp_sea_level_s": float(n.isp_sea_level_s),
        "total_propellant_kg": float(result.performance.total_propellant_kg),
        "burnout_reason": h.burnout_reason,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def save_csv(path: Path, result: MotorResult) -> None:
    """
    Write the burn time-history to CSV for Excel / MATLAB / further plotting.

    Also writes motor_export.json in the same directory for trajectory handoff.

    Lengths and rates are converted to mm / mm/s in the file for readability;
    mass flows stay in kg/s; pressure is written in bar.
    """
    h = result.history
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "time_s",
                "port_diameter_mm",
                "regression_rate_mm_s",
                "gox_kg_s_m2",
                "m_dot_fuel_kg_s",
                "m_dot_total_kg_s",
                "of_ratio",
                "thrust_N",
                "chamber_pressure_bar",
                "fuel_consumed_kg",
            ]
        )
        for i in range(len(h.time_s)):
            w.writerow(
                [
                    f"{h.time_s[i]:.6f}",
                    f"{h.port_diameter_m[i]*1e3:.6f}",
                    f"{h.regression_rate_m_s[i]*1e3:.6f}",
                    f"{h.gox_kg_s_m2[i]:.6f}",
                    f"{h.m_dot_fuel_kg_s[i]:.8f}",
                    f"{h.m_dot_total_kg_s[i]:.8f}",
                    f"{h.of_ratio[i]:.6f}",
                    f"{h.thrust_n[i]:.6f}",
                    f"{h.chamber_pressure_pa[i]/1e5:.6f}",
                    f"{h.fuel_consumed_kg[i]:.8f}",
                ]
            )
    save_motor_export_json(path.parent / "motor_export.json", result)


def make_plots(result: MotorResult, out_dir: Path | None, show: bool) -> None:
    """
    Three stacked plots vs time: port diameter, thrust, and regression rate.

    If out_dir is given, also save burn_history.png there.
    If show is True, open an interactive matplotlib window (blocks until closed).
    """
    h = result.history
    t = h.time_s
    fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

    # Port growth — dashed line marks the grain OD (web burn-through limit).
    axes[0].plot(t, h.port_diameter_m * 1e3, color="#1f4e79", lw=2)
    axes[0].axhline(
        result.geometry.grain_od_m * 1e3,
        color="#9b2c2c",
        ls="--",
        lw=1.2,
        label="Grain OD",
    )
    axes[0].set_ylabel("Port diameter [mm]")
    axes[0].set_title("Port growth, thrust, and regression rate vs time")
    axes[0].legend(loc="best")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(t, h.thrust_n, color="#b35c00", lw=2)
    axes[1].set_ylabel("Thrust [N]")
    axes[1].grid(True, alpha=0.3)

    # Regression rate falls as G_ox falls (port opens up).
    axes[2].plot(t, h.regression_rate_m_s * 1e3, color="#2f6b3a", lw=2)
    axes[2].set_ylabel("Burn rate [mm/s]")
    axes[2].set_xlabel("Time [s]")
    axes[2].grid(True, alpha=0.3)

    fig.tight_layout()

    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)
        fig_path = out_dir / "burn_history.png"
        fig.savefig(fig_path, dpi=150)
        print(f"Wrote {fig_path}")

    if show:
        plt.show()
    else:
        # Important when batch-running: free the figure so memory does not grow.
        plt.close(fig)


def main(argv: list[str] | None = None) -> int:
    """
    CLI entry point.

    Returns 0 on success, 1 on a sizing/validation error (so scripts can detect failure).
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = run_motor(inputs_from_args(args))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print_summary(args, result)

    out_dir = None if args.no_save else args.out_dir
    if out_dir is not None:
        csv_path = out_dir / "burn_history.csv"
        save_csv(csv_path, result)
        print(f"Wrote {csv_path}")
        print(f"Wrote {out_dir / 'motor_export.json'}")

    make_plots(result, out_dir=out_dir, show=not args.no_show)
    return 0


# Allows: python -m ParaffinN2O_dimensioncalc.cli
if __name__ == "__main__":
    raise SystemExit(main())
