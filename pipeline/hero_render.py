#!/usr/bin/env python3
"""High-quality banner renders of organelle glb scenes with dramatic lighting."""
import sys
import numpy as np
import trimesh
import pyvista as pv

pv.OFF_SCREEN = True

COLORS = {
    "nucleus": "#3565cf", "mitochondria": "#1fa348", "er": "#e3ae10",
    "golgi": "#c439d1", "lysosome": "#ef6a1e", "endosome": "#7a4ce0",
    "vesicle": "#e0559a", "peroxisome": "#0bbcb4", "plasma_membrane": "#8fa2bd",
    "microtubule": "#e83a55", "nuclear_pore": "#8fd6ff",
}

def render(glb, out, azim=30, elev=18, zoom=1.6, size=(3600, 1200), skip=("plasma_membrane",)):
    sc = trimesh.load(f"/home/claude/showcase-repo/assets/glb/{glb}.glb")
    p = pv.Plotter(off_screen=True, window_size=size, lighting="none")
    p.set_background("#0d1420")
    for name, g in sc.geometry.items():
        base = name.split("_geometry")[0]
        key = next((k for k in COLORS if base.startswith(k)), None)
        if key is None or key in skip:
            continue
        faces = np.hstack([np.full((len(g.faces), 1), 3), g.faces]).ravel()
        mesh = pv.PolyData(np.asarray(g.vertices), faces)
        p.add_mesh(mesh, color=COLORS[key], smooth_shading=True,
                   specular=0.5, specular_power=28, diffuse=0.9, ambient=0.16)
    # key + fill + rim
    for ldir, inten, color in [((0.5, 0.6, 1.0), 1.15, "white"),
                               ((-0.8, -0.3, 0.5), 0.45, "#bcd4ff"),
                               ((0.2, -0.9, -0.6), 0.7, "#ffd9a0")]:
        light = pv.Light(light_type="camera light", intensity=inten, color=color)
        light.position = ldir
        p.add_light(light)
    p.camera_position = "iso"
    p.camera.azimuth = azim
    p.camera.elevation = elev
    p.camera.zoom(zoom)
    p.screenshot(out)
    p.close()
    print(out)

if __name__ == "__main__":
    render("macrophage_organelles", "/tmp/hero_mac_a.png", azim=25, elev=12, zoom=1.75)
    render("macrophage_organelles", "/tmp/hero_mac_b.png", azim=115, elev=22, zoom=1.75)
    render("hela_organelles", "/tmp/hero_hela_a.png", azim=25, elev=12, zoom=1.7)
    render("hela_organelles", "/tmp/hero_hela_b.png", azim=205, elev=8, zoom=1.7)
