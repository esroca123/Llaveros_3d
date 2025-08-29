import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu llavero")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash"]
    todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # Selectbox principal que incluye la nueva opción
    estilo_seleccionado = st.selectbox(
        "Estilo del llavero", 
        ["Initial of a word", "Free Style", "A partir de una imagen"] + todos_los_estilos
    )
    
    # Campo para la descripción que ahora siempre está visible
    descripcion_opcional = st.text_area(
        "Descripción adicional (opcional)",
        placeholder="Añade aquí detalles específicos sobre el estilo o el personaje."
    )
    
    # Lógica para la opción de "Initial of a word"
    inicial_palabra = None
    estilo_inicial_seleccionado = None
    if estilo_seleccionado == "Initial of a word":
        inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej., Alexandra")
        estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)
    
    # Lógica para la opción "A partir de una imagen"
    estilo_para_imagen_seleccionado = None
    if estilo_seleccionado == "A partir de una imagen":
        st.markdown("La imagen de referencia debe subirse a la IA de tu elección por separado.")
        estilo_para_imagen_seleccionado = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)

    # Todos los campos opcionales que ahora siempre están visibles
    cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

# --- Botón para generar el prompt y validación ---

if st.button("Generar Prompt", type="primary"):
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Por favor, especifica la palabra para la inicial.")
    else:
        # Generar el prompt base
        base_prompt = ""
        
        # Lógica para la opción de "A partir de una imagen"
        if estilo_seleccionado == "A partir de una imagen":
            base_prompt = (
                f"A creative, unique, highly detailed keychain design in a {estilo_para_imagen_seleccionado.lower()} style, "
                f"based on a separate reference image provided to you. "
            )
        # Lógica para la opción de "Initial of a word"
        elif estilo_seleccionado == "Initial of a word" and inicial_palabra:
            base_prompt = f"A creative, unique, highly detailed design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style."
        # Lógica para el resto de los estilos
        elif estilo_seleccionado != "Free Style":
            base_prompt = f"A creative, unique, highly detailed {estilo_seleccionado.lower()} keychain design."
        else: # Free Style
            base_prompt = f"A creative, unique, highly detailed keychain design."

        # Añadir todos los campos opcionales al prompt base
        if descripcion_opcional:
            base_prompt += f" Additional details: {descripcion_opcional}."
        if icono:
            base_prompt += f" Incorporate the {icono} icon."
        if texto_opcional:
            base_prompt += f" Include the text: '{texto_opcional}'."
        
        if cantidad_colores != "Cualquiera":
            base_prompt += f" The design must use exactly {cantidad_colores} colors."
            if colores_seleccionados:
                colores_str = ", ".join(colores_seleccionados)
                base_prompt += f" Suggested colors: {colores_str}."
        elif colores_seleccionados:
            colores_str = ", ".join(colores_seleccionados)
            base_prompt += f" Suggested colors: {colores_str}."

        # Generar los prompts individuales para cada variación
        prompt_full_color = f"{base_prompt} A full-color version. The design must include a keyring hole but no keyring attached."
        prompt_line_art = f"{base_prompt} A black and white line art version. It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
        prompt_single_color = f"{base_prompt} A single-color version, where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
        prompt_silhouette = f"{base_prompt} A complete, solid black silhouette, with no internal lines. The design must include a keyring hole but no keyring attached."

        # Unir los prompts en un formato de cuadrícula
        prompt_completo = (
            f"Create a single image containing four distinct keychain designs, arranged in a 2x2 grid. \n\n"
            f"Top-left: {prompt_full_color}\n\n"
            f"Top-right: {prompt_line_art}\n\n"
            f"Bottom-left: {prompt_single_color}\n\n"
            f"Bottom-right: {prompt_silhouette}\n\n"
            f"Ensure there is clear space separating each of the four variations to prevent overlap."
        )
        
        # Mostrar el resultado
        st.divider()
        st.subheader("✅ Tu prompt está listo:")
        st.text_area("Copia tu prompt aquí:", prompt_completo, height=450)
