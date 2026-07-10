"""
Entry point for the trajectory GUI.

================================================================================
HOW TO LAUNCH
================================================================================
The folder name contains a space, so prefer one of:

    python "Model Trajectory/gui.py"
    double-click "Run Trajectory GUI.bat"

Running this file also works if the working directory can resolve local
imports after the sys.path bootstrap below:

    python "Model Trajectory/__main__.py"

That bootstrap inserts this folder on sys.path so sibling modules
(atmosphere, simulate, gui, …) import as top-level names.
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from gui import main

if __name__ == "__main__":
    raise SystemExit(main())
