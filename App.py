import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# Definición de estilos
estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash"]

todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu llavero")

    # Selectbox principal que incluye la nueva opción
    estilo_seleccionado = st.selectbox(
        "Estilo del llavero", 
        ["Initial of a word", "Free Style", "Subir imagen"] + todos_los_estilos
    )

    # Lógica condicional para manejar las diferentes opciones
    if estilo_seleccionado == "Subir imagen":
        # Interfaz para la opción de subir imagen
        st.markdown("Sube una imagen y describe cómo quieres que la IA la adapte al diseño del llavero.")
        imagen_subida = st.file_uploader("Sube una imagen de base:", type=["png", "jpg", "jpeg"])
        descripcion_opcional = st.text_area(
            "Descripción para el llavero:",
            placeholder="Describe lo que quieres que aparezca, por ejemplo: 'la persona de la foto manejando una moto'."
        )
        # Se requiere un estilo adicional para la imagen subida
        estilo_para_imagen = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)

        # Botón y lógica para generar el prompt
        if st.button("Generar Prompt (desde imagen)", type="primary"):
            if imagen_subida is not None and descripcion_opcional:
                base_prompt_img = (
                    f"A creative, unique, highly detailed keychain design in a {estilo_para_imagen} style, "
                    f"based on the uploaded image. The design should incorporate the following: "
                    f"'{descripcion_opcional}'."
                )
                
                # Prompt con las 4 variaciones
                prompt_completo = (
                    f"Generate a single image of a keychain design with the following four distinct sections arranged horizontally: "
                    f"1. On the far right: A full-color version of the {base_prompt_img} The design must include a keyring hole but no keyring attached."
                    f"2. Second from the right: A black and white line art version of the {base_prompt_img} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
                    f"3. Second from the left: A single-color version of the {base_prompt_img} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
                    f"4. On the far left: A complete, solid black silhouette of the {base_prompt_img} with no internal lines. The design must include a keyring hole but no keyring attached."
                    " Ensure there is clear space separating each of the four variations to prevent overlap."
                )
                
                st.divider()
                st.subheader("✅ Tu prompt (para imagen) está listo:")
                st.text_area("Copia este prompt y pégalo en tu IA de preferencia junto con la imagen subida:", prompt_completo, height=400)
            else:
                st.error("Por favor, sube una imagen y añade una descripción.")

    else:
        # Interfaz original para estilos de texto
        if estilo_seleccionado == "Initial of a word":
            inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej., Alexandra")
            estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)
        else:
            inicial_palabra = None
            estilo_inicial_seleccionado = None

        descripcion_opcional = st.text_area("Descripción de estilo adicional (opcional)", placeholder="Añade aquí detalles específicos sobre el estilo o el personaje.")

        cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
        colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
        colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

        icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
        texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

        # Botón y lógica para generar el prompt con texto
        if st.button("Generar Prompt", type="primary"):
            if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
                st.error("Por favor, especifica la palabra para la inicial.")
            else:
                base_prompt_txt = ""
                if estilo_seleccionado == "Initial of a word" and inicial_palabra:
                    base_prompt_txt = f"A creative, unique, highly detailed design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style."
                elif estilo_seleccionado == "Free Style":
                    base_prompt_txt = f"A creative, unique, highly detailed keychain design. "
                else:
                    base_prompt_txt = f"A creative, unique, highly detailed {estilo_seleccionado.lower()} keychain design."

                if descripcion_opcional:
                    base_prompt_txt += f" Additional details: {descripcion_opcional}."
                if icono:
                    base_prompt_txt += f" Incorporate the {icono} icon."
                if texto_opcional:
                    base_prompt_txt += f" Include the text: '{texto_opcional}'."
                
                if cantidad_colores != "Cualquiera":
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
                st.subheader("✅ Tu prompt está listo:")
                st.text_area("Copia tu prompt aquí:", prompt_completo, height=350)

