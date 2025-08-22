# streamlit_app.py
import streamlit as st

# Definir colecciones y tipos de llaveros
collections = [
    "Animales", "Frases Creativas", "Arcade", "Pokémon", "Floral",
    "Minimalista", "Gamer", "Personajes Populares"
]

keychain_types = [
    "Frase", "Icono", "Personaje", "Combinado"
]

def generate_combined_prompt(description, collection, keychain_type):
    """
    Genera un prompt único que incluye la colección y tipo de llavero.
    Contiene todas las variaciones en una misma imagen.
    """
    prompt = (
        f"Generate a single image for a {keychain_type} keychain/portavaso in the '{collection}' collection, based on: {description}. "
        "The image must include three variations in one frame: "
        "1) Full color version of the design, "
        "2) High-contrast black and white version suitable for DXF, "
        "3) Version where all colors are filled entirely in black, keeping the same layout, "
        "on a white background. "
        "Ensure all variations are visible, clear, and suitable for 3D extrusion."
    )
    return prompt

# Streamlit app
st.title("Generador de Prompt para Llaveros y Portavasos")

st.write("Selecciona la colección y el tipo de llavero, describe el diseño, y genera un prompt único con todas las variaciones en la misma imagen.")

# Selección de colección y tipo
selected_collection = st.selectbox("Selecciona la colección", collections)
selected_type = st.selectbox("Selecciona el tipo de llavero", keychain_types)

# Descripción del diseño
description = st.text_area("Descripción del diseño", height=100)

if st.button("Generar Prompt"):
    if description.strip() == "":
        st.warning("Por favor, ingresa una descripción válida.")
    else:
        prompt = generate_combined_prompt(description, selected_collection, selected_type)
        st.success("Prompt generado correctamente:")
        st.code(prompt, language="text")