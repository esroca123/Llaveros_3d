import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Create detailed prompts to generate unique keychain designs with AI.")
st.markdown("The resulting prompt will request a single image with four distinct design variations.")

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Customize your Keychain")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash"]
    todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # Selectbox principal que incluye la nueva opción
    estilo_seleccionado = st.selectbox(
        "Keychain Style", 
        ["Initial of a word", "Free Style", "A partir de una imagen"] + todos_los_estilos
    )
    
    # Lógica para la opción de "A partir de una imagen"
    if estilo_seleccionado == "A partir de una imagen":
        st.markdown("Sube una imagen y describe cómo quieres que la IA la adapte. **La imagen debe subirse a la IA de tu elección por separado.**")
        
        descripcion_opcional = st.text_area(
            "Description for the keychain:",
            placeholder="Describe what you want to appear, e.g., 'the person in the photo driving a futuristic motorcycle'."
        )
        # Se requiere un estilo adicional para la imagen
        estilo_para_imagen = st.selectbox("Style to apply to the image:", todos_los_estilos)
        
        # Botón y lógica para generar el prompt
        if st.button("Generate Prompt", type="primary"):
            if descripcion_opcional:
                # Prompt que indica a la IA que use la imagen de referencia
                prompt_base_img = (
                    f"A creative, unique, highly detailed keychain design in a {estilo_para_imagen} style, "
                    f"based on a separate reference image provided to you. The design should incorporate the following: "
                    f"'{descripcion_opcional}'."
                )
                
                # Prompt con las 4 variaciones
                prompt_completo = (
                    f"Generate a single image of a keychain design with the following four distinct sections arranged horizontally: "
                    f"1. On the far right: A full-color version of the {prompt_base_img} The design must include a keyring hole but no keyring attached."
                    f"2. Second from the right: A black and white line art version of the {prompt_base_img} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
                    f"3. Second from the left: A single-color version of the {prompt_base_img} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
                    f"4. On the far left: A complete, solid black silhouette of the {prompt_base_img} with no internal lines. The design must include a keyring hole but no keyring attached."
                    " Ensure there is clear space separating each of the four variations to prevent overlap."
                )
                
                st.divider()
                st.subheader("✅ Your prompt (for image) is ready:")
                st.text_area("Copy this prompt and paste it into your preferred AI (along with the reference image):", prompt_completo, height=400)
            else:
                st.error("Please add a description.")
                
    # Lógica para los estilos de texto
    else:
        if estilo_seleccionado == "Initial of a word":
            inicial_palabra = st.text_input("Word for the initial", placeholder="e.g., Alexandra")
            estilo_inicial_seleccionado = st.selectbox("Style for the initial", todos_los_estilos)
        else:
            inicial_palabra = None
            estilo_inicial_seleccionado = None

        descripcion_opcional = st.text_area("Additional style description (optional)", placeholder="Add specific details about the style or character here.")

        cantidad_colores = st.selectbox("Number of colors (optional)", ["Any"] + list(range(1, 5)))
        colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
        colores_seleccionados = st.multiselect("Suggested Colors (optional)", colores_opciones, max_selections=4)

        icono = st.text_input("Icon or symbol (optional)", placeholder="e.g., lightning, moon, flower")
        texto_opcional = st.text_input("Text or phrase (optional)", placeholder="e.g., 'Happy Birthday'")

        if st.button("Generate Prompt", type="primary"):
            if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
                st.error("Please specify the word for the initial.")
            else:
                base_prompt_txt = ""
                if estilo_seleccionado == "Initial of a word" and inicial_palabra:
                    base_prompt_txt = f"A **creative, unique, highly detailed** design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style."
                elif estilo_seleccionado == "Free Style":
                    base_prompt_txt = f"A **creative, unique, highly detailed** keychain design. "
                else:
                    base_prompt_txt = f"A **creative, unique, highly detailed** {estilo_seleccionado.lower()} keychain design."

                if descripcion_opcional:
                    base_prompt_txt += f" Additional details: {descripcion_opcional}."
                if icono:
                    base_prompt_txt += f" Incorporate the {icono} icon."
                if texto_opcional:
                    base_prompt_txt += f" Include the text: '{texto_opcional}'."
                
                if cantidad_colores != "Any":
                    base_prompt_txt += f" The design must use exactly {cantidad_colores} colors."
                    if colores_seleccionados:
                        colores_str = ", ".join(colores_seleccionados)
                        base_prompt_txt += f" Suggested colors: {colores_str}."
                elif colores_seleccionados:
                    colores_str = ", ".join(colores_seleccionados)
                    base_prompt_txt += f" Suggested colors: {colores_str}."

                prompt_completo = (
                    f"Generate a single image of a keychain design with the following four distinct sections arranged horizontally: "
                    f"1. On the far right: A full-color version of the {base_prompt_txt} The design must include a keyring hole but no keyring attached."
                    f"2. Second from the right: A black and white line art version of the {base_prompt_txt} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
                    f"3. Second from the left: A single-color version of the {base_prompt_txt} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
                    f"4. On the far left: A complete, solid black silhouette of the {base_prompt_txt} with no internal lines. The design must include a keyring hole but no keyring attached."
                    " Ensure there is clear space separating each of the four variations to prevent overlap."
                )
                
                st.divider()
                st.subheader("✅ Your prompt is ready:")
                st.text_area("Copy your prompt here:", prompt_completo, height=350)

