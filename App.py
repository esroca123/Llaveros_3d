# Generador de prompts para llaveros en colecciones
# Versión simple (no requiere librerías externas)

def generar_prompt_llavero(nombre_coleccion, tema, estilo, cantidad):
    prompts = []
    for i in range(1, cantidad + 1):
        prompt = (
            f"Llavero de la colección '{nombre_coleccion}', "
            f"diseño {i}, tema: {tema}, estilo: {estilo}, "
            f"formato 3D sencillo, máximo 4 colores, bajo relieve, "
            f"apto para impresión 3D, vista frontal."
        )
        prompts.append(prompt)
    return prompts


# Ejemplo de uso
coleccion = "Animales Fantásticos"
tema = "Dragones y criaturas míticas"
estilo = "Minimalista, moderno"
cantidad_disenos = 4

prompts_llaveros = generar_prompt_llavero(coleccion, tema, estilo, cantidad_disenos)

print("=== Prompts generados para llaveros ===")
for p in prompts_llaveros:
    print("-", p)