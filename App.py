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
    
    # NUEVA CASILLA PARA EL ESTILO DE LA BASE
    estilo_base_personalizacion = st.text_input(
        "Estilo específico para la base (opcional)",
        placeholder="Ej., 'base de hierba', 'base de nube', 'base minimalista gris'. Si se deja vacío, la IA intentará coincidir el estilo de la figura."
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

# PROMPT DE BASE DE PERSONALIZACIÓN (OPTIMIZADO Y SIN SELECCIÓN DE COLOR POR EL USUARIO)
prompt_base_personalizacion_template = """Based on the attached **single design (already cleaned)**, generate a new image where the figure is standing on a **solid, horizontal rectangular base**. 
**Crucial:** The figure must **NOT be modified or altered** in any way; simply place it on top of the base. 
The base must be **beautiful, eye-catching, and its color(s) coherent and harmonious with the colors of the figure**. It should also have a **3D relief or subtle domed effect** to match the figure's style. 
The rectangular base should be approximately **1.5 times the width of the figure** and **0.5 times the height of the figure**, maintaining a balanced proportion so as not to overwhelm the design. 
The front face of the base must be left **completely smooth and empty**, without any molded text, numbers, or details, acting as a clean, blank surface for later text engraving. 
The entire composition (figure plus base) must have a clean, sharp, **NO external contour line** perimeter, ready for die-cut. 
Do not add a keyring hole."""

# Lógica para aplicar el estilo de la base (mantiene la opción de input de estilo)
if estilo_base_personalizacion:
    prompt_base_personalizacion = prompt_base_personalizacion_template + f" The base must be in a '{estilo_base_personalizacion}' style."
else:
    prompt_base_personalizacion = prompt_base_personalizacion_template + " The base must perfectly adapt the style of the figure placed on top of it."

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
The background should be a decorative setting that complements the theme of la colección, like a **minimalist studio with soft lighting** or a **natural wood table with a subtle texture**. 
The final image should highlight the vibrant colors and detailed designs, making them look like premium collectible items."""

prompt_presentacion_soporte_pared = f"""Create a high-quality, professional product shot for an e-commerce platform. 
Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** The designs should be beautifully **mounted and naturally hanging** on the previously designed **wall-mounted stand**. 
Ensure perfect integration, realistic lighting, and natural shadows. 
The background should be a decorative setting that complements the theme of la colección. 
The final image should highlight the unity of la colección and the innovative design of the stand, with all elements perfectly aligned and aesthetically appealing."""

prompt_presentacion_soporte_pie = f"""Create a high-quality, professional product shot for an e-commerce platform. 
Show the four decorative designs from the attached image, each with a realistic **metallic keyring and a chain attached.** The designs should be beautifully **mounted and naturally hanging** on the previously designed **free-standing stand**. 
Ensure perfect integration, realistic lighting, and natural shadows. 
The background should be a decorative setting that complements the theme of la colección. 
The final image should highlight the unity of la colección and the innovative design of the stand, with all elements perfectly aligned and aesthetically appealing."""


# --- Botón para generar el prompt dinámico (solo la colección) ---
# He añadido un try-except general para capturar cualquier error inesperado dentro del botón.
# Esto no soluciona la causa raíz, pero puede ayudar a identificar si hay un error en tiempo de ejecución.
try:
    if st.button("Generar Prompt de Colección", type="primary"):
        # Verificaciones moved dentro del bloque para asegurar que las variables estén definidas
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
                # Asegurarse que estilo_inicial_seleccionado no sea None antes de .lower()
                estilo_prompt += estilo_inicial_seleccionado.lower() if estilo_inicial_seleccionado else ""
            elif estilo_seleccionado == "Full Name/Phrase" and nombre_completo:
                # Asegurarse que estilo_nombre_seleccionado no sea None antes de .lower()
                estilo_prompt += estilo_nombre_seleccionado.lower() if estilo_nombre_seleccionado else ""
            elif estilo_seleccionado != "Free Style":
                # Para el resto de estilos, se añade un comando de limpieza
                estilo_prompt += f"{estilo_seleccionado.lower().replace('{', '{{').replace('}', '}}')}, **NO external contour lines or outer shadow**"
            else:
                estilo_prompt += "modern"

            # PROMPT DE COLECCIÓN BASE
            prompt_coleccion_base = f"""Generate four highly detailed, vibrant, and full-color decorative art designs in a **{estilo_prompt} style**. 
Crucial: **Strictly adhere to this style**, presented together in a 2x2 grid. 
**No outer border, no surrounding frame, no external shadow around the entire composition.** The designs must have a sense of physical material and **shallow 3D relief or subtle domed effect** when viewed from the front (frontal isometric view). 
Ensure **soft, realistic shadows and highlights** that create a sense of depth and volume, preventing the final image from looking like a flat, digital print. 
Each design is a unique, stylized figure or symbol, where the entire piece itself is the main body of the art. 
The design must be visually strong, clear, and perfectly sized for a collectible item or keychain (approx. 5cm on its longest side). 
The image must show the designs ONLY, with ABSOLUTELY NO attached rings, chains, hooks, or holes. 
The designs should look like high-quality, stylized collectible pieces, with vibrant colors and sharp details. 
The background must be pure white (RGB 255, 255, 255). 
The overall theme is: '{descripcion_coleccion}'."""
            
            # -------------------------------------------------------------------------
            # LÓGICA DE REFERENCIA Y OPCIONES ADICIONALES
            # -------------------------------------------------------------------------
            
            if nombre_personaje:
                personajes_referencia = f"""The designs represent different poses or variations of the following characters/entities: '{nombre_personaje}'. Ensure the figures are easily recognizable and faithful to the original character's design."""
                
                if busqueda_referencia:
                    personajes_referencia += " **IMPORTANT:** Before generating, you must perform a high-fidelity reference search for each specified character to ensure maximum visual fidelity, correct proportions, and canonical color palette. The output MUST reflect these authentic details."
                
                prompt_coleccion_base += personajes_referencia

            # Lógica para Referencia de Imagen Externa
            if estilo_seleccionado == "A partir de una imagen":
                prompt_coleccion_base += f" The designs are a stylized interpretation of the **attached reference image**, applying the chosen style. "
            
            # Lógica para Nombre/Frase
            if estilo_seleccionado == "Full Name/Phrase" and nombre_completo:
                prompt_coleccion_base += f" The designs are based on the full name '{nombre_completo}'. "
                if frase_integrada:
                    prompt_coleccion_base += f"The phrase '{frase_integrada}' is beautifully and creatively integrated into the design."
            
            # Lógica de Opciones Adicionales (Colores, Iconos, Texto)
            if icono:
                prompt_coleccion_base += f" Incorporate the {icono} icon."
            if texto_opcional:
                prompt_coleccion_base += f" Include the text: '{texto_opcional}'."
            if cantidad_colores != "Cualquiera":
                prompt_coleccion_base += f" The designs must use exactly {cantidad_colores} colors."
                if colores_seleccionados:
                    colores_str = ", ".join(colores_seleccionados)
                    prompt_coleccion_base += f" Suggested colors: {colores_str}."
            elif colores_seleccionados: 
                colores_str = ", ".join(colores_seleccionados)
                prompt_coleccion_base += f" Suggested colors: {colores_str}."
                
            # Añadir detalles opcionales al final si existen
            if descripcion_opcional:
                prompt_coleccion_base += f" Additional details: {descripcion_opcional}."

            st.divider()
            st.subheader("✅ Tu prompt está listo:")
            st.markdown("### 1. Prompt para la creación de tu colección (Paso 1)")
            st.code(str(prompt_coleccion_base), language="markdown")
except Exception as e:
    st.error(f"Se ha producido un error al generar el prompt. Por favor, revisa tus entradas. Error: {e}")


# --- Aquí se muestran todos los prompts fijos (siempre visibles) ---
st.divider()
st.subheader("💡 Prompts de Flujo de Trabajo (Para usar después del Paso 1)")
st.markdown("Usa la imagen LIMPIA (cortada individualmente del Paso 1) para los siguientes prompts.")


st.markdown("### 2. Prompt de Limpieza y Preparación (Paso 2)")
st.markdown("Usa este prompt si tu imagen aún tiene una sombra o contorno no deseado alrededor de toda la figura.")
st.code(prompt_limpieza_contorno, language="markdown")

st.markdown("### 3. Prompts de Variantes de Producción (Paso 3)")
st.markdown("Usa la imagen LIMPIA (Paso 2) para generar las variantes de fabricación y personalización.")

st.markdown("#### 3.a. Prompt para la Variante de Base Personalizada (¡BASE VACÍA, TEMÁTICA Y BAJA!)")
st.info(f"La base rectangular se generará VACÍA. Si especificaste un estilo de base, se aplicará; de lo contrario, la IA intentará coincidir el estilo de la figura. El color será coherente y armonioso con la figura. Lista para agregar texto en el software de diseño.")
st.code(prompt_base_personalizacion, language="markdown")


st.markdown("#### 3.b. Prompt para versión DXF (Contorno Lineal)")
st.code(prompt_dxf, language="markdown")
st.markdown("#### 3.c. Prompt para versión Silueta (Máscara Monolítica)")
st.code(prompt_silhouette, language="markdown")
st.markdown("#### 3.d. Prompt para versión Separación de Colores (Relleno Binario)")
st.code(prompt_separacion_colores, language="markdown")

st.markdown("### 4. Prompts para el Soporte (Paso 4)")
st.markdown("Utiliza la imagen generada en el paso 1 (o la versión Limpia) para crear un soporte para tus diseños. Elige una de las siguientes opciones:")
st.markdown("#### Colgadero de Pared")
st.code(prompt_soporte_pared, language="markdown")
st.markdown("#### Soporte de Pie")
st.code(prompt_soporte_pie, language="markdown")

st.markdown("### 5. Prompts para la Presentación Final (Paso 5)")
st.markdown("Utiliza las imágenes de los diseños y el soporte para crear renders de alta calidad.")
st.markdown("#### Prompt para Presentación de Llaveros Solos")
st.code(prompt_presentacion_llaveros_solos, language="markdown")
st.markdown("#### Prompt para Presentación con Soporte de Pared")
st.code(prompt_presentacion_soporte_pared, language="markdown")
st.markdown("#### Prompt para Presentación con Soporte de Pie")
st.code(prompt_presentacion_soporte_pie, language="markdown")
