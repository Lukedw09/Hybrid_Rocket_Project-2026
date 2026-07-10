"""
Rudimentary 3D rocket mesh for the animation.

================================================================================
WHAT THIS MODULE DOES
================================================================================
Builds a simple visual model (cylinder body + cone nose + four fins) and
places it in the world frame at the rocket's current position and attitude.

This module is *display only* — it does not affect the flight physics.
dynamics.py / simulate.py never import it.

================================================================================
BODY FRAME
================================================================================
Local construction uses +y toward the nose (same convention as the dynamics
body axis). Origin is at mid-body (visual stand-in for CG).

build_rocket_mesh(...) then:
  1. Builds polygons in that body frame.
  2. Builds a 3×3 rotation from Euler angles (same tip law as dynamics).
  3. Transforms every vertex:  p_world = R @ p_body + position

animate.py maps world (x, y_up, z) into matplotlib's plot axes afterward.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from dynamics import body_axis


@dataclass
class RocketMesh:
    """
    Collections of 3D polygons in the *world* frame.

    Each polygon is an (M, 3) array of vertices (quads for body/fins,
    triangles for the nose). all_polys() concatenates them for convenience.
    """

    body_polys: list[np.ndarray]
    nose_polys: list[np.ndarray]
    fin_polys: list[np.ndarray]

    def all_polys(self) -> list[np.ndarray]:
        return self.body_polys + self.nose_polys + self.fin_polys


def _rotation_body_to_world(phi: float, theta: float, psi: float) -> np.ndarray:
    """
    3×3 matrix mapping body-frame vectors to world.

    Columns are the world-frame images of the body unit axes (e_x, e_y, e_z).
    Body +y (column 1) is the longitudinal / +nose axis from body_axis().

    We build a right-handed triad around that axis, then optionally roll by φ
    about body y (φ is normally 0 in this sim).
    """
    ey = body_axis(phi, theta, psi)

    # Pick a reference that is not nearly parallel to ey, then Gram-Schmidt
    world_ref = np.array([0.0, 0.0, 1.0])
    if abs(float(np.dot(ey, world_ref))) > 0.95:
        world_ref = np.array([1.0, 0.0, 0.0])
    ex = np.cross(world_ref, ey)
    ex /= np.linalg.norm(ex)
    ez = np.cross(ex, ey)
    ez /= np.linalg.norm(ez)

    # Roll about body +y
    c, s = np.cos(phi), np.sin(phi)
    ex_r = c * ex + s * ez
    ez_r = -s * ex + c * ez
    return np.column_stack([ex_r, ey, ez_r])


def _transform(points_body: np.ndarray, R: np.ndarray, origin: np.ndarray) -> np.ndarray:
    """Map (N, 3) body-frame points to world: P @ R.T + origin."""
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
        # One rectangular facet of the cylinder wall
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
    Simple trapezoidal fins as single quads extending radially from the body.

    Enough detail to read as a rocket in the nose-camera view; not a CFD mesh.
    """
    polys: list[np.ndarray] = []
    for k in range(n_fins):
        ang = 2.0 * np.pi * k / n_fins
        radial = np.array([np.cos(ang), 0.0, np.sin(ang)])
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

    Parameters
    ----------
    diameter_m, length_m :
        Outer body diameter and tip-to-aft length (from the GUI / SimInputs).
    position_m :
        World (x, y, z) of the visual CG (mid-body).
    attitude_rad :
        (phi, theta, psi) matching dynamics.attitude_angles.
    """
    radius = 0.5 * diameter_m
    nose_len = max(nose_fraction * length_m, 1.5 * radius)
    body_len = max(length_m - nose_len, 2.0 * radius)

    # Mid-body at local origin: aft below, nose base above, tip further +y
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
