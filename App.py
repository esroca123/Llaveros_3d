import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor para la entrada de datos (siempre visible) ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash", "Lego", "Ghibli"]
    todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # Selectbox principal
    estilo_seleccionado = st.selectbox(
        "Estilo de la colección de llaveros",
        ["Initial of a word", "Free Style", "A partir de una imagen", "Full Name/Phrase"] + todos_los estilos
    )

    # Campo para la descripción de la colección
    descripcion_coleccion = st.text_area(
        "Descripción de la colección",
        placeholder="Describe el tema o concepto para los cuatro diseños (ej., 'cuatro animales de la selva', 'vehículos de carreras')."
    )

    # Campo para detalles adicionales
    descripcion_opcional = st.text_area(
        "Detalles adicionales para cada diseño (opcional)",
        placeholder="Añade aquí detalles específicos sobre el estilo, personajes, etc."
    )
    
    # Nuevo campo para el soporte
    descripcion_soporte = st.text_area(
        "Descripción especial del soporte (opcional)",
        placeholder="Ej., 'con el nombre de Juan', 'diseñado como un árbol', 'con la fecha 2024'."
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

    # Campos opcionales
    cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

# --- Aquí se definen todos los prompts fijos y dinámicos antes del botón ---

# -------------------------------------------------------------------------
# PROMPTS FIJOS (Soportes, Variantes y Presentación)
# -------------------------------------------------------------------------

prompt_soporte_pared = (
    f"Create a highly **creative, innovative, and aesthetic wall-mounted stand** to hang four decorative designs. "
    f"The design must be a functional art piece that **reflects and complements the theme of the collection**, not just a simple hanger. "
    f"The design must have a flat back for easy mounting, be simple and stable, with minimal overhangs, making it suitable for easy 3D printing. "
    f"It must include four hooks or holes to hang the designs. "
    f"{descripcion_soporte}"
    f"The stand must be visible in its entirety. No designs should be attached yet."
)

prompt_soporte_pie = (
    f"Create a highly **creative, innovative, and aesthetic free-standing stand** to hold four decorative designs. "
    f"The design must be a functional art piece that **reflects and complements the theme of the collection**, not just a simple hanger. "
    f"The design must have a wide, stable base and a vertical structure with four hooks or pegs. It must be simple and stable, with minimal overhangs, making it suitable for easy 3D printing. "
    f"It.must include four hooks or holes to hang the designs. "
    f"{descripcion_soporte}"
    f"The stand must be visible in its entirety. No designs should be attached yet."
)

# PROMPT DXF (Agujero eliminado y consistencia geométrica añadida)
prompt_dxf = (
    f"Generate a black and white line art version of the **single design** from the attached image, optimized for DXF file conversion. "
    f"**Maintain the exact size and aspect ratio of the attached image.** "
    f"The design must have only thin, continuous outlines, no shadows, and a clean vector style. "
    f"Crucial: Do not include any hole or attachment point in the design. "
    f"Important: Base the output only on the provided image, do not add new elements or alter the core design. "
    f"The background must be pure white (RGB 255, 255, 255)."
)

# PROMPT SILUETA MEJORADO (FINAL: Fusión total, sin detalles internos)
prompt_silhouette = (
    f"Generate a complete, solid, and technical black silhouette of the **single design** from the attached image. "
    f"**Crucial:** The output must be a single, monolithic, **100% filled black shape** that represents **only the exact outer perimeter** of the design. "
    f"**It must completely fuse all interior shapes and lines from the original design into one undifferentiated black mass.** "
    f"**Maintain the exact size and aspect ratio of the attached image.** "
    f"The design must have no internal lines, no shadows, no gradients, and no internal white spaces whatsoever. "
    f"Crucial: Do not include any hole or attachment point in the design. "
    f"Important: Base the output only on the provided image, do not add new elements. "
    f"The background must be pure white (RGB 255, 255, 255)."
)


# PROMPT DE SEPARACIÓN DE COLORES (FINAL: forzando grosor mínimo y claridad binaria al 100%)
prompt_separacion_colores = (
    f"Based on the attached **black and white line art image of the single design**, generate a **100% binary inverted, technical Fill-In version for industrial color separation**. "
    f"**Maintain the exact size and aspect ratio of the attached image.** No gradients, no shadows, pure black and pure white only. "
    f"The transformation must strictly adhere to a complete inversion, ensuring: "
    f"1. **Solid Black Fills (100% Inversion):** **ALL areas that were originally white within the design's perimeter** (excluding the outer background) must now be filled with **solid, pure black**. The original figure must be 100% filled, without exception. "
    f"2. **Minimal White Separation:** The spaces created by the original black lines must be replaced by **pure white separation lines** with an **ABSOLUTELY MINIMAL stroke thickness (1-pixel width only)**, acting only as clean, razor-thin divisions between the black shapes. The goal is the thinnest possible white line for precision manufacturing. "
    f"3. **Outer Background:** The outer background must remain **pure white** (RGB 255, 255, 255). "
    f"Crucial: Do not include any hole or attachment point in the design. "
    f"The output must be a clean, binary image, ready for industrial color layering."
)


prompt_presentacion_llaveros_solos = (
    f"Create a high-quality, professional product shot for an e-commerce platform. "
    f"Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** "
    f"The designs should be arranged in a visually interesting and appealing composition. "
    f"The background should be a decorative setting that complements the theme of the collection, like a **minimalist studio with soft lighting** or a **natural wood table with a subtle texture**. "
    f"The final image should highlight the vibrant colors and detailed designs, making them look like premium collectible items."
)

prompt_presentacion_soporte_pared = (
    f"Create a high-quality, professional product shot for an e-commerce platform. "
    f"Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** "
    f"The designs should be beautifully **mounted and naturally hanging** on the previously designed **wall-mounted stand**. "
    f"Ensure perfect integration, realistic lighting, and natural shadows. "
    f"The background should be a decorative setting that complements the theme of the collection. "
