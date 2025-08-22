import cv2
import numpy as np
import svgwrite

def image_to_keychain_svg(image_path, output_svg, keychain_size=(100, 100), hole_radius=5, hole_offset=5):
    """
    Convierte una imagen a un llavero en SVG en silueta negra, con agujero para la argolla.
    
    :param image_path: Ruta de la imagen de entrada
    :param output_svg: Ruta de salida del archivo SVG
    :param keychain_size: Tamaño del llavero (ancho, alto) en mm
    :param hole_radius: Radio del agujero en mm
    :param hole_offset: Distancia desde el borde superior al centro del agujero en mm
    """
    
    # Leer imagen en escala de grises
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Redimensionar al tamaño del llavero
    img = cv2.resize(img, keychain_size)
    
    # Umbralizar para convertir a silueta (blanco y negro)
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Crear documento SVG
    dwg = svgwrite.Drawing(output_svg, size=(f"{keychain_size[0]}mm", f"{keychain_size[1]}mm"))
    
    # Dibujar fondo blanco
    dwg.add(dwg.rect(insert=(0, 0), size=(f"{keychain_size[0]}mm", f"{keychain_size[1]}mm"), fill="white"))
    
    # Dibujar silueta negra
    for contour in contours:
        points = [(p[0][0], p[0][1]) for p in contour]
        dwg.add(dwg.polygon(points, fill="black"))
    
    # Añadir el agujero (círculo vacío en la parte superior central)
    hole_center = (keychain_size[0] / 2, hole_offset + hole_radius)
    dwg.add(dwg.circle(center=(f"{hole_center[0]}mm", f"{hole_center[1]}mm"),
                       r=f"{hole_radius}mm", fill="white"))
    
    # Guardar archivo
    dwg.save()
    print(f"Llavero guardado en {output_svg}")

# Ejemplo de uso
image_to_keychain_svg("entrada.png", "llavero.svg")