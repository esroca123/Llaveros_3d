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
        # Descripción base del diseño
        if estilo_seleccionado == "Initial of a word" and inicial_palabra:
            base_prompt = f"A creative, detailed keychain design based on the letter '{inicial_palabra.upper()[0]}' in {estilo_inicial_seleccionado.lower()} style"
        elif estilo_seleccionado == "Free Style":
            base_prompt = "A creative, detailed keychain design"
        else:
            base_prompt = f"A creative, detailed {estilo_seleccionado.lower()} keychain design"

        if descripcion_opcional:
            base_prompt += f", with {descripcion_opcional}"
        if icono:
            base_prompt += f", featuring a {icono} icon"
        if texto_opcional:
            base_prompt += f", with the text '{texto_opcional}'"
        
        if cantidad_colores != "Any":
            base_prompt += f". Use exactly {cantidad_colores} colors"
            if colores_seleccionados:
                base_prompt += f": {', '.join(colores_seleccionados)}"
        elif colores_seleccionados:
            base_prompt += f". Suggested colors: {', '.join(colores_seleccionados)}"

        # Prompt final simplificado
        prompt = (
            f"Generate one image with four horizontal sections of the same keychain design: {base_prompt}. "
            "Each section shows a variation:\n"
            "1. Full-color version (with keyring hole, no keyring).\n"
            "2. Black & white line art (thin outlines, no shadows, clean vector, DXF-ready).\n"
            "3. Solid black fill version (all parts filled, no empty spaces).\n"
            "4. Pure silhouette (solid black, no internal lines).\n"
            "Keep clear separation between the four variations."
        )

        st.divider()
        st.subheader("✅ Your prompt is ready:")
        st.text_area("Copy your prompt here:", prompt, height=300)
