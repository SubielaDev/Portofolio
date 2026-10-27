---
author: A.S
branch: worktree-chore-remove-unused-assets
status: done
---

# Remove unused styles and images

## Intent
Delete CSS rules and image files that nothing in the site references, with no visual change.

## Scope
- `style.css`: rules for classes absent from `index.html` and `script.js`, plus the variables and keyframes only they used.
- `assets/`: images not referenced by `index.html` or `README.md`.
- Kept on purpose: `.gradiente-3` and `.retraso-200`, used by the commented-out "Task Manager App" card.

## Checklist
- [x] Unused CSS removed — proof: every class selector left in `style.css` appears in `index.html` or `script.js`.
- [x] CSS still well-formed — proof: brace count balanced.
- [x] No dangling variables or keyframes — proof: each `--var` and `@keyframes` left has at least one use.
- [x] Unused image removed — proof: `assets/scraper_boe.png` had no reference; remaining 3 images are all referenced.

## Evidence
- Removed classes: `branding`, `logo2`, `btn-primario`, `btn-bloque`, `visual-hero`, `contenedor-imagen`, `perfil-imagen`, `mancha`, `tarjeta-cristal`, `fragmento-codigo`, `icono-hero`, `grid-habilidades`, `tarjeta-habilidad`, `icono-habilidad` (+ variants), contact form block (`contenedor-contacto`, `subtitulo-contacto`, `formulario-contacto`, `grupo-formulario`, `enlaces-sociales`, `icono-social`), `anim-aparecer-arriba`, `anim-flotar`, `retraso-300`, `redes-hero`, `icono-mini`.
- Removed variables: `--acento-brillo`, `--fondo-cristal`. Removed keyframes: `aparecerArriba`, `flotar`.
- Braces: 117 open / 117 close.

## Next
Merge branch `worktree-chore-remove-unused-assets` into `main` locally. No push.
