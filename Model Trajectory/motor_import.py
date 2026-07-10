"""
Load motor burn history for the trajectory simulator.

================================================================================
WHAT THIS MODULE DOES
================================================================================
The trajectory code does *not* re-run the hybrid motor sizing model. Instead it
reads the files that ParaffinN2O_dimensioncalc already wrote under something
like motorsim_output/:

  burn_history.csv   — time series (source of truth for F(t) and m_dot(t))
  motor_export.json  — nozzle scalars (exit area, etc.) for altitude thrust fix

load_motor(folder) returns a MotorData object. During flight integration,
dynamics.py calls motor.thrust_sl(t) and motor.m_dot(t), which linearly
interpolate those tables. After the last CSV sample, both return 0 (burnout).

================================================================================
WHY TWO FILES?
================================================================================
The CSV has the burn curve. The JSON has A_e and related scalars that are *not*
in every CSV column set, but are needed to correct sea-level thrust for ambient
pressure as the rocket climbs:

    F(h) = F_sl(t) + (P_sl - P_a(h)) * A_e

If either file is missing, we raise FileNotFoundError with a message that
points the user back to "Run Motor GUI.bat".

================================================================================
UNITS
================================================================================
Everything here is SI: seconds, newtons, kg/s, m², Pa.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

CSV_NAME = "burn_history.csv"
JSON_NAME = "motor_export.json"

_MISSING_MSG = (
    "Motor output not found. Run the motor sizing tool first "
    '(double-click "Run Motor GUI.bat" or: python -m ParaffinN2O_dimensioncalc), '
    f"then point this app at the folder containing {CSV_NAME} and {JSON_NAME}."
)


# =============================================================================
# Data container
# =============================================================================


@dataclass(frozen=True)
class MotorData:
    """
    Sea-level thrust / mass-flow histories plus nozzle scalars.

    frozen=True makes instances immutable after construction — safe to share
    between the GUI, the integrator, and the animation without accidental edits.

    Arrays are parallel: time_s[i], thrust_n[i], m_dot_total_kg_s[i] are one
    sample from the motor burn simulation.
    """

    time_s: np.ndarray
    thrust_n: np.ndarray
    m_dot_total_kg_s: np.ndarray
    exit_area_m2: float
    exit_pressure_pa: float
    throat_area_m2: float
    isp_sea_level_s: float
    total_propellant_kg: float
    burnout_reason: str
    source_dir: Path

    @property
    def burn_time_s(self) -> float:
        """Duration of the tabulated burn history [s] (last time sample)."""
        if len(self.time_s) == 0:
            return 0.0
        return float(self.time_s[-1])

    def thrust_sl(self, t: float) -> float:
        """
        Sea-level thrust [N] at simulation time t.

        Linear interpolation between CSV samples. Before the first sample we
        hold the first value; after the last sample we return 0 (engine off).
        """
        return float(_interp_clamp(self.time_s, self.thrust_n, t, after=0.0))

    def m_dot(self, t: float) -> float:
        """
        Total propellant mass flow [kg/s] at time t (fuel + oxidizer).

        Same interpolation rules as thrust_sl. The flight integrator uses this
        to deplete remaining propellant mass.
        """
        return float(_interp_clamp(self.time_s, self.m_dot_total_kg_s, t, after=0.0))


def _interp_clamp(
    t_grid: np.ndarray,
    y_grid: np.ndarray,
    t: float,
    *,
    after: float,
) -> float:
    """
    1-D linear interpolation with explicit end behavior.

    np.interp alone would clamp to the *last* y value past the end of the
    table. For a rocket motor we want thrust/m_dot → 0 after burnout, so we
    pass that as `after` and only use np.interp inside the table span.
    """
    if len(t_grid) == 0:
        return after
    if t < t_grid[0]:
        return float(y_grid[0])
    if t > t_grid[-1]:
        return after
    return float(np.interp(t, t_grid, y_grid))


# =============================================================================
# Public loader
# =============================================================================


def load_motor(folder: str | Path) -> MotorData:
    """
    Load burn_history.csv + motor_export.json from a motor output folder.

    Typical call:
        motor = load_motor("motorsim_output")
        F = motor.thrust_sl(2.5)   # newtons at t = 2.5 s
    """
    folder = Path(folder)
    csv_path = folder / CSV_NAME
    json_path = folder / JSON_NAME

    if not csv_path.is_file() or not json_path.is_file():
        raise FileNotFoundError(_MISSING_MSG)

    time_s, thrust_n, m_dot = _read_burn_csv(csv_path)
    meta = _read_export_json(json_path)

    return MotorData(
        time_s=time_s,
        thrust_n=thrust_n,
        m_dot_total_kg_s=m_dot,
        exit_area_m2=float(meta["exit_area_m2"]),
        exit_pressure_pa=float(meta["exit_pressure_pa"]),
        throat_area_m2=float(meta["throat_area_m2"]),
        isp_sea_level_s=float(meta["isp_sea_level_s"]),
        total_propellant_kg=float(meta["total_propellant_kg"]),
        burnout_reason=str(meta.get("burnout_reason", "")),
        source_dir=folder.resolve(),
    )


def _read_burn_csv(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Parse burn_history.csv into parallel NumPy arrays.

    DictReader maps column headers → values per row. We only need three
    columns; the motor tool may write more (port diameter, O/F, …).
    """
    times: list[float] = []
    thrusts: list[float] = []
    mdots: list[float] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"time_s", "thrust_N", "m_dot_total_kg_s"}
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"{path.name} is missing required columns {sorted(required)}. "
                "Re-run the motor tool to regenerate the CSV."
            )
        for row in reader:
            times.append(float(row["time_s"]))
            thrusts.append(float(row["thrust_N"]))
            mdots.append(float(row["m_dot_total_kg_s"]))

    if not times:
        raise ValueError(f"{path.name} has no data rows.")

    return (
        np.asarray(times, dtype=float),
        np.asarray(thrusts, dtype=float),
        np.asarray(mdots, dtype=float),
    )


def _read_export_json(path: Path) -> dict:
    """
    Parse motor_export.json nozzle / bookkeeping scalars.

    Written by ParaffinN2O_dimensioncalc when it saves burn_history.csv.
    """
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    required = (
        "exit_area_m2",
        "exit_pressure_pa",
        "throat_area_m2",
        "isp_sea_level_s",
        "total_propellant_kg",
    )
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(
            f"{path.name} is missing keys {missing}. "
            "Re-run the motor tool so save_csv writes a complete motor_export.json."
        )
    return data
