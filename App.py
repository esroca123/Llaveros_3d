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
        placeholder="Describe el tema o concepto para los cuatro diseños (ej., 'cuatro animales de la selva', 'vehículos de carreras')."
    )

    # Campo para la descripción que ahora siempre está visible
    descripcion_opcional = st.text_area(
        "Detalles adicionales para cada diseño (opcional)",
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
        estilo_prompt = ""
        base_prompt_coleccion = ""

        # Lógica para la opción de "A partir de una imagen"
        if estilo_seleccionado == "A partir de una imagen":
            estilo_prompt = estilo_para_imagen_seleccionado.lower()
        # Lógica para la opción de "Initial of a word"
        elif estilo_seleccionado == "Initial of a word" and inicial_palabra:
            estilo_prompt = estilo_inicial_seleccionado.lower()
        # Lógica para la nueva opción "Full Name/Phrase"
        elif estilo_seleccionado == "Full Name/Phrase" and nombre_completo:
            estilo_prompt = estilo_nombre_seleccionado.lower()
        # Lógica para el resto de los estilos
        elif estilo_seleccionado != "Free Style":
            estilo_prompt = estilo_seleccionado.lower()
        else: # Free Style
            estilo_prompt = "modern" # Estilo predeterminado si es "Free Style"

        # Generar el prompt principal para la colección a color
        prompt_coleccion_full_color = (
            f"Generate four highly detailed, full-color decorative art designs in a {estilo_prompt} style, presented in a 2x2 grid. "
            f"Each design is a custom, stylized figure, word, or symbol, where the entire piece itself is the main body of the art. "
            f"A single, small, and functional circular hole for attachment is seamlessly incorporated into the top of each design. "
            f"This attachment hole is the ONLY hole or loop on the main body of the design. "
            f"The image must show the designs ONLY, with ABSOLUTELY NO attached metallic rings, chains, hooks, or any other accessories. "
            f"The designs should look like high-quality, stylized collectible pieces, with vibrant colors and sharp details. "
            f"The background must be pure white (RGB 255, 255, 255). "
            f"The overall theme is: '{descripcion_coleccion}'. Additional details: {descripcion_opcional}."
        )

        # Añado la lógica específica para la opción de "Full Name/Phrase"
        if estilo_seleccionado == "Full Name/Phrase" and nombre_completo:
            prompt_coleccion_full_color += f" The designs are based on the full name '{nombre_completo}'. "
            if frase_integrada:
                prompt_coleccion_full_color += f"The phrase '{frase_integrada}' is beautifully and creatively integrated into the design."
            
        # Añadir todos los campos opcionales al prompt principal
        if icono:
            prompt_coleccion_full_color += f" Incorporate the {icono} icon."
        if texto_opcional:
            prompt_coleccion_full_color += f" Include the text: '{texto_opcional}'."

        if cantidad_colores != "Cualquiera":
            prompt_coleccion_full_color += f" The designs must use exactly {cantidad_colores} colors."
            if colores_seleccionados:
                colores_str = ", ".join(colores_seleccionados)
                prompt_coleccion_full_color += f" Suggested colors: {colores_str}."
        elif colores_seleccionados:
            colores_str = ", ".join(colores_seleccionados)
            prompt_coleccion_full_color += f" Suggested colors: {colores_str}."

        prompt_dxf = (
            f"Generate a black and white line art version of the design from the attached image, optimized for DXF file conversion. "
            f"It must have only thin outlines, no shadows, a clean vector style. "
            f"The design must include a single circular hole for attachment at the top. "
            f"Important: Base the output only on the provided image, do not add new elements or alter the core design. "
            f"The background must be pure white (RGB 255, 255, 255)."
        )

        prompt_silhouette = (
            f"Generate a complete, solid black silhouette of the design from the attached image. "
            f"The design must have no internal lines. It must include a single circular hole for attachment at the top. "
            f"Important: Base the output only on the provided image, do not add new elements. "
            f"The background must be pure white (RGB 255, 255, 255)."
        )

        prompt_separacion_colores = (
            f"Based on the attached image, generate a simplified version for manufacturing. "
            f"Each distinct color area of the original design should be represented as a **solid black shape,** clearly separated from the others. "
            f"The design must also include a single circular hole for attachment. "
            f"The background must be pure white (RGB 255, 255, 255)."
        )

        # Generar el prompt para el soporte
        prompt_soporte = (
            f"Create a unique, innovative, and highly detailed stand to hang four decorative designs. "
            f"The stand can be either a wall-mounted design or a free-standing design. "
            f"Its style must perfectly match the style and theme of the four designs shown in the attached image. "
            f"It must be aesthetically pleasing, functional, and include four hooks or holes to hang the designs. "
            f"The stand must be visible in its entirety. No designs should be attached yet."
        )

        # Generar el prompt para la presentación final - CORREGIDO
        prompt_presentacion = (
            f"Create a high-quality, professional product shot for an e-commerce platform. "
            f"Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** "
            f"The designs should be beautifully **mounted and naturally hanging** on the previously designed stand. "
            f"Ensure perfect integration, realistic lighting, and natural shadows. "
            f"The background should be a decorative setting that complements the theme of the collection, like a **minimalist studio with soft lighting** or a **natural wood table with a subtle texture**. "
            f"The final image should highlight the unity of the collection and the innovative design of the stand, with all elements perfectly aligned and aesthetically appealing."
        )

        # Mostrar los resultados y los botones de copiar nativos de Streamlit
        st.divider()
        st.subheader("✅ Tus prompts están listos:")

        # Prompt para la colección de 4 llaveros (versión a color)
        st.markdown("### 1. Prompt para la colección de 4 diseños decorativos (sin argolla)")
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
        st.markdown("### 3. Prompt para generar el soporte para los diseños")
        st.code(prompt_soporte, language="markdown")

        # Prompt para la presentación final (con llaveros montados)
        st.markdown("---")
        st.markdown("### 4. Prompt para la presentación final (con los diseños montados)")
        st.code(prompt_presentacion, language="markdown")
