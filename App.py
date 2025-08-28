import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Create detailed prompts to generate unique keychain designs with AI.")
st.markdown("The resulting prompt will request a single image with four distinct design variations.")

# --- Main container for data entry ---
with st.container():
    st.subheader("🛠️ Customize your Keychain")

    # Style and description container
    with st.container():
        estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
        estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
        estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
        
        # Nuevos estilos temáticos añadidos
        estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty"]
        
        estilo_seleccionado = st.selectbox("Keychain Style", ["Initial of a word", "Free Style"] + estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos)

        if estilo_seleccionado == "Initial of a word":
            inicial_palabra = st.text_input("Word for the initial", placeholder="e.g., Alexandra")
            estilos_iniciales_disponibles = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos
            estilo_inicial_seleccionado = st.selectbox("Style for the initial", estilos_iniciales_disponibles)
        else:
            inicial_palabra = None
            estilo_inicial_seleccionado = None

        descripcion_opcional = st.text_area("Additional style description (optional)", placeholder="Add specific details about the style or character here.")

    # Colors container
    with st.container():
        cantidad_colores = st.selectbox("Number of colors (optional)", ["Any"] + list(range(1, 5)))
        colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
        colores_seleccionados = st.multiselect("Suggested Colors (optional)", colores_opciones, max_selections=4)

    # Optional fields for text and icon
    icono = st.text_input("Icon or symbol (optional)", placeholder="e.g., lightning, moon, flower")
    texto_opcional = st.text_input("Text or phrase (optional)", placeholder="e.g., 'Happy Birthday'")

# --- Button to generate the prompt and validation ---

if st.button("Generate Prompt", type="primary"):
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Please specify the word for the initial.")
    else:
        # Generate the base prompt
        prompt = "Generate a single image of a keychain design with the following characteristics, split into four distinct sections arranged horizontally: "
        
        # Add the style part, including the new "Free Style" logic
        if estilo_seleccionado == "Initial of a word" and inicial_palabra:
            base_prompt = f"A **creative, unique, highly detailed** design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style."
        elif estilo_seleccionado == "Free Style":
            base_prompt = f"A **creative, unique, highly detailed** keychain design. "
        else:
            base_prompt = f"A **creative, unique, highly detailed** {estilo_seleccionado.lower()} keychain design."

        # Add optional description, text and icon
        if descripcion_opcional:
            base_prompt += f" Additional details: {descripcion_opcional}."
        if icono:
            base_prompt += f" Incorporate the {icono} icon."
        if texto_opcional:
            base_prompt += f" Include the text: '{texto_opcional}'."
        
        # Add number of colors and suggested colors only if selected
        if cantidad_colores != "Any":
            base_prompt += f" The design must use exactly {cantidad_colores} colors."
            if colores_seleccionados:
                colores_str = ", ".join(colores_seleccionados)
                base_prompt += f" Suggested colors: {colores_str}."
        elif colores_seleccionados:
            colores_str = ", ".join(colores_seleccionados)
            base_prompt += f" Suggested colors: {colores_str}."

        # Specify the generation of the four images with horizontal arrangement
        prompt += (
            f"1. On the far right: A full-color version of the {base_prompt} The design must include a keyring hole but no keyring attached."
            f"2. Second from the right: A black and white line art version of the {base_prompt} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
            f"3. Second from the left: A single-color version of the {base_prompt} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
            f"4. On the far left: A complete, solid black silhouette of the {base_prompt} with no internal lines. The design must include a keyring hole but no keyring attached."
            " Ensure there is clear space separating each of the four variations to prevent overlap."
        )
        
        # Display the result
        st.divider()
        st.subheader("✅ Your prompt is ready:")
        st.text_area("Copy your prompt here:", prompt, height=350)