"""Project-specific radial bolt FS at hydroproof — companion to RESEARCH_BRIEF.md."""
from __future__ import annotations

import math

# Preferred chamber (Mach 1 Hybrid Rocket Project.md)
DI_IN, DO_IN, T_IN = 5.75, 6.0, 0.125
DI, DO, T = (x * 0.0254 for x in (DI_IN, DO_IN, T_IN))

# 6061-T6 at ~200 F (HalfCat conservative values)
YTS_AL = 38e3 * 6894.76
SHEAR_AL = 30e3 * 6894.76
BYS_AL = 56e3 * 6894.76

# 1/4-28 Grade 8 (HalfCat worked-example diameters; Grade 8 UTS)
D_MAJ = 0.2500 * 0.0254
D_MIN = 0.2052 * 0.0254
UTS_BOLT = 150e3 * 6894.76
SHEAR_BOLT = 0.75 * UTS_BOLT
E = 2.0 * D_MAJ  # recommended edge distance
EMIN = E - D_MAJ / 2


def pa(bar: float) -> float:
    return bar * 1e5


def analyze(p_bar: float, n: int) -> dict[str, float]:
    p = pa(p_bar)
    force = p * math.pi / 4 * DI**2
    fb = force / n
    sigma_h = p * DI / (2 * T)
    sigma_a = p * DI / (4 * T)
    ab = math.pi / 4 * D_MIN**2
    tau_b = force / (n * ab)
    tau_to = fb / (EMIN * 2 * T)
    a_net = ((DO - T) * math.pi - n * D_MAJ) * T
    sigma_t = force / a_net
    sigma_br = fb / (D_MAJ * T)
    return {
        "F_kN": force / 1000,
        "FS_hoop_y": YTS_AL / sigma_h,
        "FS_axial_y": YTS_AL / sigma_a,
        "FS_bolt": SHEAR_BOLT / tau_b,
        "FS_tearout": SHEAR_AL / tau_to,
        "FS_tensile": YTS_AL / sigma_t,
        "FS_bearing": BYS_AL / sigma_br,
    }


def main() -> None:
    print(f"Di={DI*1000:.2f} mm  t={T*1000:.2f} mm  E=2d={E*1000:.2f} mm")
    for p in (40.0, 45.0, 60.0):
        print(f"\n--- P = {p:.0f} bar ---")
        for n in (6, 8, 10, 12, 14, 16, 18, 20, 24):
            r = analyze(p, n)
            m = min(r["FS_bolt"], r["FS_tearout"], r["FS_tensile"], r["FS_bearing"])
            print(
                f"N={n:2d}  F={r['F_kN']:5.1f} kN  "
                f"bolt={r['FS_bolt']:4.2f}  tear={r['FS_tearout']:4.2f}  "
                f"tens={r['FS_tensile']:4.2f}  bear={r['FS_bearing']:4.2f}  "
                f"min={m:4.2f}"
            )


if __name__ == "__main__":
    main()
