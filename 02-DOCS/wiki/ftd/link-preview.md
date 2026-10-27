---
author: A.S
branch: main
status: done
---

# Link preview for Google and social sharing

## Intent
Show a clear description in Google results and a rich card with an image when the site link is shared on WhatsApp, LinkedIn or X.

## Scope
- `index.html` `<head>`: `description`, `author`, `canonical`, Open Graph (`og:*`) and Twitter Card tags, all with absolute URLs on `https://portofolio-vert-mu.vercel.app`.
- `assets/og-image.jpg`: 1200×630 card in the site palette (terminal window, name, role, profile photo).
- `01-TOOLS/og-image/generar.py`: regenerates the image (`python 01-TOOLS/og-image/generar.py`, needs Pillow). Edit texts there if the role or stack changes.

## Checklist
- [x] Meta tags present — proof: HTML parser finds `description` (131 chars), `og:title` (42), `og:description` (100), `og:image`, `og:url`, `twitter:card`, `canonical`.
- [x] Image fits every platform — proof: Pillow reads 1200×630 JPEG, 66 KB (WhatsApp limit ≈300 KB).
- [x] Image is served — proof: local static server returns 200 `image/jpeg` for `/assets/og-image.jpg`.
- [x] Absolute URLs point at the live site — proof: `https://portofolio-vert-mu.vercel.app/` and `/assets/profile.jpg` return 200 in production, same folder layout.
- [ ] Real preview checked after deploy — needs a push (not done in this task).

## Evidence
- Docker check not run: `docker` is not on the PATH of the agent shell.
- `og-image.jpg` is not excluded by `.dockerignore`.

## Next
After the next deploy, paste the URL in LinkedIn Post Inspector (https://www.linkedin.com/post-inspector/) and the Facebook Sharing Debugger (also refreshes WhatsApp's cache). WhatsApp caches previews per link: an already-shared link may keep the old one for a while.
