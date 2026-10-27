# Stack

Portfolio personal estático de una sola página. Sin build, sin framework, sin dependencias npm.

## Front-end

| Pieza | Uso | Evidencia |
|---|---|---|
| HTML5 | Una página (`index.html`, `lang="es"`) con secciones ancladas | `index.html` |
| CSS3 puro | Variables en `:root`, Flexbox/Grid, `@keyframes`, 2 media queries a 768px | `style.css` |
| JavaScript vanilla | Menú móvil, animaciones al hacer scroll (IntersectionObserver), fondo del nav al hacer scroll | `script.js` |

## Recursos externos (CDN)

- **Google Fonts**: `Sixtyfour` (fuente principal, retro) y `Roboto` (textos de lectura). Se cargan dos `<link>` duplicados; el segundo ya incluye las dos familias.
- **Font Awesome 6.4.0** desde cdnjs: todos los iconos.
- **Google Drive**: enlace al CV descargable.
- **YouTube / GitHub**: demo y código de los proyectos.

## Despliegue

- **Producción: Vercel**, en https://portofolio-vert-mu.vercel.app.
- Vercel publica solo en cada push a `main` en GitHub (`SubielaDev/Portofolio`). Un push a `main` cambia la web en vivo.
- El enlace de la ficha "About" del repo en GitHub (`portofolio-khaki-rho.vercel.app`) está caducado.
- `dockerfile`: imagen `nginx:alpine`, copia todo el repo a `/usr/share/nginx/html`, expone el puerto 80. No es la vía de producción.
- No hay `.dockerignore`: la imagen incluye también `.git`, `02-DOCS`, `01-TOOLS`, `.claude`, etc.
- No hay CI, tests ni linter configurados.

## Requisitos de compatibilidad

- Tiene que verse bien en **móvil y ordenador**.
- Navegadores obligatorios: **Chrome, Safari y Edge**.
