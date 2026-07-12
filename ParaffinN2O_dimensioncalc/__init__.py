"""
ParaffinN2O_dimensioncalc — N2O / paraffin hybrid rocket motor sizing package.

Public entry points most users need:
  run_motor(MotorInputs)  -> MotorResult   (size + nozzle + simulate)
  size_motor / simulate_burn               (steps separately, if desired)
  analyze_nozzle                           (frozen nozzle only; see nozzle.py)

Front-ends:
  python -m ParaffinN2O_dimensioncalc          -> GUI (see __main__.py)
  python -m ParaffinN2O_dimensioncalc.cli ...  -> command line
"""

from .model import (
    PARAFFIN_DENSITY,
    MotorInputs,
    MotorResult,
    aluminum_case_wall_thickness_m,
    run_motor,
    size_motor,
    simulate_burn,
)
from .drawing import make_motor_drawing
from .nozzle import NozzleAnalysis, analyze_nozzle

# Names re-exported when someone does: from ParaffinN2O_dimensioncalc import *
__all__ = [
    "PARAFFIN_DENSITY",
    "MotorInputs",
    "MotorResult",
    "NozzleAnalysis",
    "aluminum_case_wall_thickness_m",
    "run_motor",
    "size_motor",
    "simulate_burn",
    "analyze_nozzle",
    "make_motor_drawing",
]
