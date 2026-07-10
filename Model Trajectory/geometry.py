"""
Rudimentary rocket mesh: cylinder body + conical nose + simple fins.

Mesh is built in a body frame with +y along the longitudinal (+nose) axis,
then transformed into world coordinates using position and Euler attitude.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from dynamics import body_axis


@dataclass
class RocketMesh:
    """Collections of 3D polygons (each an (M, 3) vertex array) in world frame."""

    body_polys: list[np.ndarray]
    nose_polys: list[np.ndarray]
    fin_polys: list[np.ndarray]

    def all_polys(self) -> list[np.ndarray]:
        return self.body_polys + self.nose_polys + self.fin_polys


def _rotation_body_to_world(phi: float, theta: float, psi: float) -> np.ndarray:
    """
    3×3 matrix mapping body-frame vectors to world.

    Body +y is the longitudinal (+nose) axis. Columns are world images of
    body unit axes (ex, ey, ez).
    """
    # Longitudinal (body +y) from attitude law
    ey = body_axis(phi, theta, psi)
    # Build a right-handed frame; prefer world +z as a reference for "up" of fins
    world_ref = np.array([0.0, 0.0, 1.0])
    if abs(float(np.dot(ey, world_ref))) > 0.95:
        world_ref = np.array([1.0, 0.0, 0.0])
    ex = np.cross(world_ref, ey)
    ex /= np.linalg.norm(ex)
    ez = np.cross(ex, ey)
    ez /= np.linalg.norm(ez)
    # Optional roll about body y
    c, s = np.cos(phi), np.sin(phi)
    ex_r = c * ex + s * ez
    ez_r = -s * ex + c * ez
    return np.column_stack([ex_r, ey, ez_r])


def _transform(points_body: np.ndarray, R: np.ndarray, origin: np.ndarray) -> np.ndarray:
    """Map (N, 3) body-frame points to world."""
    return points_body @ R.T + origin


def _cylinder_polys(
    radius: float,
    y0: float,
    y1: float,
    n_theta: int = 12,
) -> list[np.ndarray]:
    """Side quads of a cylinder along body +y from y0 to y1."""
    thetas = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
    polys: list[np.ndarray] = []
    for i, th0 in enumerate(thetas):
        th1 = thetas[(i + 1) % n_theta]
        c0, s0 = np.cos(th0), np.sin(th0)
        c1, s1 = np.cos(th1), np.sin(th1)
        polys.append(
            np.array(
                [
                    [radius * c0, y0, radius * s0],
                    [radius * c1, y0, radius * s1],
                    [radius * c1, y1, radius * s1],
                    [radius * c0, y1, radius * s0],
                ],
                dtype=float,
            )
        )
    return polys


def _cone_polys(
    radius: float,
    y_base: float,
    y_tip: float,
    n_theta: int = 12,
) -> list[np.ndarray]:
    """Triangular facets of a nose cone along body +y."""
    thetas = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
    tip = np.array([0.0, y_tip, 0.0])
    polys: list[np.ndarray] = []
    for i, th0 in enumerate(thetas):
        th1 = thetas[(i + 1) % n_theta]
        p0 = np.array([radius * np.cos(th0), y_base, radius * np.sin(th0)])
        p1 = np.array([radius * np.cos(th1), y_base, radius * np.sin(th1)])
        polys.append(np.vstack([p0, p1, tip]))
    return polys


def _fin_polys(
    radius: float,
    y_root_aft: float,
    y_root_fwd: float,
    span: float,
    sweep: float,
    n_fins: int = 4,
) -> list[np.ndarray]:
    """
    Simple trapezoidal fins in the body x–y / z–y planes.

    Each fin is a single quad extending radially from the body.
    """
    polys: list[np.ndarray] = []
    for k in range(n_fins):
        ang = 2.0 * np.pi * k / n_fins
        radial = np.array([np.cos(ang), 0.0, np.sin(ang)])
        # Root (on body) and tip (outboard); slight forward sweep at tip
        root_aft = np.array([radius * radial[0], y_root_aft, radius * radial[2]])
        root_fwd = np.array([radius * radial[0], y_root_fwd, radius * radial[2]])
        tip_aft = root_aft + span * radial + np.array([0.0, -sweep, 0.0])
        tip_fwd = root_fwd + span * radial
        polys.append(np.vstack([root_aft, root_fwd, tip_fwd, tip_aft]))
    return polys


def build_rocket_mesh(
    diameter_m: float,
    length_m: float,
    position_m: np.ndarray,
    attitude_rad: np.ndarray,
    *,
    nose_fraction: float = 0.18,
    fin_span_frac: float = 0.55,
) -> RocketMesh:
    """
    Build a world-frame rocket mesh at the given pose.

    Body frame: +y toward nose, origin at geometric mid-body (approx CG visual).
    length_m is overall tip-to-aft length; diameter_m is outer body diameter.
    """
    radius = 0.5 * diameter_m
    nose_len = max(nose_fraction * length_m, 1.5 * radius)
    body_len = max(length_m - nose_len, 2.0 * radius)

    # Place mid-body at origin: aft at -body_len/2, nose base at +body_len/2, tip beyond
    y_aft = -0.5 * body_len
    y_nose_base = 0.5 * body_len
    y_tip = y_nose_base + nose_len

    body_local = _cylinder_polys(radius, y_aft, y_nose_base)
    nose_local = _cone_polys(radius, y_nose_base, y_tip)
    fin_span = fin_span_frac * diameter_m
    fin_chord = 0.22 * body_len
    y_fin_fwd = y_aft + fin_chord
    fin_local = _fin_polys(
        radius,
        y_root_aft=y_aft,
        y_root_fwd=y_fin_fwd,
        span=fin_span,
        sweep=0.35 * fin_chord,
    )

    phi, theta, psi = (float(attitude_rad[0]), float(attitude_rad[1]), float(attitude_rad[2]))
    R = _rotation_body_to_world(phi, theta, psi)
    origin = np.asarray(position_m, dtype=float).reshape(3)

    return RocketMesh(
        body_polys=[_transform(p, R, origin) for p in body_local],
        nose_polys=[_transform(p, R, origin) for p in nose_local],
        fin_polys=[_transform(p, R, origin) for p in fin_local],
    )
