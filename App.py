import cv2
import numpy as np
import matplotlib.pyplot as plt

def procesar_imagen(ruta_imagen, salida="resultado.png"):
    # Cargar imagen
    img = cv2.imread(ruta_imagen)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ---- 1. Versión en blanco y negro (silueta) ----
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bn = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)

    # ---- 2. Versión con colores indexados (mapa de colores -> números) ----
    Z = img_rgb.reshape((-1,3))
    Z = np.float32(Z)

    # Usamos KMeans para reducir la cantidad de colores detectados
    K = 6  # número máximo de colores (puedes ajustarlo)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    labels = labels.flatten()
    mapa_colores = labels.reshape(img_rgb.shape[:2])

    # Creamos una imagen negra y escribimos el número de cada color
    img_indexada = np.zeros_like(img_rgb)
    for i in range(K):
        mask = (mapa_colores == i)
        img_indexada[mask] = [0, 0, 0]  # negro
        # Escribimos un número en el centro de la región
        coords = np.column_stack(np.where(mask))
        if len(coords) > 0:
            y, x = coords[len(coords)//2]  # punto medio de la región
            cv2.putText(img_indexada, str(i+1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.4, (255,255,255), 1, cv2.LINE_AA)

    # ---- Mostrar en una sola imagen ----
    fig, axs = plt.subplots(1, 3, figsize=(15,5))
    axs[0].imshow(img_rgb)
    axs[0].set_title("Versión a color")
    axs[0].axis("off")

    axs[1].imshow(bn, cmap="gray")
    axs[1].set_title("Versión blanco y negro")
    axs[1].axis("off")

    axs[2].imshow(img_indexada)
    axs[2].set_title("Colores numerados")
    axs[2].axis("off")

    plt.tight_layout()
    plt.savefig(salida, dpi=300)
    plt.show()

# Ejemplo de uso
# procesar_imagen("imagen.png", "resultado.png")