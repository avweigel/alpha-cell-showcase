# Alpha Cell — membrane landscapes

Visual showcase of cell-membrane surfaces reconstructed from isotropic FIB-SEM
volumes (Janelia CellMap / OpenOrganelle), prepared for Alpha Cell
presentations and discussions.

**Open `index.html`** — it works two ways:

- **Locally**: double-click `index.html`. Everything (viewer library, meshes,
  videos, images) is in the repo, so it works offline.
- **On the web**: enable GitHub Pages (Settings → Pages → Deploy from branch →
  `main`, root). The page is then shareable as a URL.

## What's inside

| Path | Contents |
| :-- | :-- |
| `index.html` | The showcase page: 14 interactive 3D meshes, 4 turntable videos, gallery stills, scale table, dataset links |
| `assets/glb/` | Vertex-colored membrane meshes (glb), ~36 MB total |
| `assets/video/` | Turntable MP4 loops (good for slides) |
| `assets/img/` | Rendered stills / posters |
| `vendor/` | `<model-viewer>` UMD build (no CDN needed) |
| `pipeline/render_meshes.py` | The render pipeline (trimesh + PyVista): PCA face-on camera, camera lighting, stills + turntable frames |

## Provenance

Meshes come from CellMap ground-truth segmentations of eight public mouse
datasets (liver, kidney, heart, cortex; chemical vs rapid-cryo preservation):
see the dataset cards at the bottom of the page, all on
[OpenOrganelle](https://openorganelle.janelia.org).

The surface analyses (curvature, contact gap, protrusions) are part of an
unpublished manuscript in preparation — please don't redistribute the rendered
surfaces outside the group for now.
