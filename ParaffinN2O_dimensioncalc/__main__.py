"""
Package entry point for `python -m ParaffinN2O_dimensioncalc`.

By default this opens the GUI. For scripting / automation, call the CLI module:

    python -m ParaffinN2O_dimensioncalc.cli --case-od-mm 100 ...
"""

from ParaffinN2O_dimensioncalc.gui import main

if __name__ == "__main__":
    raise SystemExit(main())
