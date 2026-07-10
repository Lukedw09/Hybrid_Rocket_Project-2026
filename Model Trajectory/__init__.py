"""
Model Trajectory — 9-state near-vertical flight simulator.

================================================================================
READING ORDER (recommended)
================================================================================
  1. motor_import.py  — load thrust / m_dot from the motor tool
  2. atmosphere.py    — ISA density, pressure, speed of sound, Mach
  3. dynamics.py      — forces, attitude hold, RK4 step (core physics)
  4. simulate.py      — boost + coast loop → TrajectoryResult
  5. geometry.py      — visual rocket mesh only
  6. animate.py       — 3D path, HUD, camera modes
  7. gui.py           — tkinter form that calls simulate + animate

================================================================================
COORDINATE SYSTEM
================================================================================
  y up, launch at origin, small x/z drift from the attitude hold.
  Requires motorsim_output/burn_history.csv + motor_export.json from the
  ParaffinN2O_dimensioncalc motor tool.

Launch: double-click "Run Trajectory GUI.bat" from the project root.
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
