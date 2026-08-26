#!/usr/bin/env python3
"""Mesh organelle classes from CellMap 'all' painted labels -> colored glb scenes."""
import sys
import numpy as np
import trimesh
from scipy import ndimage
from skimage.measure import marching_cubes
import fast_simplification

# class groups: name -> (label ids, hex color)
GROUPS = {
    "nucleus":     ([20, 21, 22, 23, 24, 25, 26, 27, 28, 29], "#2f5fc4"),
    "mitochondria":([3, 4, 5],   "#1f9440"),
    "er":          ([16, 17, 18, 19], "#d9a613"),
    "golgi":       ([6, 7],      "#bb3ec7"),
    "lysosome":    ([12, 13],    "#e0641f"),
    "endosome":    ([10, 11],    "#6a3fd4"),
    "vesicle":     ([8, 9],      "#d4568f"),
    "peroxisome":  ([47, 48],    "#0da8a2"),
    "plasma_membrane": ([2],     "#9aa7b8"),
}

def hex2rgba(h, a=255):
    h = h.lstrip("#")
    return [int(h[i:i+2], 16) for i in (0, 2, 4)] + [a]

def mesh_group(mask, voxel_nm, target_faces):
    if mask.sum() < 500:
        return None
    m = ndimage.gaussian_filter(mask.astype(np.float32), 1.2)
    try:
        v, f, _, _ = marching_cubes(m, 0.5, spacing=(voxel_nm,)*3)
    except Exception:
        return None
    if len(f) > target_faces:
        v, f = fast_simplification.simplify(v.astype(np.float32), f.astype(np.int64),
                                            target_reduction=1 - target_faces/len(f))
    return trimesh.Trimesh(vertices=v, faces=f, process=False)

def build(name, npy, voxel_nm=4.0, downsample=1, budget=420_000, exclude=()):
    arr = np.load(npy)
    if downsample > 1:
        arr = arr[::downsample, ::downsample, ::downsample]
        voxel_nm *= downsample
    scene = trimesh.Scene()
    present = set(np.unique(arr).tolist())
    total_vox = {g: int(np.isin(arr, ids).sum()) for g, (ids, _) in GROUPS.items()}
    active = [g for g in GROUPS if g not in exclude and total_vox[g] > 500
              and any(i in present for i in GROUPS[g][0])]
    vox_sum = sum(total_vox[g] for g in active)
    for g in active:
        ids, color = GROUPS[g]
        mask = np.isin(arr, ids)
        tf = max(20_000, int(budget * total_vox[g] / vox_sum))
        mesh = mesh_group(mask, voxel_nm, tf)
        if mesh is None:
            continue
        rgba = hex2rgba(color, 110 if g == "plasma_membrane" else 255)
        mat = trimesh.visual.material.PBRMaterial(
            baseColorFactor=[c/255 for c in rgba],
            metallicFactor=0.0, roughnessFactor=0.85,
            alphaMode="BLEND" if g == "plasma_membrane" else "OPAQUE",
            doubleSided=True)
        mesh.visual = trimesh.visual.TextureVisuals(material=mat)
        scene.add_geometry(mesh, node_name=g, geom_name=g)
        print(f"  {g}: {total_vox[g]} vox -> {len(mesh.faces)} faces")
    out = f"/home/claude/showcase-repo/assets/glb/{name}.glb"
    scene.export(out)
    import os
    print(name, "->", os.path.getsize(out)/1e6, "MB")

if __name__ == "__main__":
    build("liver_cell_organelles", "crop145_all.npy", downsample=2, budget=600_000)
    build("liver_organelles_golgi", "crop143_all.npy", downsample=1, budget=400_000)
