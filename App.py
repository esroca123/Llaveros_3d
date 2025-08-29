import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# Definición de estilos (fuera de la lógica condicional para que sea accesible)
estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash"]

todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

# --- Seleccionar método de generación ---
st.subheader("Selecciona el método de generación")
metodo_seleccionado = st.radio(
    "Elige cómo quieres crear tu diseño:",
    ("A partir de texto (4 variaciones)", "A partir de una imagen")
)

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu llavero")

    if metodo_seleccionado == "A partir de texto (4 variaciones)":
        st.markdown("El prompt resultante solicitará una sola imagen con cuatro variaciones de diseño distintas.")

        # Style and description container
        with st.container():
            estilo_seleccionado = st.selectbox("Estilo del llavero", ["Initial of a word", "Free Style"] + todos_los_estilos)

            if estilo_seleccionado == "Initial of a word":
                inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej., Alexandra")
                estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)
            else:
                inicial_palabra = None
                estilo_inicial_seleccionado = None

            descripcion_opcional = st.text_area("Descripción de estilo adicional (opcional)", placeholder="Añade aquí detalles específicos sobre el estilo o el personaje.")

        # Colors container
        with st.container():
            cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
            colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
            colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

        # Optional fields for text and icon
        icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
        texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

        # --- Button to generate the prompt and validation ---
        if st.button("Generar Prompt (4 variaciones)", type="primary"):
            if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
                st.error("Por favor, especifica la palabra para la inicial.")
            else:
                # Generate the base prompt
                base_prompt = ""
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
                if cantidad_colores != "Cualquiera":
                    base_prompt += f" The design must use exactly {cantidad_colores} colors."
                    if colores_seleccionados:
                        colores_str = ", ".join(colores_seleccionados)
                        base_prompt += f" Suggested colors: {colores_str}."
                elif colores_seleccionados:
                    colores_str = ", ".join(colores_seleccionados)
                    base_prompt += f" Suggested colors: {colores_str}."

                # Specify the generation of the four images with horizontal arrangement
                prompt_completo = (
                    f"Generate a single image of a keychain design with the following four distinct sections arranged horizontally: "
                    f"1. On the far right: A full-color version of the {base_prompt} The design must include a keyring hole but no keyring attached."
                    f"2. Second from the right: A black and white line art version of the {base_prompt} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
                    f"3. Second from the left: A single-color version of the {base_prompt} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
                    f"4. On the far left: A complete, solid black silhouette of the {base_prompt} with no internal lines. The design must include a keyring hole but no keyring attached."
                    " Ensure there is clear space separating each of the four variations to prevent overlap."
                )
                
                # Display the result
                st.divider()
                st.subheader("✅ Tu prompt (4 variaciones) está listo:")
                st.text_area("Copia tu prompt aquí:", prompt_completo, height=350)

    else: # A partir de una imagen
        st.markdown("Sube una imagen y describe cómo quieres el llavero. El prompt resultante lo usarás junto con tu imagen en otra IA.")

        imagen_subida = st.file_uploader("Sube una imagen de base:", type=["png", "jpg", "jpeg"])
        
        estilo_seleccionado_img = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)
        
        descripcion_adicional_img = st.text_area(
            "Descripción adicional para el llavero (basado en la imagen):",
            placeholder="Describe lo que quieres que aparezca, por ejemplo: 'la persona de la foto manejando una moto en un paisaje futurista'."
        )
        
        if st.button("Generar Prompt (desde imagen)", type="primary"):
            if imagen_subida is not None and descripcion_adicional_img:
                # Genera el prompt para usar en la otra IA
                prompt_para_ia_con_imagen = (
                    f"A creative, unique, highly detailed keychain design in a {estilo_seleccionado_img} style, "
                    f"based on the uploaded image. The design should incorporate the following: "
                    f"'{descripcion_adicional_img}'. The design must include a keyring hole but no keyring attached."
                )
                
                # Muestra el resultado
                st.divider()
                st.subheader("✅ Tu prompt (para imagen) está listo:")
                st.text_area("Copia este prompt y pégalo en tu IA de preferencia junto con la imagen subida:", prompt_para_ia_con_imagen, height=200)
            else:
                st.error("Por favor, sube una imagen y añade una descripción.")

