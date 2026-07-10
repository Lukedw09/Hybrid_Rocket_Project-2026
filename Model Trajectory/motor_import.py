"""
Load motor burn history for trajectory simulation.

Requires both burn_history.csv (series source of truth) and motor_export.json
(nozzle scalars for altitude thrust correction) from ParaffinN2O_dimensioncalc.
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


@dataclass(frozen=True)
class MotorData:
    """Sea-level thrust / mass-flow histories plus nozzle scalars."""

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
        """Duration of the tabulated burn history [s]."""
        if len(self.time_s) == 0:
            return 0.0
        return float(self.time_s[-1])

    def thrust_sl(self, t: float) -> float:
        """Linearly interpolate sea-level thrust [N] at time t. Zero after burn."""
        return float(_interp_clamp(self.time_s, self.thrust_n, t, after=0.0))

    def m_dot(self, t: float) -> float:
        """Linearly interpolate total propellant mass flow [kg/s]. Zero after burn."""
        return float(_interp_clamp(self.time_s, self.m_dot_total_kg_s, t, after=0.0))


def _interp_clamp(
    t_grid: np.ndarray,
    y_grid: np.ndarray,
    t: float,
    *,
    after: float,
) -> float:
    """Linear interpolation; return `after` when t is past the last sample."""
    if len(t_grid) == 0:
        return after
    if t < t_grid[0]:
        return float(y_grid[0])
    if t > t_grid[-1]:
        return after
    return float(np.interp(t, t_grid, y_grid))


def load_motor(folder: str | Path) -> MotorData:
    """
    Load burn_history.csv + motor_export.json from a motor output folder.

    CSV columns used: time_s, thrust_N, m_dot_total_kg_s.
    JSON supplies exit_area_m2 and related scalars (required).
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
    """Parse burn_history.csv; CSV is the source of truth for time series."""
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
    """Parse motor_export.json nozzle / bookkeeping scalars."""
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
