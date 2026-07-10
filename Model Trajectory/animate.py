"""
Looping 3D trajectory animation with boost/coast path, apogee marker, HUD,
and three camera modes.

Plot mapping: world (x, y_up, z) → matplotlib (x, z, y_up) so the xz plane is
the ground under view_init, and altitude is the vertical axis.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal

import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 — registers 3d projection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from dynamics import body_axis
from geometry import build_rocket_mesh
from simulate import TrajectoryResult

CameraMode = Literal["orbit", "follow", "nose"]

CAMERA_LABELS = {
    "orbit": "(a) Orbit trajectory",
    "follow": "(b) Follow rocket",
    "nose": "(c) Nose camera",
}

# Visual length of ground axes (plot x & y = world x & z) relative to altitude
# (plot z). Applied via set_box_aspect only — data limits stay tight so the
# camera does not pull back from the trajectory.
_HORIZ_VISUAL_SCALE = 1.22


@dataclass
class AnimationHandles:
    """Live artists updated each frame."""

    anim: FuncAnimation
    ax: Axes
    hud: object  # matplotlib text
    live_hud: object
    set_camera_mode: Callable[[CameraMode], None]


def _world_to_plot(xyz: np.ndarray) -> np.ndarray:
    """
    Map world (x, y_up, z) → plot (x, z, y_up).

    Matplotlib treats plot-XY as the ground plane and plot-Z as up, so this
    makes the physical xz plane the ground relative to the camera.
    """
    xyz = np.asarray(xyz, dtype=float)
    if xyz.ndim == 1:
        return np.array([xyz[0], xyz[2], xyz[1]], dtype=float)
    return np.column_stack([xyz[:, 0], xyz[:, 2], xyz[:, 1]])


def _polys_to_plot(polys: list[np.ndarray]) -> list[np.ndarray]:
    return [_world_to_plot(p) for p in polys]


def _path_segments(result: TrajectoryResult) -> tuple[np.ndarray, np.ndarray]:
    """
    Split trajectory into boost (red) and coast (green) polylines (world frame).

    Returns (boost_xyz (N,3), coast_xyz (M,3)). Coast starts at the last
    boost sample so the path is continuous.
    """
    pos = result.position_m
    thrusting = result.thrusting
    if len(pos) == 0:
        empty = np.zeros((0, 3))
        return empty, empty

    if not np.any(thrusting):
        return np.zeros((0, 3)), pos.copy()

    last_boost = int(np.where(thrusting)[0][-1])
    boost = pos[: last_boost + 1]
    coast = pos[last_boost:]
    return boost, coast


def _hud_static_text(result: TrajectoryResult) -> str:
    """Top-left HUD: inputs summary + goals vs achieved."""
    v = result.vehicle
    lines = [
        "Rocket Trajectory Analysis",
        "Frame: y up · xz ground · launch at origin",
        f"D={v.diameter_m * 1e3:.0f} mm  L={v.length_m * 1e3:.0f} mm",
        f"m_dry={v.mass_dry_kg:.2f} kg  m_prop0={v.mass_propellant_kg:.2f} kg",
        f"Cd={v.cd:.2f}",
        f"Max alt={result.max_altitude_m:.1f} m  (goal {result.altitude_goal_m:.1f} m)",
        f"Max Mach={result.max_mach:.3f}  (goal {result.mach_goal:.3f})",
        f"Boost time={result.boost_time_s:.2f} s  Impact={result.impact_time_s:.1f} s",
    ]
    return "\n".join(lines)


def _axis_limits_plot(
    result: TrajectoryResult,
    pad_frac: float = 0.55,
) -> tuple[list[float], list[float], list[float]]:
    """
    Tight plot-axis limits (x, world-z, altitude) framed on the trajectory.

    Horizontal limits follow path extent only (not altitude), so expanding the
    visual x/z axes via box_aspect does not zoom the camera out.
    """
    pos = result.position_m
    x = pos[:, 0]
    y = pos[:, 1]  # altitude
    z = pos[:, 2]

    x_c = 0.5 * (float(x.min()) + float(x.max()))
    y_c = 0.5 * (float(y.min()) + float(y.max()))
    z_c = 0.5 * (float(z.min()) + float(z.max()))

    x_half = 0.5 * max(float(x.max() - x.min()), 1.0) * (1.0 + pad_frac)
    y_half = 0.5 * max(float(y.max() - y.min()), 1.0) * (1.0 + pad_frac)
    z_half = 0.5 * max(float(z.max() - z.min()), 1.0) * (1.0 + pad_frac)
    # Square ground footprint large enough for both horizontal drifts
    horiz_half = max(x_half, z_half, 1.0)

    xlim = [x_c - horiz_half, x_c + horiz_half]
    ylim = [z_c - horiz_half, z_c + horiz_half]
    zlim = [min(0.0, y_c - y_half), y_c + y_half]
    return xlim, ylim, zlim


def _apply_box_aspect(ax: Axes, xlim: list[float], ylim: list[float], zlim: list[float]) -> None:
    """
    Stretch ground axes visually without changing data limits / camera distance.

    box_aspect sets on-screen axis lengths; limits alone control framing zoom.
    """
    # Normalize by altitude span so aspect is stable, then stretch x/z visually
    sz = max(zlim[1] - zlim[0], 1e-6)
    sx = _HORIZ_VISUAL_SCALE * sz
    sy = _HORIZ_VISUAL_SCALE * sz
    _ = xlim, ylim  # framing only; visual scale is independent of horiz limits
    try:
        ax.set_box_aspect((sx, sy, sz))
    except AttributeError:
        pass


def _clear_rocket_artists(artists: list) -> None:
    for a in artists:
        try:
            a.remove()
        except Exception:  # noqa: BLE001
            pass
    artists.clear()


def _draw_rocket_mesh(ax: Axes, result: TrajectoryResult, index: int, artists: list) -> None:
    """Draw full rocket mesh in plot frame (nose-camera scale only)."""
    mesh = build_rocket_mesh(
        result.vehicle.diameter_m,
        result.vehicle.length_m,
        result.position_m[index],
        result.attitude_rad[index],
    )
    body = Poly3DCollection(
        _polys_to_plot(mesh.body_polys),
        alpha=0.92,
        facecolor="#c0c4c8",
        edgecolor="#333333",
        linewidths=0.3,
    )
    nose = Poly3DCollection(
        _polys_to_plot(mesh.nose_polys),
        alpha=0.95,
        facecolor="#e8eaed",
        edgecolor="#333333",
        linewidths=0.3,
    )
    fins = Poly3DCollection(
        _polys_to_plot(mesh.fin_polys),
        alpha=0.9,
        facecolor="#6b7280",
        edgecolor="#222222",
        linewidths=0.4,
    )
    ax.add_collection3d(body)
    ax.add_collection3d(nose)
    ax.add_collection3d(fins)
    artists.extend([body, nose, fins])


def _draw_rocket_dot(ax: Axes, result: TrajectoryResult, index: int, artists: list) -> None:
    """Black marker for orbit/follow — mesh is invisible at trajectory scale."""
    p = _world_to_plot(result.position_m[index])
    (dot,) = ax.plot(
        [p[0]],
        [p[1]],
        [p[2]],
        marker="o",
        markersize=7,
        color="black",
        markeredgecolor="white",
        markeredgewidth=0.6,
        linestyle="none",
        zorder=10,
    )
    artists.append(dot)


def _set_nose_camera(ax: Axes, result: TrajectoryResult, index: int) -> None:
    """Place camera at rocket CG looking along body +nose (plot frame)."""
    pos_w = result.position_m[index]
    att = result.attitude_rad[index]
    axis_w = body_axis(float(att[0]), float(att[1]), float(att[2]))
    pos = _world_to_plot(pos_w)
    axis = _world_to_plot(axis_w)

    look_dist = max(2.0 * result.vehicle.length_m, 1.0)
    half = 0.45 * look_dist
    focus = pos + axis * (0.55 * look_dist)
    ax.set_xlim(focus[0] - half, focus[0] + half)
    ax.set_ylim(focus[1] - half, focus[1] + half)
    ax.set_zlim(focus[2] - half, focus[2] + half)
    _apply_box_aspect(
        ax,
        [focus[0] - half, focus[0] + half],
        [focus[1] - half, focus[1] + half],
        [focus[2] - half, focus[2] + half],
    )

    # plot-Z is up; elev from ground (plot XY = world xz), azim in that plane
    vx, vy, vz = axis  # plot components
    elev = float(np.degrees(np.arctan2(vz, np.hypot(vx, vy))))
    azim = float(np.degrees(np.arctan2(vy, vx)))
    ax.view_init(elev=elev, azim=azim)


def attach_animation(
    fig: Figure,
    ax: Axes,
    result: TrajectoryResult,
    *,
    camera_mode: CameraMode = "orbit",
    interval_ms: int = 30,
    frame_stride: int = 2,
) -> AnimationHandles:
    """
    Draw static path + apogee, then start a looping FuncAnimation on `ax`.

    Camera modes:
      (a) orbit  — fixed framing of full trajectory; continuous azimuth orbit
      (b) follow — limits centered on rocket; continuous azimuth orbit
      (c) nose   — camera at CG looking along +nose (mesh); others use a black dot

    Plot axes: X=world x, Y=world z, Z=world y (up). Ground plane = xz.
    """
    boost, coast = _path_segments(result)
    xlim0, ylim0, zlim0 = _axis_limits_plot(result)

    if len(boost) > 1:
        bp = _world_to_plot(boost)
        ax.plot(bp[:, 0], bp[:, 1], bp[:, 2], color="red", lw=1.8, label="Boost")
    if len(coast) > 1:
        cp = _world_to_plot(coast)
        ax.plot(cp[:, 0], cp[:, 1], cp[:, 2], color="green", lw=1.8, label="Coast")

    apo = _world_to_plot(result.apogee_position_m)
    ax.scatter(
        [apo[0]],
        [apo[1]],
        [apo[2]],
        color="#f5c542",
        s=60,
        depthshade=True,
        label="Apogee",
        zorder=5,
    )

    ax.set_xlabel("x [m]")
    ax.set_ylabel("z [m]")
    ax.set_zlabel("y [m] (up)")
    ax.set_xlim(*xlim0)
    ax.set_ylim(*ylim0)
    ax.set_zlim(*zlim0)
    _apply_box_aspect(ax, xlim0, ylim0, zlim0)

    hud = fig.text(
        0.02,
        0.98,
        _hud_static_text(result),
        transform=fig.transFigure,
        va="top",
        ha="left",
        family="monospace",
        fontsize=8,
        color="white",
        bbox={"boxstyle": "round,pad=0.4", "facecolor": "black", "alpha": 0.55, "edgecolor": "none"},
    )
    live_hud = fig.text(
        0.02,
        0.72,
        "",
        transform=fig.transFigure,
        va="top",
        ha="left",
        family="monospace",
        fontsize=8,
        color="white",
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "black", "alpha": 0.55, "edgecolor": "none"},
    )

    n = len(result.time_s)
    indices = list(range(0, n, max(frame_stride, 1)))
    if indices[-1] != n - 1:
        indices.append(n - 1)

    rocket_artists: list = []
    mode_holder: dict[str, CameraMode] = {"mode": camera_mode}
    tick = {"i": 0}
    azim0 = -60.0
    deg_per_frame = 360.0 / max(int(12.0 * 1000.0 / max(interval_ms, 1)), 1)

    def set_camera_mode(mode: CameraMode) -> None:
        mode_holder["mode"] = mode

    def update(frame_i: int):
        idx = indices[frame_i % len(indices)]
        mode = mode_holder["mode"]

        _clear_rocket_artists(rocket_artists)
        if mode == "nose":
            _draw_rocket_mesh(ax, result, idx, rocket_artists)
        else:
            _draw_rocket_dot(ax, result, idx, rocket_artists)

        t = float(result.time_s[idx])
        alt = float(result.altitude_m[idx])
        mach = float(result.mach[idx])
        phase = "BOOST" if result.thrusting[idx] else "COAST"
        live_hud.set_text(f"t={t:6.2f} s  [{phase}]\nalt={alt:8.1f} m\nMach={mach:6.3f}")

        azim = azim0 + deg_per_frame * tick["i"]
        tick["i"] += 1

        if mode == "orbit":
            ax.set_xlim(*xlim0)
            ax.set_ylim(*ylim0)
            ax.set_zlim(*zlim0)
            _apply_box_aspect(ax, xlim0, ylim0, zlim0)
            # elev above xz ground plane
            ax.view_init(elev=22.0, azim=azim)
        elif mode == "follow":
            p = _world_to_plot(result.position_m[idx])
            half_alt = max(0.28 * (zlim0[1] - zlim0[0]), 8.0 * result.vehicle.length_m, 120.0)
            # Keep follow framing tight (same zoom); visual x/z stretch is box_aspect only
            half_horiz = max(
                0.28 * (xlim0[1] - xlim0[0]),
                8.0 * result.vehicle.length_m,
                25.0,
            )
            xlim = [p[0] - half_horiz, p[0] + half_horiz]
            ylim = [p[1] - half_horiz, p[1] + half_horiz]
            zlim = [p[2] - half_alt, p[2] + half_alt]
            ax.set_xlim(*xlim)
            ax.set_ylim(*ylim)
            ax.set_zlim(*zlim)
            _apply_box_aspect(ax, xlim, ylim, zlim)
            ax.view_init(elev=22.0, azim=azim)
        else:  # nose
            _set_nose_camera(ax, result, idx)

        return rocket_artists + [live_hud]

    anim = FuncAnimation(
        fig,
        update,
        frames=len(indices),
        interval=interval_ms,
        blit=False,
        repeat=True,
    )

    update(0)
    return AnimationHandles(
        anim=anim,
        ax=ax,
        hud=hud,
        live_hud=live_hud,
        set_camera_mode=set_camera_mode,
    )


def run_standalone_preview(
    result: TrajectoryResult,
    *,
    camera_mode: CameraMode = "orbit",
) -> None:
    """Open a matplotlib window with a looping animation (for smoke tests)."""
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(10, 7), facecolor="#1a1a1a")
    ax = fig.add_subplot(111, projection="3d", facecolor="#1a1a1a")
    ax.tick_params(colors="#cccccc")
    ax.xaxis.label.set_color("#cccccc")
    ax.yaxis.label.set_color("#cccccc")
    ax.zaxis.label.set_color("#cccccc")
    handles = attach_animation(fig, ax, result, camera_mode=camera_mode)
    _ = handles
    plt.tight_layout()
    plt.show()
