# Estilo

## Idioma y nombres

- Todo en **español**: texto visible, clases CSS, variables CSS, variables JS y comentarios.
- **Regla para código nuevo**: nombres y comentarios en español, igual que el existente (confirmado por el autor).
- Clases en kebab-case descriptivo: `barra-navegacion`, `tarjeta-proyecto`, `contenido-terminal`.
- Variables JS en camelCase español: `alternarMenu`, `opcionesObservador`, `elementosOcultos`.
- Variables CSS: `--color-fondo`, `--acento-primario`, `--texto-secundario`, `--transicion`.
- Los comentarios de `:root` mezclan inglés (nombres de color: "Space Indigo", "Golden Pollen").

## Formato

- HTML con 2 espacios y atributos en varias líneas (formato tipo Prettier).
- CSS y JS con 4 espacios. JS con comillas simples y `;`.
- CSS organizado por bloques con cabecera `/* --- Sección --- */`.
- Comentarios cortos, uno por bloque lógico.

## Sistema visual

| Token | Valor | Papel |
|---|---|---|
| `--color-fondo` | `#1f2041` | Fondo índigo oscuro |
| `--color-fondo-secundario` | `#2c2d5e` | Tarjetas |
| `--texto-primario` | `#ffffff` | Texto |
| `--texto-secundario` | `#8faab5` | Texto apagado, enlaces |
| `--acento-primario` | `#ffc857` | Dorado |
| `--acento-secundario` | `#119da4` | Cian |

- Estética "terminal": ventanas con tres puntos (rojo/amarillo/verde), prefijo `>`, fuente `Sixtyfour`.
- `.acento`: texto con degradado dorado → cian. Se usa para resaltar una palabra del título.
- Efecto cristal: fondos semitransparentes + `backdrop-filter: blur`.
- Breakpoint único: `max-width: 768px`.

## Patrones de animación

- Aparición al hacer scroll: añadir `.oculto` (o `.anim-aparecer-arriba`); `script.js` pone `.mostrar` una vez.
- Escalonado: `.retraso-100`, `.retraso-200`, `.retraso-300`.
- `@keyframes` existentes: `parpadeo-cita`, `parpadeo-boton`, `aparecerArriba`, `flotar`, `typing`, `blink`, `scroll`.

## Inconsistencias conocidas

- `script.js` escribe colores del nav en línea (`rgba(31, 32, 65, …)`) en vez de usar variables.
- Hay un `style="margin: 0 auto"` en línea en `#sobre-mi`.
- Propiedades duplicadas en `style.css` (`width` en `.barra-navegacion`, `text-decoration` en `.logo`).
- Clases sin uso en el HTML: `.branding`, `.logo2`.
