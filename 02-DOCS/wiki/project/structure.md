# Estructura

## Ficheros

```text
/
├── index.html      # Toda la página (316 líneas)
├── style.css       # Todos los estilos (≈700 líneas)
├── script.js       # Toda la interactividad (49 líneas)
├── dockerfile      # Servir con nginx
├── README.md       # Presentación del repo (en español)
├── assets/         # profile.jpg, logo-navbar.avif, portfolio.gif, og-image.jpg
├── 01-TOOLS/       # Harness rsc: conectores a herramientas; og-image/generar.py crea og-image.jpg
└── 02-DOCS/        # Harness rsc: wiki del proyecto
```

`portfolio.gif` solo lo usa el README. `.gradiente-3` y `.retraso-200` ya no los usa ninguna tarjeta; quedan en `style.css` para una tercera tarjeta futura.

## Secciones de la página (en orden)

| Ancla | Contenido |
|---|---|
| `aside.barra-social` | Barra lateral fija: GitHub, LinkedIn, email, y atajos a `#sobre-mi` y `#habilidades` |
| `nav.barra-navegacion` | Logo "Portfolio" + un único enlace a `#proyectos` + botón hamburguesa (`.alternar-menu`) |
| `#inicio` (hero) | "Ventana de terminal" con saludo, título, cita y foto; botones "Ver Proyectos" y "Descargar CV" |
| `#sobre-mi` | Texto de trayectoria + estadísticas (+1 año, +3 proyectos) |
| `#habilidades` | Slider infinito de tecnologías (8 items duplicados a mano para el bucle) |
| `#proyectos` | Grid de tarjetas: "Agenda Clínica Online" y "Scraper BOE" |
| `footer` | Copyright 2025 |

## Estado de las tarjetas de proyecto

- **Agenda Clínica Online** (antes "Dashboard Personal", renombrada el 2026-10-28): agenda online para clínicas. El código está en carpetas locales y aún no está subido; por eso los enlaces son `#`. Ya no muestra el aviso "en construcción".
- **Scraper BOE**: publicado, con código en GitHub y demo en YouTube.
- **Task Manager App**: el proyecto no existe. La tarjeta comentada se borró del código el 2026-10-28.

## Cómo añadir un proyecto

Copiar un `<article class="tarjeta-proyecto oculto retraso-N">` dentro de `.grid-proyectos`. Partes: `.imagen-proyecto` (gradiente `gradiente-1..3` o logo), `.info-proyecto` con `h3`, `p`, `.etiquetas` y `.enlaces-proyecto` (Código + Demo).

## Cómo añadir una tecnología al slider

Añadir el `.slide` dos veces: una en el bloque "Originales" y otra en "Duplicados". Si no, el bucle infinito salta.

## Observaciones del código

- `#habilidades` está dentro de `#sobre-mi` y hay un `</div>` de más justo antes de `</section>` (línea 243).
- `body.tema-oscuro` no tiene reglas en `style.css`: es la única paleta.
- El README menciona un "efecto de escritura" en el hero; existe en CSS (`@keyframes typing` sobre `.texto2-terminal`).
