import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash", "Lego", "Ghibli"]
    todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # Selectbox principal que incluye la nueva opción
    estilo_seleccionado = st.selectbox(
        "Estilo de la colección de llaveros",
        ["Initial of a word", "Free Style", "A partir de una imagen", "Full Name/Phrase"] + todos_los_estilos
    )

    # Campo para la descripción que ahora siempre está visible
    descripcion_coleccion = st.text_area(
        "Descripción de la colección",
        placeholder="Describe el tema o concepto para los cuatro llaveros (ej., 'cuatro animales de la selva', 'vehículos de carreras')."
    )

    # Campo para la descripción que ahora siempre está visible
    descripcion_opcional = st.text_area(
        "Detalles adicionales para cada llavero (opcional)",
        placeholder="Añade aquí detalles específicos sobre el estilo, personajes, etc."
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

    # Lógica para la nueva opción "Full Name/Phrase"
    nombre_completo = None
    frase_integrada = None
    estilo_nombre_seleccionado = None
    if estilo_seleccionado == "Full Name/Phrase":
        nombre_completo = st.text_input("Nombre completo", placeholder="ej., María Fernanda")
        frase_integrada = st.text_input("Frase para integrar (opcional)", placeholder="ej., 'La mejor mamá del mundo'")
        estilo_nombre_seleccionado = st.selectbox("Estilo para el nombre", todos_los_estilos)

    # Todos los campos opcionales que ahora siempre están visibles
    cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

# --- Botón para generar el prompt y validación ---
if st.button("Generar Prompts", type="primary"):
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Por favor, especifica la palabra para la inicial.")
    elif estilo_seleccionado == "Full Name/Phrase" and not nombre_completo:
        st.error("Por favor, especifica el nombre completo.")
    else:
        # Generar el prompt base
        base_prompt_coleccion = ""

        # Lógica para la opción de "A partir de una imagen"
        if estilo_seleccionado == "A partir de una imagen":
            base_prompt_coleccion = (
                f"A collection of four unique, highly detailed keychain designs in a {estilo_para_imagen_seleccionado.lower()} style, "
                f"based on a separate reference image provided to you. The collection theme is '{descripcion_coleccion}'."
            )
        # Lógica para la opción de "Initial of a word"
        elif estilo_seleccionado == "Initial of a word" and inicial_palabra:
            base_prompt_coleccion = f"A collection of four unique, highly detailed keychain designs based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style. The collection theme is '{descripcion_coleccion}'."
        # Lógica para la nueva opción "Full Name/Phrase"
        elif estilo_seleccionado == "Full Name/Phrase" and nombre_completo:
            base_prompt_coleccion = f"A collection of four unique, highly detailed keychain designs based on the full name '{nombre_completo}' in a {estilo_nombre_seleccionado.lower()} style. The phrase '{frase_integrada}' is beautifully and creatively integrated into the design. The collection theme is '{descripcion_coleccion}'."
        # Lógica para el resto de los estilos
        elif estilo_seleccionado != "Free Style":
            base_prompt_coleccion = f"A collection of four unique, highly detailed {estilo_seleccionado.lower()} keychain designs. The collection theme is '{descripcion_coleccion}'."
        else: # Free Style
            base_prompt_coleccion = f"A collection of four unique, highly detailed keychain designs. The collection theme is '{descripcion_coleccion}'."

        # Añadir todos los campos opcionales al prompt base
        if descripcion_opcional:
            base_prompt_coleccion += f" Additional details: {descripcion_opcional}."
        if icono:
            base_prompt_coleccion += f" Incorporate the {icono} icon."
        if texto_opcional:
            base_prompt_coleccion += f" Include the text: '{texto_opcional}'."

        if cantidad_colores != "Cualquiera":
            base_prompt_coleccion += f" The designs must use exactly {cantidad_colores} colors."
            if colores_seleccionados:
                colores_str = ", ".join(colores_seleccionados)
                base_prompt_coleccion += f" Suggested colors: {colores_str}."
        elif colores_seleccionados:
            colores_str = ", ".join(colores_seleccionados)
            base_prompt_coleccion += f" Suggested colors: {colores_str}."

        # Generar los prompts individuales para cada variación de la colección
        prompt_coleccion_full_color = (
            f"Generate four highly detailed, full-color keychain designs for a cohesive collection, presented in a 2x2 grid. "
            f"Each design is a custom, stylized figure where the entire figure itself is the main body of the keychain. "
            f"A single, small, and functional keyring hole (an integrated ring eyelet) is seamlessly incorporated into the top of each character's head or a prominent part of their upper body. "
            f"This keyring hole is the ONLY hole or loop on the keychain's body. "
            f"The image must show the keychain design ONLY, with NO attached metallic keyrings, chains, or accessories. "
            f"The characters are depicted with unique, action-oriented stances, creating visually striking and collectible items. "
            f"The figures should look like high-quality, stylized collectible figures, with vibrant colors and sharp details. "
            f"Use a clean, minimalist background to highlight the designs. "
            f"The overall theme is: '{descripcion_coleccion}'. Additional details: {descripcion_opcional}."
        )

        prompt_dxf = (
            f"Generate a black and white line art version of the keychain design from the attached image, optimized for DXF file conversion. "
            f"It must have only thin outlines, no shadows, a clean vector style. "
            f"The design must include a single keyring hole at the top. "
            f"Important: Base the output only on the provided image, do not add new elements or alter the core design."
        )

        prompt_silhouette = (
            f"Generate a complete, solid black silhouette of the keychain design from the attached image. "
            f"The design must have no internal lines. It must include a single keyring hole at the top. "
            f"Important: Base the output only on the provided image, do not add new elements."
        )

        prompt_separacion_colores = (
            f"Generate a single-color version of the keychain design from the attached image. "
            f"Each original color area should be filled with solid black, maintaining the separation between the different parts, "
            f"with fully filled shapes and no empty spaces. It must include a single keyring hole at the top. "
            f"Important: Base the output only on the provided image, do not add new elements."
        )

        # Generar el prompt para el soporte
        prompt_soporte = (
            f"Create a unique, innovative, and highly detailed stand to hang four keychains from the collection '{descripcion_coleccion}'. "
            f"The stand's design must be a perfect match for the style '{estilo_seleccionado}' and the theme of the keychains. "
            f"It must be aesthetically pleasing, functional, and include four hooks or holes to hang the keychains. "
            f"The stand must be visible in its entirety, with a clean background. No keychains should be attached yet."
        )

        # Generar el prompt para la presentación final
        prompt_presentacion = (
            f"Create a high-quality, professional product shot. "
            f"Show the four keychains from the collection '{descripcion_coleccion}' mounted and hanging on the previously designed stand. "
            f"The presentation must highlight the unity of the collection and the innovative design of the stand, with soft lighting and a minimalist background. "
            f"All elements must be perfectly aligned and aesthetically appealing."
        )

        # Mostrar los resultados y los botones de copiar nativos de Streamlit
        st.divider()
        st.subheader("✅ Tus prompts están listos:")

        # Prompt para la colección de 4 llaveros (versión a color)
        st.markdown("### 1. Prompt para la colección de 4 llaveros (versión a color)")
        st.code(prompt_coleccion_full_color, language="markdown")

        # Prompts para las variantes (para usarse con la imagen generada en el paso 1)
        st.markdown("---")
        st.markdown("### 2. Prompts para las variantes (para usarse con la imagen generada en el paso 1)")

        st.markdown("#### Prompt para versión DXF")
        st.code(prompt_dxf, language="markdown")

        st.markdown("#### Prompt para versión Silueta")
        st.code(prompt_silhouette, language="markdown")

        st.markdown("#### Prompt para versión Separación de Colores")
        st.code(prompt_separacion_colores, language="markdown")

        # Prompt para generar el soporte para llaveros
        st.markdown("---")
        st.markdown("### 3. Prompt para generar el soporte para llaveros")
        st.code(prompt_soporte, language="markdown")

        # Prompt para la presentación final (con llaveros montados)
        st.markdown("---")
        st.markdown("### 4. Prompt para la presentación final (con llaveros montados)")
        st.code(prompt_presentacion, language="markdown")
