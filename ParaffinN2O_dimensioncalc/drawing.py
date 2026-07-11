"""
SolidWorks-style longitudinal cross-section drawings of the sized hybrid motor.

Shows two views on one figure:
  1. Full motor (case + grain + nozzle) — SECTION A-A
  2. Nozzle detail — DETAIL B

Only calculated dimensions are labeled (case OD, wall, grain OD/ID/length,
throat & exit diameters). Injector, tank, and airframe are omitted. Nozzle
axial contour uses standard conical half-angles solely to draw a plausible
shape; those lengths are not design outputs and are not dimensioned.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

from ParaffinN2O_dimensioncalc.model import MotorInputs, MotorResult

# Conical half-angles for schematic nozzle outline only (not sized by the model).
_CONV_HALF_DEG = 45.0
_DIV_HALF_DEG = 15.0

# Drawing appearance (SolidWorks-like section view).
_BG = "#e8e8e8"
_EDGE = "#000000"
_DIM = "#000000"
_CENTER = "#333333"
_CASE_HATCH = {"facecolor": "none", "edgecolor": _EDGE, "hatch": "///", "lw": 1.4}
_GRAIN_HATCH = {"facecolor": "#d0d0d0", "edgecolor": _EDGE, "hatch": "...", "lw": 1.2}
_NOZZLE_HATCH = {"facecolor": "none", "edgecolor": _EDGE, "hatch": "\\\\\\", "lw": 1.4}


def _mm(m: float) -> float:
    return m * 1e3


def _poly(ax, xy: list[tuple[float, float]], **style) -> None:
    ax.add_patch(Polygon(xy, closed=True, **style))


def _centerline(ax, x0: float, x1: float, y: float = 0.0) -> None:
    ax.plot(
        [x0, x1],
        [y, y],
        color=_CENTER,
        lw=0.8,
        ls=(0, (6, 2, 1, 2)),
        zorder=0,
    )


def _arrowheads(ax, p0: tuple[float, float], p1: tuple[float, float], size: float) -> None:
    """Small filled triangular arrowheads at both ends of a dimension line."""
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    length = float(np.hypot(dx, dy))
    if length < 1e-9:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy, ux  # perpendicular
    hs = size
    hw = size * 0.45

    def head(tip: tuple[float, float], direction: float) -> None:
        tx, ty = tip
        bx, by = tx - direction * ux * hs, ty - direction * uy * hs
        ax.add_patch(
            Polygon(
                [
                    (tx, ty),
                    (bx + px * hw, by + py * hw),
                    (bx - px * hw, by - py * hw),
                ],
                closed=True,
                facecolor=_DIM,
                edgecolor=_DIM,
                lw=0.3,
                zorder=5,
                clip_on=False,
            )
        )

    ax.plot([x0, x1], [y0, y1], color=_DIM, lw=0.65, clip_on=False, zorder=4)
    head((x0, y0), -1.0)
    head((x1, y1), 1.0)


def _dim_horizontal(
    ax,
    x0: float,
    x1: float,
    y: float,
    text: str,
    *,
    offset: float = 0.0,
    fontsize: float = 8,
    head: float = 2.2,
) -> None:
    """Horizontal dimension with arrowheads (SolidWorks style)."""
    xa, xb = min(x0, x1), max(x0, x1)
    y_line = y + offset
    ax.plot([xa, xa], [y, y_line], color=_DIM, lw=0.55, clip_on=False)
    ax.plot([xb, xb], [y, y_line], color=_DIM, lw=0.55, clip_on=False)
    _arrowheads(ax, (xa, y_line), (xb, y_line), head)
    ax.text(
        0.5 * (xa + xb),
        y_line + head * 0.35,
        text,
        ha="center",
        va="bottom",
        fontsize=fontsize,
        color=_DIM,
        clip_on=False,
        bbox=dict(boxstyle="square,pad=0.12", fc=_BG, ec="none", alpha=0.95),
    )


def _dim_diameter(
    ax,
    x: float,
    r: float,
    text: str,
    *,
    side: str = "right",
    span: float | None = None,
    fontsize: float = 8,
    head: float = 2.2,
    text_offset: float = 0.0,
) -> None:
    """Vertical diameter dimension through the centerline at axial station x."""
    if span is None:
        span = max(abs(r) * 0.25, 6.0)
    x_line = x + span if side == "right" else x - span
    ax.plot([x, x_line], [r, r], color=_DIM, lw=0.55, clip_on=False)
    ax.plot([x, x_line], [-r, -r], color=_DIM, lw=0.55, clip_on=False)
    _arrowheads(ax, (x_line, -r), (x_line, r), head)
    ha = "left" if side == "right" else "right"
    x_text = x_line + (2.5 + text_offset if side == "right" else -(2.5 + text_offset))
    ax.text(
        x_text,
        0.0,
        text,
        ha=ha,
        va="center",
        fontsize=fontsize,
        color=_DIM,
        rotation=90,
        clip_on=False,
        bbox=dict(boxstyle="square,pad=0.1", fc=_BG, ec="none", alpha=0.95),
    )


def _nozzle_radii_and_lengths(
    chamber_id_mm: float,
    throat_mm: float,
    exit_mm: float,
) -> tuple[float, float, float, float, float]:
    """
    Return (r_chamber, r_throat, r_exit, L_conv, L_div) in mm.

    Conical lengths come from fixed half-angles for drawing only.
    """
    r_c = 0.5 * chamber_id_mm
    r_t = 0.5 * throat_mm
    r_e = 0.5 * exit_mm
    L_conv = (r_c - r_t) / np.tan(np.deg2rad(_CONV_HALF_DEG))
    L_div = (r_e - r_t) / np.tan(np.deg2rad(_DIV_HALF_DEG))
    L_conv = max(float(L_conv), 1.0)
    L_div = max(float(L_div), 1.0)
    return r_c, r_t, r_e, L_conv, L_div


def _nozzle_outer_upper(
    x_start: float,
    x_throat: float,
    x_exit: float,
    r_case: float,
    r_exit_outer: float,
) -> list[tuple[float, float]]:
    """
    Outer nozzle wall (upper half).

    Holds case OD through the convergent, then tapers on the divergent —
    similar to a flanged nozzle blank in a section drawing.
    """
    # Keep OD = case through most of the convergent; begin taper near throat.
    x_shoulder = x_start + 0.85 * (x_throat - x_start)
    return [
        (x_start, r_case),
        (x_shoulder, r_case),
        (x_throat, max(r_case * 0.85, r_exit_outer * 1.15)),
        (x_exit, r_exit_outer),
    ]


def _build_motor_polygons(
    inp: MotorInputs,
    result: MotorResult,
) -> dict:
    """Compute mm-space polygons and key stations for both views."""
    g = result.geometry
    n = result.performance.nozzle

    case_od = _mm(inp.case_od_m)
    wall = _mm(inp.wall_thickness_m)
    grain_od = _mm(g.grain_od_m)
    port = _mm(g.port_diameter_m)
    L_grain = _mm(g.grain_length_m)
    Dt = _mm(n.throat_diameter_m)
    De = _mm(n.exit_diameter_m)

    r_case = 0.5 * case_od
    r_grain = 0.5 * grain_od
    r_port = 0.5 * port

    # Chamber ID at nozzle entry ≈ grain OD (combustion port opens to grain OD).
    r_c, r_t, r_e, L_conv, L_div = _nozzle_radii_and_lengths(grain_od, Dt, De)

    x0 = 0.0
    x_grain_end = L_grain
    x_throat = x_grain_end + L_conv
    x_exit = x_throat + L_div

    # Case wall: outer case OD, inner case ID (= grain OD), full grain length.
    case_upper = [
        (x0, r_grain),
        (x0, r_case),
        (x_grain_end, r_case),
        (x_grain_end, r_grain),
    ]
    case_poly = case_upper + [(x, -y) for x, y in reversed(case_upper)]

    # Fuel grain annulus (initial port).
    grain_upper = [
        (x0, r_port),
        (x0, r_grain),
        (x_grain_end, r_grain),
        (x_grain_end, r_port),
    ]
    grain_poly = grain_upper + [(x, -y) for x, y in reversed(grain_upper)]

    # Nozzle solid: outer profile vs convergent–divergent gas path.
    r_exit_outer = max(r_e + wall, r_case * 0.55)
    outer_u = _nozzle_outer_upper(
        x_grain_end, x_throat, x_exit, r_case, r_exit_outer
    )
    inner_u = [
        (x_grain_end, r_c),
        (x_throat, r_t),
        (x_exit, r_e),
    ]
    # Walk outer left→right, then inner right→left to close the solid region.
    nozzle_upper = outer_u + list(reversed(inner_u))
    nozzle_poly = nozzle_upper + [(x, -y) for x, y in reversed(nozzle_upper)]

    return {
        "case_od": case_od,
        "wall": wall,
        "grain_od": grain_od,
        "port": port,
        "L_grain": L_grain,
        "Dt": Dt,
        "De": De,
        "r_case": r_case,
        "r_grain": r_grain,
        "r_port": r_port,
        "r_t": r_t,
        "r_e": r_e,
        "r_c": r_c,
        "L_conv": L_conv,
        "L_div": L_div,
        "x0": x0,
        "x_grain_end": x_grain_end,
        "x_throat": x_throat,
        "x_exit": x_exit,
        "case_poly": case_poly,
        "grain_poly": grain_poly,
        "nozzle_poly": nozzle_poly,
        "expansion_ratio": n.expansion_ratio,
    }


def _style_axes(ax, title: str) -> None:
    ax.set_facecolor(_BG)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    for spine in ax.spines.values():
        spine.set_visible(False)


def _draw_full_motor(ax, geom: dict) -> None:
    _poly(ax, geom["case_poly"], **_CASE_HATCH)
    _poly(ax, geom["grain_poly"], **_GRAIN_HATCH)
    _poly(ax, geom["nozzle_poly"], **_NOZZLE_HATCH)

    # Port / chamber cavity outline (gas path through grain).
    ax.plot(
        [geom["x0"], geom["x_grain_end"]],
        [geom["r_port"], geom["r_port"]],
        color=_EDGE,
        lw=1.0,
    )
    ax.plot(
        [geom["x0"], geom["x_grain_end"]],
        [-geom["r_port"], -geom["r_port"]],
        color=_EDGE,
        lw=1.0,
    )

    pad = max(geom["r_case"] * 0.18, 14.0)
    _centerline(ax, geom["x0"] - pad * 0.3, geom["x_exit"] + pad * 0.3)

    # Dimensions — calculated body parameters that define the motor.
    _dim_horizontal(
        ax,
        geom["x0"],
        geom["x_grain_end"],
        geom["r_case"],
        f"{geom['L_grain']:.1f}",
        offset=pad * 0.9,
        head=2.0,
    )
    _dim_diameter(
        ax,
        geom["x0"],
        geom["r_case"],
        f"Ø{geom['case_od']:.1f}",
        side="left",
        span=pad * 0.7,
        head=2.0,
    )
    # Grain OD inside the case, mid-grain.
    _dim_diameter(
        ax,
        0.28 * geom["L_grain"],
        geom["r_grain"],
        f"Ø{geom['grain_od']:.1f}",
        side="right",
        span=pad * 0.35,
        head=1.8,
        fontsize=7.5,
    )
    # Initial port ID — dimensioned in the bore.
    _dim_diameter(
        ax,
        0.62 * geom["L_grain"],
        geom["r_port"],
        f"Ø{geom['port']:.1f}",
        side="right",
        span=pad * 0.25,
        head=1.8,
        fontsize=7.5,
    )
    # Wall / liner thickness (radial).
    xw = geom["x0"] + min(0.1 * geom["L_grain"], 18.0)
    y_wall = 0.5 * (geom["r_grain"] + geom["r_case"])
    ax.annotate(
        f"{geom['wall']:.1f}",
        xy=(xw, y_wall),
        xytext=(xw + pad * 0.55, geom["r_case"] + pad * 0.28),
        fontsize=8,
        color=_DIM,
        arrowprops=dict(arrowstyle="-", color=_DIM, lw=0.55),
        bbox=dict(boxstyle="square,pad=0.1", fc=_BG, ec="none", alpha=0.95),
    )

    # Throat / exit (also expanded in DETAIL B).
    _dim_diameter(
        ax,
        geom["x_throat"],
        geom["r_t"],
        f"Ø{geom['Dt']:.1f}",
        side="right",
        span=pad * 0.4,
        head=1.6,
        fontsize=7,
    )
    _dim_diameter(
        ax,
        geom["x_exit"],
        geom["r_e"],
        f"Ø{geom['De']:.1f}",
        side="right",
        span=pad * 0.45,
        head=1.6,
        fontsize=7,
    )

    ax.text(
        0.5 * (geom["x0"] + geom["x_grain_end"]),
        -geom["r_case"] - pad * 0.5,
        "SECTION A-A",
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=_EDGE,
    )
    ax.text(
        0.02,
        0.98,
        "mm",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        color="#555555",
    )

    ax.set_xlim(geom["x0"] - pad * 1.6, geom["x_exit"] + pad * 1.5)
    ax.set_ylim(-geom["r_case"] - pad * 1.2, geom["r_case"] + pad * 1.55)


def _draw_nozzle_detail(ax, geom: dict) -> None:
    # Shift geometry so nozzle starts at x=0 for the detail view.
    dx = geom["x_grain_end"]
    shift = lambda pts: [(x - dx, y) for x, y in pts]

    _poly(ax, shift(geom["nozzle_poly"]), **_NOZZLE_HATCH)

    # Short remnant of case/grain at the left for context.
    stub = 0.12 * geom["L_grain"]
    case_stub = [
        (-stub, geom["r_grain"]),
        (-stub, geom["r_case"]),
        (0.0, geom["r_case"]),
        (0.0, geom["r_grain"]),
        (0.0, -geom["r_grain"]),
        (0.0, -geom["r_case"]),
        (-stub, -geom["r_case"]),
        (-stub, -geom["r_grain"]),
    ]
    grain_stub = [
        (-stub, geom["r_port"]),
        (-stub, geom["r_grain"]),
        (0.0, geom["r_grain"]),
        (0.0, geom["r_port"]),
        (0.0, -geom["r_port"]),
        (0.0, -geom["r_grain"]),
        (-stub, -geom["r_grain"]),
        (-stub, -geom["r_port"]),
    ]
    _poly(ax, case_stub, **_CASE_HATCH)
    _poly(ax, grain_stub, **_GRAIN_HATCH)

    x_t = geom["L_conv"]
    x_e = geom["L_conv"] + geom["L_div"]
    pad = max(geom["r_case"] * 0.2, 10.0)

    _centerline(ax, -stub - pad * 0.2, x_e + pad * 0.3)

    # Gas-path guide (inner contour).
    ax.plot(
        [0.0, x_t, x_e],
        [geom["r_c"], geom["r_t"], geom["r_e"]],
        color=_EDGE,
        lw=1.1,
    )
    ax.plot(
        [0.0, x_t, x_e],
        [-geom["r_c"], -geom["r_t"], -geom["r_e"]],
        color=_EDGE,
        lw=1.1,
    )

    _dim_diameter(
        ax,
        x_t,
        geom["r_t"],
        f"Ø{geom['Dt']:.2f}",
        side="left",
        span=pad * 0.7,
    )
    _dim_diameter(
        ax,
        x_e,
        geom["r_e"],
        f"Ø{geom['De']:.2f}",
        side="right",
        span=pad * 0.65,
    )
    _dim_diameter(
        ax,
        -stub * 0.35,
        geom["r_c"],
        f"Ø{geom['grain_od']:.1f}",
        side="left",
        span=pad * 0.55,
        fontsize=7.5,
    )

    ax.text(
        0.5 * x_e,
        -max(geom["r_case"], geom["r_e"] + geom["wall"]) - pad * 0.5,
        "DETAIL B  —  NOZZLE",
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold",
        color=_EDGE,
    )
    ax.text(
        0.02,
        0.02,
        f"ε = Aₑ/Aₜ = {geom['expansion_ratio']:.3f}\n"
        f"contour: {_CONV_HALF_DEG:.0f}° / {_DIV_HALF_DEG:.0f}° half-angles (schematic)",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=7.5,
        color="#555555",
    )
    ax.text(
        0.98,
        0.98,
        "mm",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8,
        color="#555555",
    )

    r_max = max(geom["r_case"], geom["r_e"] + geom["wall"])
    ax.set_xlim(-stub - pad * 1.2, x_e + pad * 1.5)
    ax.set_ylim(-r_max - pad * 1.2, r_max + pad * 1.1)


def make_motor_drawing(
    inp: MotorInputs,
    result: MotorResult,
    out_dir: Path | None,
    show: bool,
) -> None:
    """
    Draw SECTION A-A (full motor) and DETAIL B (nozzle) in SolidWorks section style.

    If out_dir is set, saves motor_section.png.
    If show is True, leave the figure open for a later plt.show() (so it can
    appear alongside the burn-history window). If show is False, close after save.
    """
    geom = _build_motor_polygons(inp, result)

    fig, axes = plt.subplots(2, 1, figsize=(11, 8.5), facecolor=_BG)
    fig.suptitle(
        "Hybrid Motor — Longitudinal Cross-Section",
        fontsize=13,
        fontweight="bold",
        y=0.98,
    )

    _style_axes(axes[0], "SECTION A-A  —  MOTOR ASSEMBLY")
    _draw_full_motor(axes[0], geom)

    _style_axes(axes[1], "DETAIL B  —  NOZZLE")
    _draw_nozzle_detail(axes[1], geom)

    fig.tight_layout(rect=(0, 0, 1, 0.96))

    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)
        fig_path = out_dir / "motor_section.png"
        fig.savefig(fig_path, dpi=160, facecolor=fig.get_facecolor())
        print(f"Wrote {fig_path}")

    if not show:
        plt.close(fig)
