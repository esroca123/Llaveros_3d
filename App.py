import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Create detailed prompts to generate unique keychain designs with AI.")
st.markdown("The resulting prompt will request a single image with three design variations.")

# --- Main container for data entry ---
with st.container():
    st.subheader("🛠️ Customize your Keychain")

    # Style and description container
    with st.container():
        estilos_opciones = ["Minimalist", "Futurist", "Cartoon", "Initial of a word"]
        estilo_seleccionado = st.selectbox("Keychain Style", estilos_opciones)
        
        if estilo_seleccionado == "Initial of a word":
            inicial_palabra = st.text_input("Word for the initial", placeholder="e.g., Alexandra")
        else:
            inicial_palabra = None

        descripcion_opcional = st.text_area("Additional style description (optional)", placeholder="Add specific details about the style here.")

    # Colors container
    with st.container():
        colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
        colores_seleccionados = st.multiselect("Suggested Colors (max. 4)", colores_opciones, max_selections=4)

    # Optional fields for text and icon
    icono = st.text_input("Icon or symbol (optional)", placeholder="e.g., lightning, moon, flower")
    texto_opcional = st.text_input("Text or phrase (optional)", placeholder="e.g., 'Happy Birthday'")

# --- Button to generate the prompt and validation ---
if st.button("Generate Prompt", type="primary"):
    if not estilo_seleccionado or (estilo_seleccionado == "Initial of a word" and not inicial_palabra):
        st.error("Please select a style and specify the word for the initial if needed.")
    elif not colores_seleccionados:
        st.error("Please select at least one color.")
    else:
        # Generate the base prompt
        prompt = "Generate a single image of a keychain design with the following characteristics: "
        
        # Add the style part
        if estilo_seleccionado == "Initial of a word" and inicial_palabra:
            prompt += f"A design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_seleccionado.lower()} style."
        else:
            prompt += f"A {estilo_seleccionado.lower()} keychain design."

        # Add optional description and icon
        if descripcion_opcional:
            prompt += f" Additional details: {descripcion_opcional}."
        if icono:
            prompt += f" Incorporate the {icono} icon."
        if texto_opcional:
            prompt += f" Include the text: '{texto_opcional}'."
        
        # Add a hole for the keyring, no ring included
        prompt += " The design includes a hole for the keyring but no ring attached."

        # Add suggested colors
        colores_str = ", ".join(colores_seleccionados)
        prompt += f" Suggested colors: {colores_str}."

        # Specify the generation of the three images
        prompt += (
            " The image must include three variations of the same design: "
            "1. A full-color version. "
            "2. A black and white version with clear, defined contours, optimized for DXF file generation. "
            "3. A single-color version where all original colors are replaced by black, identifying the different colored areas as black shapes. "
            "All three versions should be visible within a single, unified image."
        )
        
        # Display the result
        st.divider()
        st.subheader("✅ Your prompt is ready:")
        st.text_area("Copy your prompt here:", prompt, height=250)
        st.balloons()
