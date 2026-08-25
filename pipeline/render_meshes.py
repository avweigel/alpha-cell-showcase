#!/usr/bin/env python3
"""Render staged membrane .glb meshes: face-on stills + turntable frames."""
import os, sys
import numpy as np
import trimesh
import pyvista as pv

pv.OFF_SCREEN = True
GLB_DIR = "/mnt/user-data/uploads/ecs-analysis/figures/membranes/glb"
OUT = "/home/claude/norrkoping/renders"
os.makedirs(OUT, exist_ok=True)

MESHES = [
    ("crop1072_curvature", "Liver bile canaliculus (cryo) — curvature"),
    ("crop1072_gap",       "Liver bile canaliculus (cryo) — contact gap"),
    ("crop1027_curvature", "Kidney glomerular — curvature"),
    ("crop1026_gap",       "Kidney glomerular — contact gap"),
    ("crop1151_curvature", "Heart intercalated disc — curvature"),
    ("crop1144_deviation", "Cortex — protrusions"),
]

def load(name):
    sc = trimesh.load(f"{GLB_DIR}/{name}.glb")
    g = list(sc.geometry.values())[0]
    faces = np.hstack([np.full((len(g.faces), 1), 3), g.faces]).ravel()
    mesh = pv.PolyData(np.asarray(g.vertices), faces)
    mesh["rgb"] = np.asarray(g.visual.vertex_colors)[:, :3]
    return mesh

def camera_for(mesh, azim_deg=0.0, elev_deg=18.0, side=+1, zoom=1.0):
    """Face-on camera via PCA: view along the smallest principal axis."""
    pts = mesh.points - mesh.center
    cov = np.cov(pts.T)
    evals, evecs = np.linalg.eigh(cov)
    normal = evecs[:, 0] * side          # smallest variance = patch normal
    long_axis = evecs[:, 2]              # largest variance = in-plane up
    # rotate the normal around long axis for turntables
    from scipy.spatial.transform import Rotation as R
    rot = R.from_rotvec(np.radians(azim_deg) * long_axis)
    view = rot.apply(normal)
    # small elevation tilt around the remaining axis
    third = np.cross(long_axis, view); third /= np.linalg.norm(third)
    rot2 = R.from_rotvec(np.radians(elev_deg) * third)
    view = rot2.apply(view)
    extent = np.linalg.norm(mesh.bounds[1::2] - np.asarray(mesh.bounds[0::2]))
    dist = extent * 1.1 / zoom
    pos = mesh.center + view * dist
    return pos, mesh.center, long_axis

def render(name, title, azim=0.0, side=+1, fname=None, size=(2000, 1400), zoom=1.0):
    mesh = load(name)
    p = pv.Plotter(off_screen=True, window_size=size, lighting="none")
    p.set_background("#0d1420")
    pos, focus, up = camera_for(mesh, azim_deg=azim, side=side, zoom=zoom)
    p.add_mesh(mesh, scalars="rgb", rgb=True, smooth_shading=True,
               specular=0.35, specular_power=20, diffuse=0.85, ambient=0.28)
    # three-point lighting relative to camera
    for ldir, inten in [((0.4, 0.4, 1.0), 1.0), ((-0.7, -0.2, 0.6), 0.5), ((0.1, -0.8, 0.4), 0.35)]:
        light = pv.Light(light_type="camera light", intensity=inten)
        light.position = ldir
        p.add_light(light)
    p.camera.position = tuple(pos)
    p.camera.focal_point = tuple(focus)
    p.camera.up = tuple(up)
    p.camera.zoom(zoom)
    out = f"{OUT}/{fname or name}.png"
    p.screenshot(out)
    p.close()
    return out

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "stills"
    if mode == "stills":
        for name, title in MESHES:
            for side in (+1, -1):
                out = render(name, title, side=side,
                             fname=f"{name}_side{'A' if side>0 else 'B'}")
                print(out)
    elif mode == "turntable":
        name = sys.argv[2]
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 48
        side = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        for i in range(n):
            az = 360.0 * i / n
            render(name, "", azim=az, side=side, fname=f"tt_{name}_{i:03d}",
                   size=(1280, 900), zoom=1.15)
        print(f"{n} frames for {name}")
