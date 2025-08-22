import cv2
import numpy as np
import potrace
from PIL import Image
import argparse

def posterize_image(image, num_colors=4):
    """
    Reduce la cantidad de colores en la imagen para separar mejor las zonas.
    """
    # Convertir a RGB
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    Z = img.reshape((-1, 3))

    # Convertir a float32
    Z = np.float32(Z)

    # Definir criterios de k-means y aplicar clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    K = num_colors
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    clustered_img = res.reshape((img.shape))

    return clustered_img

def convert_to_bw(image):
    """
    Convierte la imagen en varias capas en blanco y negro según colores separados.
    """
    # Posterización a pocos colores
    posterized = posterize_image(image, num_colors=4)

    bw_layers = []
    for i in np.unique(posterized.reshape(-1, 3), axis=0):
        mask = cv2.inRange(posterized, i, i)
        bw_layers.append(mask)

    return bw_layers

def save_as_svg(bw_layers, output_path):
    """
    Convierte las capas en blanco y negro a SVG usando potrace.
    """
    svg_content = ""

    for idx, layer in enumerate(bw_layers):
        pil_img = Image.fromarray(layer).convert("1")
        bitmap = potrace.Bitmap(np.array(pil_img))
        path = bitmap.trace()

        # Crear SVG parcial
        layer_svg = '<g fill="black">'
        for curve in path:
            layer_svg += '<path d="M '
            for segment in curve:
                if segment.is_corner:
                    c = segment.c
                    layer_svg += f"L {c[1][0]} {c[1][1]} "
                else:
                    c = segment.c
                    layer_svg += f"C {c[0][0]} {c[0][1]}, {c[1][0]} {c[1][1]}, {c[2][0]} {c[2][1]} "
            layer_svg += 'Z" />'
        layer_svg += '</g>'
        svg_content += layer_svg

    # SVG final
    svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
    svg_footer = '</svg>'
    final_svg = svg_header + svg_content + svg_footer

    with open(output_path, "w") as f:
        f.write(final_svg)

def main():
    parser = argparse.ArgumentParser(description="Convertir PNG a SVG con separación de colores.")
    parser.add_argument("input", help="Ruta de la imagen PNG de entrada")
    parser.add_argument("output", help="Ruta del archivo SVG de salida")
    args = parser.parse_args()

    # Leer imagen
    image = cv2.imread(args.input)

    # Separar en capas por colores
    bw_layers = convert_to_bw(image)

    # Guardar como SVG
    save_as_svg(bw_layers, args.output)

if __name__ == "__main__":
    main()