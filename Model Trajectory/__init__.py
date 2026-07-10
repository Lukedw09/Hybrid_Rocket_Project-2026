"""
Model Trajectory — 9-state near-vertical flight simulator.

Coordinate system: y up, launch at origin, small x/z drift from attitude hold.
Requires motorsim_output/burn_history.csv + motor_export.json from the motor tool.
"""

from __future__ import annotations

__all__ = [
    "atmosphere",
    "motor_import",
    "dynamics",
    "simulate",
    "geometry",
    "animate",
]
