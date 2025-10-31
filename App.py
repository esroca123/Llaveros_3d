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
    
    # ESTILO MODIFICADO PARA CONTORNO CERO
    estilo_iconic_chibi_cartoon = "Iconic Chibi Cartoon (Contorno Cero)"
    todos_los_estilos = [estilo_iconic_chibi_cartoon] + estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # Selectbox principal
    estilo_seleccionado = st.selectbox(
        "Estilo de la colección de llaveros",
        ["Initial of a word", "Free Style", "A partir de una imagen", "Full Name/Phrase"] + todos_los_estilos
    )

    # Campos de descripción
    descripcion_coleccion = st.text_area(
        "Descripción de la colección",
        placeholder="Describe el tema o concepto para los cuatro diseños (ej., 'cuatro animales de la selva', 'vehículos de carreras')."
    )

    nombre_personaje = st.text_input(
        "Nombres de personajes/referencias (opcional)",
        placeholder="Ej., 'Goku', 'Pikachu', 'Hello Kitty', o 'Sonic, Tails'. Separa con comas si son varios."
    )
    
    busqueda_referencia = st.checkbox(
        "Activar búsqueda intensiva de referencia (Recomendado para personajes conocidos)",
        value=False,
        help="Si se activa, se instruye a la IA a buscar imágenes de referencia del personaje para asegurar la fidelidad."
    )
    
    st.caption("Si hay 4 diseños y pones 1, 2 o 3 nombres, la IA llenará los demás con conceptos relacionados al tema general.")

    # Campos de personalización de la BASE RECTANGULAR
    st.divider()
    st.subheader("📝 Datos para Personalización (Base Vacía)")
    st.markdown("Estos datos se usan para la estética de la base, no para generar texto en la imagen. La base se generará lista para grabar un nombre.")
    
    st.text_input( 
        "Nombre/Texto de referencia (La base se genera VACÍA)",
        placeholder="Ej., 'Juan', 'Team A'. (Solo como referencia)."
    )
    
    color_base_personalizacion = st.color_picker(
        "Color de la base rectangular", 
        "#4B77BE"
    )
    
    # Campos opcionales generales
    st.divider()
    st.subheader("✨ Detalles Adicionales")
    descripcion_opcional = st.text_area(
        "Detalles adicionales para cada diseño (opcional)",
        placeholder="Añade aquí detalles específicos sobre el estilo, poses, expresiones, etc."
    )
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

    # Campos opcionales de color e ícono
    cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

# -------------------------------------------------------------------------
# PROMPTS FIJOS Y DE VARIANTE (Base de Personalización)
# -------------------------------------------------------------------------

prompt_soporte_pared = f"""Create a highly **creative, innovative, and aesthetic wall-mounted stand** to hang four decorative designs. 
The design must be a functional art piece that **reflects and complements the theme of the collection**, not just a simple hanger. 
The design must have a flat back for easy mounting, be simple and stable, with minimal overhangs, making it suitable for easy 3D printing. 
It must include four hooks or holes to hang the designs. 
{descripcion_soporte} 
The stand must be visible in its entirety. No designs should be attached yet."""

prompt_soporte_pie = f"""Create a highly **creative, innovative, and aesthetic free-standing stand** to hold four decorative designs. 
The design must be a functional art piece that **reflects and complements the theme of the collection**, not just a simple hanger. 
The design must have a wide, stable base and a vertical structure with four hooks or pegs. It must be simple and stable, with minimal overhangs, making it suitable for easy 3D printing. 
It must include four hooks or holes to hang the designs. 
{descripcion_soporte} 
The stand must be visible in its entirety. No designs should be attached yet."""

# PROMPT DE LIMPIEZA REFORZADO 
prompt_limpieza_contorno = f"""Take the attached single design and digitally clean it up. 
**Crucial Elimination Command:** Completely **remove all black or colored outlines, borders, and contour lines** from the design's perimeter. 
**Instead of a line, the border must be PERFECTLY SHARP and should transition DIRECTLY from the design's outermost color to the pure white background.** *If the design naturally has internal black lines, maintain those, but the ABSOLUTE OUTER EDGE must have NO black line or shadow.* Ensure the background is pure white (RGB 255, 255, 255). 
The final figure must look like a sharp, clean cut-out. Do not add a keyring hole."""

# PROMPT DE BASE DE PERSONALIZACIÓN (VACÍA, ALTURA REDUCIDA Y TEMÁTICA)
prompt_base_personalizacion = f"""Based on the attached **single design (already cleaned)**, generate a new image where the figure is standing on a **solid, horizontal rectangular base**. 
**Crucial:** The base must be colored **{color_base_personalizacion}** and **perfectly integrate the style and 3D relief/domed effect of the original design**. 
The rectangular base should be **wider than the figure** (approx. 1.5x the width of the figure) and **significantly shorter in height** (approx. 0.3x to 0.5x the height of the figure), proportionally balanced so as not to overwhelm the design. 
The base itself must be **stylized and themed to complement the collection concept: '{descripcion_coleccion}'**, for example, if the collection is about 'Pokemon', the base could have subtle Pokemon-related textures or shapes. 
The **front face of the base must be left completely smooth and empty**, without any molded text, numbers, or details, acting as a clean, blank surface for later text engraving. 
The entire composition (figure plus base) must have a clean, sharp, **NO external contour line** perimeter, ready for die-cut. 
Do not add a keyring hole."""

# PROMPT DXF
prompt_dxf = f"""Generate a black and white line art version of the **single design** from the attached image, optimized for DXF file conversion. 
**Maintain the exact size and aspect ratio of the attached image.** The design must have only thin, continuous outlines, no shadows, and a clean vector style. 
Crucial: Do not include any hole or attachment point in the design. 
Important: Base the output only on the provided image, do not add new elements or alter the core design. 
The background must be pure white (RGB 255, 255, 255)."""

# PROMPT SILUETA
prompt_silhouette = f"""Generate a complete, solid, and technical black silhouette of the **single design** from the attached image, optimized for DXF file conversion.
**Crucial:** The output must be a single, monolithic, **100% filled black shape** that represents **ONLY the exact outermost edge (perimeter) of the design**. 
**It must ignore and completely fill all internal lines, white spaces, or design details with solid black**, acting as a continuous mask. 
**Maintain the exact size and aspect ratio of the attached image.** The design must have absolutely no internal white spaces, lines, shadows, or gradients. 
Crucial: Do not include any hole or attachment point in the design. 
The background must be pure white (RGB 255, 255, 255)."""


# PROMPT DE SEPARACIÓN DE COLORES
prompt_separacion_colores = f"""Based on the attached **black and white line art image of the single design**, generate a **100% binary inverted, technical Fill-In version for industrial color separation**. 
**Maintain the exact size and aspect ratio of the attached image.** No gradients, no shadows, pure black and pure white only. 
The transformation must strictly adhere to a complete inversion, ensuring: 
1. **Solid Black Fills (100% Inversion):** **ALL areas that were originally white within the design's perimeter** (excluding the outer background) must now be filled with **solid, pure black**. The original figure must be 100% filled, without exception. 
2. **Minimal White Separation:** The spaces created by the original black lines must be replaced by **pure white separation lines** with an **ABSOLUTELY MINIMAL stroke thickness (1-pixel width only)**, acting only as clean, razor-thin divisions between the black shapes. The goal is the thinnest possible white line for precision manufacturing. 
3. **Outer Background:** The outer background must remain **pure white** (RGB 255, 255, 255). 
Crucial: Do not include any hole or attachment point in the design. 
The output must be a clean, binary image, ready for industrial color layering."""


prompt_presentacion_llaveros_solos = f"""Create a high-quality, professional product shot for an e-commerce platform. 
Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** The designs should be arranged in a visually interesting and appealing composition. 
The background should be a decorative setting that complements the theme of the collection, like a **minimalist studio with soft lighting** or a **natural wood table with a subtle texture**. 
The final image should highlight the vibrant colors and detailed designs, making them look like premium collectible items."""

prompt_presentacion_soporte_pared = f"""Create a high-quality, professional product shot for an e-commerce platform. 
Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** The designs should be beautifully **mounted and naturally hanging** on the previously designed **wall-mounted stand**. 
Ensure perfect integration, realistic lighting, and natural shadows. 
The background should be a decorative setting that complements the theme of the collection. 
The final image should highlight the unity of the collection and the innovative design of the stand, with all elements perfectly aligned and aesthetically appealing."""

prompt_presentacion_soporte_pie = f"""Create a high-quality, professional product shot for an e-commerce platform. 
Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** The designs should be beautifully **mounted and naturally hanging** on the previously designed **free-standing stand**. 
Ensure perfect integration, realistic lighting, and natural shadows. 
The background should be a decorative setting that complements the theme of la colección. 
The final image should highlight the unity of la colección and the innovative design of the stand, with all elements perfectly aligned and aesthetically appealing."""


# --- Botón para generar el prompt dinámico (solo la colección) ---
if st.button("Generar Prompt de Colección", type="primary"):
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Por favor, especifica la palabra para la inicial.")
    elif estilo_seleccionado == "Full Name/Phrase" and not nombre_completo:
        st.error("Por favor, especifica el nombre completo.")
    elif not descripcion_coleccion: # Se añade validación para que la descripción de la colección sea obligatoria
        st.error("Por favor, describe la colección para que la base se integre temáticamente.")
    else:
        # Generar el estilo base para el prompt
        estilo_prompt = ""
        
        # LÓGICA DE CONTORNO CERO PARA EL ESTILO CHIBI
        if estilo_seleccionado == "Iconic Chibi Cartoon (Contorno Cero)":
            estilo_prompt = (
                f"Iconic Chibi Cartoon style, **FLAT VECTOR ART**, **NO external contour lines, NO perimeter shadow, NO thick black outlines on the outer edge**. Use solid, vibrant colors. The design must be a **clean, sharp silhouette** of the figure, ready for die-cut, with shallow 3D relief or subtle domed effect, friendly expressions, simple poses. The outer border must be a **razor-clean cut** to the white background."
            )
        elif estilo_seleccionado == "A partir de una imagen":
            estilo_prompt += estilo_para_imagen_seleccionado.lower()
        elif estilo_seleccionado == "Initial of a word" and inicial_palabra:
            estilo_prompt += estilo_inicial_seleccionado.lower()
        elif estilo_seleccionado == "Full Name/Phrase" and nombre_completo:
            estilo_prompt += estilo_nombre_seleccionado.lower()
        elif estilo_seleccionado != "Free Style":
            # Para el resto de estilos, se añade un comando de limpieza
            # El .replace garantiza que cualquier llave literal se escape.
            estilo_prompt += estilo_seleccionado.lower().replace("{
