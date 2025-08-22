from PIL import Image, ImageOps
import os

def generar_variantes_llavero(ruta_imagen, carpeta_salida):
    # Asegurar que la carpeta exista
    os.makedirs(carpeta_salida, exist_ok=True)

    # Abrir imagen original
    img = Image.open(ruta_imagen).convert("RGBA")

    # 1. Guardar la imagen original a color (sin cambios)
    img.save(os.path.join(carpeta_salida, "llavero_color.png"))

    # 2. Generar versión en blanco y negro contornos
    img_gray = img.convert("L")
    img_edges = img_gray.point(lambda x: 0 if x < 128 else 255, '1')  # Umbral binario
    img_edges.save(os.path.join(carpeta_salida, "llavero_bn_contorno.png"))

    # 3. Generar versión en blanco y negro relleno (silueta)
    img_silueta = ImageOps.invert(img_gray)  # invertimos para silueta
    img_silueta = img_silueta.point(lambda x: 0 if x < 128 else 255, '1')
    img_silueta.save(os.path.join(carpeta_salida, "llavero_bn_relleno.png"))

    print("✅ Tres imágenes generadas en:", carpeta_salida)


# Ejemplo de uso
generar_variantes_llavero("entrada.png", "salida_llavero")