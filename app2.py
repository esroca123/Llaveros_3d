import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash", "Lego", "Ghibli", "illustration", "Photorealistic", "Hyperrealistic", "Live Action Style", "Cosplay photography", "Unreal Engine 5 Render"]
    
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
        placeholder="Describe el tema o concepto (ej., 'cuatro guerreros espaciales')."
    )

    # Lógica para la opción "A partir de una imagen" (NUEVA SUB-OPCIÓN)
    estilo_para_imagen_seleccionado = None
    enfoque_referencia = None
    if estilo_seleccionado == "A partir de una imagen":
        st.info("💡 Sube la imagen de referencia directamente a tu IA generadora.")
        enfoque_referencia = st.radio(
            "Enfoque de la referencia:",
            ["Solo personajes de la imagen", "Imagen completa (composición y fondo)"],
            horizontal=True
        )
        estilo_para_imagen_seleccionado = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)

    nombre_personaje = st.text_input(
        "Nombres de personajes/referencias (opcional)",
        placeholder="Ej., 'Goku, Vegeta'. Separa con comas."
    )
    
    busqueda_referencia = st.checkbox("Activar búsqueda intensiva de referencia", value=False)

    # Lógica para "Initial of a word"
    inicial_palabra = None
    estilo_inicial_seleccionado = None
    if estilo_seleccionado == "Initial of a word":
        inicial_palabra = st.text_input("Palabra para la inicial")
        estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)

    # Lógica para "Full Name/Phrase"
    nombre_completo = None
    frase_integrada = None
    estilo_nombre_seleccionado = None
    if estilo_seleccionado == "Full Name/Phrase":
        nombre_completo = st.text_input("Nombre completo")
        frase_integrada = st.text_input("Frase opcional")
        estilo_nombre_seleccionado = st.selectbox("Estilo para el nombre", todos_los_estilos)

    # Personalización de la Base
    st.divider()
    st.subheader("📝 Personalización de la Base")
    estilo_base_personalizacion = st.text_input("Estilo específico para la base (opcional)", placeholder="Ej. base de lava")

    # Colores e iconos
    cantidad_colores = st.selectbox("Cantidad de colores", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos", colores_opciones, max_selections=4)
    icono = st.text_input("Icono o símbolo")
    descripcion_opcional = st.text_area("Detalles adicionales (poses, expresiones)")

# --- PROMPTS DE SOPORTE Y POST-PROCESADO ---
prompt_limpieza_contorno = "Take the design and clean it. REMOVE all outer shadows and outlines. Perimeter must transition directly to white background. Keep internal black lines."

prompt_base_personalizacion_template = "Place the cleaned design on a horizontal rectangular base. Base must be solid, empty on front for engraving, and match the figure's theme. No keyring holes."
if estilo_base_personalizacion:
    prompt_base_personalizacion = prompt_base_personalizacion_template + f" Base style: {estilo_base_personalizacion}."
else:
    prompt_base_personalizacion = prompt_base_personalizacion_template + " Base must match the figure's style."

prompt_dxf = "Generate black and white line art of the design. Thin continuous outlines only, no shadows. Pure white background."
prompt_silhouette = "Generate a 100% solid black silhouette of the design's outer perimeter. No internal details."

# --- BOTÓN DE GENERACIÓN ---
try:
    if st.button("Generar Prompt de Colección", type="primary"):
        if not descripcion_coleccion:
            st.error("Por favor, describe la colección.")
        else:
            # Definir estilo_prompt
            if estilo_seleccionado == "Iconic Chibi Cartoon (Contorno Cero)":
                estilo_prompt = "Iconic Chibi, flat vector, no outer outlines, razor-clean edges"
            elif estilo_seleccionado == "A partir de una imagen":
                estilo_prompt = estilo_para_imagen_seleccionado.lower()
            elif estilo_seleccionado == "Initial of a word":
                estilo_prompt = estilo_inicial_seleccionado.lower()
            elif estilo_seleccionado == "Full Name/Phrase":
                estilo_prompt = estilo_nombre_seleccionado.lower()
            else:
                estilo_prompt = estilo_seleccionado.lower()

            # CONSTRUCCIÓN DEL PROMPT BASE (Optimizado y Directo)
            prompt_coleccion_base = f"""Generate 4 vibrant designs in **{estilo_prompt} style**, 2x2 grid.
**CRITICAL STYLE:** Use **SOLID FLAT COLORS** only. **NO gradients, NO soft shading, NO color fading**.
**VOLUME:** Define all muscles, depth, and details exclusively with **sharp, crisp black internal lines**.
**ORIGINALITY:** Unique creations inspired by the theme. **NO direct replication of copyrighted characters or logos.**
**CLEANLINESS:** No outer borders, no surrounding frames, no external shadows. Pure white background (RGB 255, 255, 255).
**FORMAT:** Frontal view, no rings or holes. High-quality collectible look.
**THEME:** '{descripcion_coleccion}'."""

            # Inyección de Referencia de Imagen
            if estilo_seleccionado == "A partir de una imagen":
                if enfoque_referencia == "Solo personajes de la imagen":
                    prompt_coleccion_base += " Extract ONLY characters from reference, ignore its background."
                else:
                    prompt_coleccion_base += " Replicate the full composition and atmosphere of the reference."

            # Inyección de Personajes/Nombres
            if nombre_personaje:
                prompt_coleccion_base += f" Designs based on: {nombre_personaje}."
                if busqueda_referencia:
                    prompt_coleccion_base += " Search high-fidelity references for canonical details."

            # Otros detalles
            if icono: prompt_coleccion_base += f" Include {icono} symbol."
            if cantidad_colores != "Cualquiera": prompt_coleccion_base += f" Use max {cantidad_colores} colors."
            if colores_seleccionados: prompt_coleccion_base += f" Colors: {', '.join(colores_seleccionados)}."
            if descripcion_opcional: prompt_coleccion_base += f" Extra details: {descripcion_opcional}."

            st.divider()
            st.subheader("✅ Prompt de Colección Generado:")
            st.code(prompt_coleccion_base, language="markdown")

except Exception as e:
    st.error(f"Error: {e}")

# --- SECCIÓN DE PROMPTS SECUNDARIOS ---
st.divider()
st.subheader("💡 Pasos Siguientes")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Paso 2: Limpieza**")
    st.code(prompt_limpieza_contorno)
with col2:
    st.markdown("**Paso 3: Base**")
    st.code(prompt_base_personalizacion)

st.markdown("**Producción (DXF y Silueta)**")
st.code(f"DXF: {prompt_dxf}\n\nSILUETA: {prompt_silhouette}")
