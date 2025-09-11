import streamlit as st

# --------------------------------------
# Título de la app
# --------------------------------------
st.title("Llavero Prompts Generator")
st.markdown("""
Crea prompts detallados para generar colecciones de llaveros únicos y su soporte.
Cada colección tendrá 4 llaveros coherentes, con opciones de derivar imágenes para DXF, silueta y separación de colores.
""")

# --------------------------------------
# Selección de estilo
# --------------------------------------
estilos = [
    "Estilo Creativo",
    "Estilo Minimalista",
    "Estilo Nombre + Frase",
    "Estilo Anime",
    "Estilo Gamer",
    "Estilo Flores"
]

estilo_seleccionado = st.selectbox("Selecciona un estilo de llavero:", estilos)

# --------------------------------------
# Inputs para estilo Nombre + Frase
# --------------------------------------
nombre = ""
frase = ""
if estilo_seleccionado == "Estilo Nombre + Frase":
    nombre = st.text_input("Ingresa el nombre completo:")
    frase = st.text_input("Ingresa una frase opcional:")

# --------------------------------------
# Generación de prompts para 4 llaveros
# --------------------------------------
coleccion_prompts = []

st.subheader("Prompts para la colección de 4 llaveros")

for i in range(1, 5):
    prompt = ""
    if estilo_seleccionado == "Estilo Nombre + Frase":
        prompt = f"Llavero {i}: Diseño creativo integrando el nombre '{nombre}'"
        if frase:
            prompt += f" y la frase '{frase}' de manera estética"
        prompt += ", estilo único y colorido, listo para impresión 3D."
    else:
        prompt = f"Llavero {i}: Diseño de estilo '{estilo_seleccionado}', coherente con la colección, colorido y detallado, listo para impresión 3D."
    
    coleccion_prompts.append(prompt)
    st.text_area(f"Prompt Llavero {i}", prompt, height=80, key=f"llavero_{i}")

# --------------------------------------
# Prompts derivados (DXF, silueta, separación de colores)
# --------------------------------------
st.subheader("Prompts derivados para cada llavero")
derived_prompts_template = {
    "DXF": "Convierte la imagen adjunta exactamente a blanco y negro, sin reinterpretación, alto contraste, fondo blanco, lista para DXF.",
    "Silueta": "Genera la silueta de la imagen adjunta, con contornos definidos y fondo transparente.",
    "Separación de colores": "Separa los colores de la imagen adjunta en capas, manteniendo los detalles para impresión en 3D."
}

for i, base_prompt in enumerate(coleccion_prompts, start=1):
    st.markdown(f"**Llavero {i}**")
    for tipo, derivado in derived_prompts_template.items():
        prompt_derivado = f"{derivado} Basado en la imagen del Llavero {i}."
        st.text_area(f"{tipo}", prompt_derivado, height=80, key=f"llavero_{i}_{tipo}")

# --------------------------------------
# Soporte y colección completa
# --------------------------------------
st.subheader("Soporte para colgar los llaveros")

soporte_prompt = f"Genera un soporte innovador para colgar los 4 llaveros de la colección de estilo '{estilo_seleccionado}', que se integre visualmente con el diseño de los llaveros y sea funcional."
st.text_area("Prompt Soporte", soporte_prompt, height=80, key="soporte")

coleccion_completa_prompt = f"Muestra los 4 llaveros montados en el soporte, formando una colección coherente de estilo '{estilo_seleccionado}'."
st.text_area("Prompt Colección Completa", coleccion_completa_prompt, height=80, key="coleccion_completa")

# --------------------------------------
# Botón de copiar todos los prompts
# --------------------------------------
st.subheader("Copiar prompts")
if st.button("Copiar todos los prompts"):
    todos_prompts = "\n\n".join(coleccion_prompts + 
                               [f"{tipo} Llavero {i}: {derivado}" 
                                for i in range(1,5) 
                                for tipo, derivado in derived_prompts_template.items()] + 
                               [soporte_prompt, coleccion_completa_prompt])
    st.code(todos_prompts)
    st.success("Todos los prompts han sido copiados a la vista de código. Ahora puedes seleccionarlos y copiarlos manualmente.")