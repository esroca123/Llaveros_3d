import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")
st.markdown("El prompt resultante solicitará una sola imagen con cuatro variaciones de diseño distintas.")

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu llavero")

    # Contenedor de estilo y descripción
    with st.container():
        estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
        estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
        estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
        estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "color Splash"]
        
        estilo_seleccionado = st.selectbox("Estilo del llavero", ["Initial of a word", "Free Style"] + estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos)

        if estilo_seleccionado == "Initial of a word":
            inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej., Alexandra")
            estilos_iniciales_disponibles = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos
            estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", estilos_iniciales_disponibles)
        else:
            inicial_palabra = None
            estilo_inicial_seleccionado = None

        descripcion_opcional = st.text_area("Descripción de estilo adicional (opcional)", placeholder="Añade aquí detalles específicos sobre el estilo o el personaje.")

    # Contenedor de colores
    with st.container():
        cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
        colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
        colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

    # Campos opcionales para texto e icono
    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

# --- Botón para generar el prompt y validación ---

if st.button("Generar Prompt", type="primary"):
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Por favor, especifica la palabra para la inicial.")
    else:
        # Generar el prompt base
        base_prompt = ""
        
        if estilo_seleccionado == "Initial of a word" and inicial_palabra:
            base_prompt = f"A creative, unique, highly detailed design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style."
        elif estilo_seleccionado == "Free Style":
            base_prompt = f"A creative, unique, highly detailed keychain design."
        else:
            base_prompt = f"A creative, unique, highly detailed {estilo_seleccionado.lower()} keychain design."

        # Añadir descripción opcional, texto e icono
        if descripcion_opcional:
            base_prompt += f" Additional details: {descripcion_opcional}."
        if icono:
            base_prompt += f" Incorporate the {icono} icon."
        if texto_opcional:
            base_prompt += f" Include the text: '{texto_opcional}'."
        
        # Añadir cantidad de colores y colores sugeridos solo si se seleccionaron
        if cantidad_colores != "Cualquiera":
            base_prompt += f" The design must use exactly {cantidad_colores} colors."
            if colores_seleccionados:
                colores_str = ", ".join(colores_seleccionados)
                base_prompt += f" Suggested colors: {colores_str}."
        elif colores_seleccionados:
            colores_str = ", ".join(colores_seleccionados)
            base_prompt += f" Suggested colors: {colores_str}."

        # Generar los prompts específicos para cada variación
        prompt_full_color = f"A **full-color** version of the design based on: {base_prompt} The design must include a keyring hole but no keyring attached."
        prompt_line_art = f"A **black and white line art** version of the design based on: {base_prompt} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
        prompt_single_color = f"A **single-color** version of the design based on: {base_prompt} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
        prompt_silhouette = f"A complete, **solid black silhouette** of the design based on: {base_prompt} It must have no internal lines whatsoever, strictly a complete solid shape. The design must include a keyring hole but no keyring attached."
        
        # Combinar los prompts en un formato de cuadrícula
        final_prompt = (
            f"Generate a single image of a keychain design with the following four distinct sections arranged horizontally: \n\n"
            f"1. On the far right: {prompt_full_color}\n\n"
            f"2. Second from the right: {prompt_line_art}\n\n"
            f"3. Second from the left: {prompt_single_color}\n\n"
            f"4. On the far left: {prompt_silhouette}\n\n"
            f"Ensure there is clear space separating each of the four variations to prevent overlap."
        )
        
        # Mostrar el resultado
        st.divider()
        st.subheader("✅ Tu prompt está listo:")
        st.text_area("Copia tu prompt aquí:", final_prompt, height=350)
