# Alpha Cell — Into the cell

![From raw electron microscopy to labeled voxels, organelle meshes, measured membranes, and whole tissue](assets/img/readme_hero.jpg)

**Live page: [avweigel.github.io/alpha-cell-showcase](https://avweigel.github.io/alpha-cell-showcase/)**

A guided zoom from a whole organ down to the machinery inside a single cell,
built for Alpha Cell talks, outreach and discussions. Every 3D scene, movie and
number on the page comes from real segmented microscopy data. Where a cartoon
appears, it is labeled as a cartoon and sits next to the real data it stands for.

## How to open it

**The showcase is a single web page: `index.html`.**

- **On the web (easiest)**: open
  [avweigel.github.io/alpha-cell-showcase](https://avweigel.github.io/alpha-cell-showcase/).
  Nothing to download, and the interactive 3D models work.
- **On your computer**: download or clone this repo, then **double-click
  `Open showcase.command`**. It starts a tiny local server and opens the page
  with everything working, fully offline. (Opening `index.html` directly also
  works for the movies and images, but browsers refuse to load interactive 3D
  models from a plain file, and the page will say so if that happens.)

## The journey

A sticky scale ruler tracks how far in you are, and every chapter has a short
blurb plus an expandable "dig deeper" for anyone who wants more.

1. **The organ** — start with a liver: where the sample comes from and how small
   a piece we actually image.
2. **The tissue** — every cell in a liver acinus found and colored, rendered
   from the real segmentation (1,514 cells).
3. **One cell** — zoom into a single hepatocyte, with an interactive whole-cell
   model you can spin.
4. **The machines inside** — the cartoon cell you remember from school, with
   clickable organelles that swap in the real thing: nuclear pores,
   mitochondrial networks, ER, a hand-annotated Golgi stack.
5. **Now take it apart** — one scan, every piece: the liver block separates into
   its extractable structures (blood supply, bile canaliculi, 1,897 nuclei,
   1.3 million mitochondria, 49,801 lipid droplets, ~27,000 peroxisomes).
6. **Now add time** — living mouse embryos through their first divisions, the
   dimension Alpha Cell measures next alongside space (Ellenberg lab, EMBL).
7. **Now run it backwards** — how measurement, AI models, prediction and the
   next experiment form the loop that builds a virtual cell.

Plus **detours** along the way (mosquito, worm, plant tissue) showing the same
methods elsewhere in nature, and a closing **explore** section linking the public
data.

## Repo contents

| Path | Contents |
| :-- | :-- |
| `index.html` | The whole showcase, self-contained |
| `assets/glb/` | Interactive 3D models (whole cells, organelle scenes) |
| `assets/video/` | Rendered movies and fly-throughs |
| `assets/img/` | Posters, stills, and BioRender artwork |
| `vendor/` | `<model-viewer>` library (bundled, no CDN) |
| `pipeline/` | Mesh and movie render scripts (PyVista + trimesh) |
| `Open showcase.command` | Local launcher for offline viewing |

## Provenance

The liver tissue, cells and organelles are segmented from public Janelia CellMap
/ OpenOrganelle volumes, browsable at
[OpenOrganelle](https://openorganelle.janelia.org); organelle scenes come from
the public [CellMap Segmentation Challenge](https://cellmapchallenge.janelia.org)
training data. The embryo time-lapse movies are from the Ellenberg lab at EMBL,
recorded on an inverted light-sheet microscope. Cartoons were created in
BioRender.

The liver zonation work, the membrane analyses, the mosquito stylet
reconstruction and the nuclear pore survey are from **manuscripts in
preparation** — please don't redistribute those outside the group for now. The
underlying raw datasets are fully public.

Prepared by Aubrey Weigel, SciLifeLab / KTH — Alpha Cell.
