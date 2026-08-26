# Alpha Cell — data showcase

![From raw electron microscopy to labeled voxels, organelle meshes, measured membranes, and whole tissue](assets/img/readme_hero.jpg)

A visual showcase of what modern volume electron microscopy data is and what it
makes possible, built for Alpha Cell presentations and discussions. Everything
on the page is real segmented data from the Janelia CellMap / OpenOrganelle
collection — nothing is an illustration.

## How to open it

**The showcase is a single web page: `index.html`.**

- **On the web (easiest)**: the page is live at the repo's GitHub Pages URL —
  nothing to download, everything works.
- **On your computer**: download or clone this repo, then **double-click
  `Open showcase.command`** — it starts a tiny local server and opens the page
  with everything working, fully offline. (Opening `index.html` directly also
  works for the movies, charts and images, but browsers refuse to load the
  interactive 3D models from a plain file — the page will tell you if that
  happens.)

## What's on the page

1. **Opener** — a two-minute FIB-SEM fly-through of a mosquito stylet, from raw
   EM to the fully segmented reconstruction.
2. **Scale** — one dataset spans six orders of magnitude, from whole tissue to
   the lipid bilayer, with links to fly through the public volumes in
   Neuroglancer.
3. **Resolution** — interactive 3D membrane models at 4–8 nm voxel size (drag,
   zoom, pan).
4. **Quantification** — surfaces colored by measurement (contact gap, curvature,
   protrusions) plus live charts from the analysis: ECS width, contact
   fractions, and an effect-size matrix comparing chemical vs rapid-cryo
   preservation.
5. **Liver zonation & beyond** — an entire acinus with every cell and organelle
   segmented, nuclear pore densities across the tissue, and plasmodesmata in
   plant tissue.
6. **Workflow** — from organ to numbers: tissue → preserve → FIB-SEM → segment
   → measure.
7. **More to explore** — turntable loops (good for slides), all 14 interactive
   models, and a stills gallery.

## Repo contents

| Path | Contents |
| :-- | :-- |
| `index.html` | The whole showcase — self-contained |
| `assets/glb/` | Vertex-colored membrane meshes |
| `assets/video/` | Fly-throughs and turntable loops |
| `assets/img/` | Posters and rendered stills |
| `vendor/` | `<model-viewer>` library (bundled, no CDN) |
| `pipeline/render_meshes.py` | Mesh render pipeline (trimesh + PyVista) |

## Provenance

Meshes and charts come from CellMap ground-truth segmentations of public mouse
datasets (liver, kidney, heart, cortex — chemical vs rapid-cryo preservation),
all browsable on [OpenOrganelle](https://openorganelle.janelia.org). The organelle scenes come from the public [CellMap Segmentation Challenge](https://cellmapchallenge.janelia.org) training data. The
membrane analyses, the stylet reconstruction, and the zonation work are from
manuscripts in preparation — please don't redistribute outside the group for
now. The raw datasets are fully public.
