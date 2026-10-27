"""Genera assets/og-image.jpg (1200x630), la vista previa al compartir la web.

Uso: python 01-TOOLS/og-image/generar.py   (requiere Pillow)
Descarga las fuentes Sixtyfour y Roboto de google/fonts a una carpeta temporal.
"""
import tempfile
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'assets' / 'og-image.jpg'
FOTO = RAIZ / 'assets' / 'profile.jpg'

ANCHO, ALTO = 1200, 630

# Paleta de style.css (:root)
COLOR_FONDO = (31, 32, 65)
COLOR_FONDO_SECUNDARIO = (44, 45, 94)
TEXTO_PRIMARIO = (255, 255, 255)
TEXTO_SECUNDARIO = (143, 170, 181)
ACENTO_PRIMARIO = (255, 200, 87)
ACENTO_SECUNDARIO = (17, 157, 164)

FUENTES = {
    'Sixtyfour.ttf': 'https://github.com/google/fonts/raw/main/ofl/sixtyfour/Sixtyfour%5BBLED%2CSCAN%5D.ttf',
    'Roboto.ttf': 'https://github.com/google/fonts/raw/main/ofl/roboto/Roboto%5Bwdth%2Cwght%5D.ttf',
}


def obtener_fuente(nombre):
    ruta = Path(tempfile.gettempdir()) / 'og-image-fuentes' / nombre
    if not ruta.exists():
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_bytes(urllib.request.urlopen(FUENTES[nombre]).read())
    return ruta


def fuente(nombre, tamano, peso=None):
    f = ImageFont.truetype(str(obtener_fuente(nombre)), tamano)
    if peso:
        f.set_variation_by_axes([peso, 100])  # ejes de Roboto: peso, anchura
    return f


def texto_degradado(lienzo, posicion, texto, f):
    # Degradado dorado -> cian, como la clase .acento
    caja = f.getbbox(texto)
    ancho, alto = caja[2], caja[3]
    degradado = Image.new('RGB', (ancho, alto))
    for x in range(ancho):
        t = x / max(ancho - 1, 1)
        color = tuple(round(a + (b - a) * t) for a, b in zip(ACENTO_PRIMARIO, ACENTO_SECUNDARIO))
        ImageDraw.Draw(degradado).line([(x, 0), (x, alto)], fill=color)
    mascara = Image.new('L', (ancho, alto), 0)
    ImageDraw.Draw(mascara).text((0, 0), texto, font=f, fill=255)
    lienzo.paste(degradado, posicion, mascara)


def main():
    lienzo = Image.new('RGB', (ANCHO, ALTO), COLOR_FONDO)
    dibujo = ImageDraw.Draw(lienzo)

    # Ventana de terminal
    margen = 48
    ventana = (margen, margen, ANCHO - margen, ALTO - margen)
    dibujo.rounded_rectangle(ventana, radius=22, fill=COLOR_FONDO_SECUNDARIO, outline=(70, 72, 130), width=2)
    dibujo.line([(margen, margen + 56), (ANCHO - margen, margen + 56)], fill=(70, 72, 130), width=2)
    for i, color in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        cx, cy = margen + 36 + i * 30, margen + 28
        dibujo.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=color)

    # Foto de perfil en círculo con borde dorado
    diametro = 300
    foto = ImageOps.fit(Image.open(FOTO).convert('RGB'), (diametro, diametro), centering=(0.5, 0.3))
    mascara = Image.new('L', (diametro * 4, diametro * 4), 0)
    ImageDraw.Draw(mascara).ellipse((0, 0, diametro * 4, diametro * 4), fill=255)
    mascara = mascara.resize((diametro, diametro), Image.LANCZOS)
    fx, fy = ANCHO - margen - 60 - diametro, 172
    dibujo.ellipse((fx - 8, fy - 8, fx + diametro + 8, fy + diametro + 8), fill=ACENTO_PRIMARIO)
    lienzo.paste(foto, (fx, fy), mascara)

    # Textos
    x = margen + 56
    dibujo.text((x, 150), 'Hola, soy', font=fuente('Roboto.ttf', 34, 400), fill=TEXTO_SECUNDARIO)
    dibujo.text((x, 192), 'Alfonso Subiela', font=fuente('Roboto.ttf', 64, 700), fill=TEXTO_PRIMARIO)
    texto_degradado(lienzo, (x, 292), 'Desarrollador', fuente('Sixtyfour.ttf', 40))
    texto_degradado(lienzo, (x, 346), 'Web Junior', fuente('Sixtyfour.ttf', 40))
    dibujo.text(
        (x, 430),
        '> Apasionado por la tecnología y el diseño.',
        font=fuente('Roboto.ttf', 28, 400),
        fill=TEXTO_PRIMARIO,
    )
    dibujo.text((x, 498), 'Python · JavaScript · HTML · CSS', font=fuente('Roboto.ttf', 24, 500), fill=ACENTO_SECUNDARIO)

    lienzo.save(SALIDA, 'JPEG', quality=88, optimize=True, progressive=True)
    print(f'{SALIDA} ({SALIDA.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    main()
