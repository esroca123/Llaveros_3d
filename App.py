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

def generate_combined_prompt(description, collection, keychain_type, initial):
    """
    Genera un prompt único que incluye:
    - Colección
    - Tipo de llavero
    - Descripción del diseño
    - Inicial del nombre
    - Agujero para la argolla
    - Todas las variaciones en la misma imagen
    """
    prompt = (
        f"Generate a single keychain image for a {keychain_type} keychain in the '{collection}' collection, based on: {description}. "
        f"The design should include the initial '{initial}' prominently. "
        "The keychain must have a hole for the keyring in the appropriate position. "
        "The image must include three variations in one frame: "
        "1) Full color version of the design, "
        "2) High-contrast black and white version suitable for DXF, "
        "3) Version where all colors are filled entirely in black, keeping the same layout, "
        "on a white background. "
        "Ensure all variations are clear, visible, and suitable for 3D extrusion."
    )
    return prompt

# Streamlit app
st.title("Generador de Prompt para Llaveros y Portavasos")

st.write("Selecciona la colección, tipo de llavero, ingresa la descripción y la inicial del nombre para generar un prompt único con todas las variaciones en la misma imagen.")

# Selección de colección y tipo
selected_collection = st.selectbox("Selecciona la colección", collections)
selected_type = st.selectbox("Selecciona el tipo de llavero", keychain_types)

# Entrada de descripción y inicial
description = st.text_area("Descripción del diseño", height=100)
initial = st.text_input("Inicial del nombre")

if st.button("Generar Prompt"):
    if description.strip() == "" or initial.strip() == "":
        st.warning("Por favor, ingresa una descripción válida y la inicial del nombre.")
    else:
        prompt = generate_combined_prompt(description, selected_collection, selected_type, initial.upper())
        st.success("Prompt generado correctamente:")
        st.code(prompt, language="text")