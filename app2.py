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

    # --- SELECCIÓN DE ESTILOS (SISTEMA DUAL) ---
    col_estilo1, col_estilo2 = st.columns(2)
    
    with col_estilo1:
        estilo_seleccionado = st.selectbox(
            "Estilo Principal",
            ["Initial of a word", "Free Style", "A partir de una imagen", "Full Name/Phrase"] + todos_los_estilos
        )

    with col_estilo2:
        estilo_secundario = st.selectbox(
            "Segundo Estilo (Opcional)",
            ["Ninguno"] + todos_los_estilos
        )

    # Variables de control
    texto_ingresado = ""
    tipo_letras = None
    estilo_base_personalizado = None
    enfoque_referencia = None
    estilo_para_imagen_seleccionado = None

    # Lógica unificada para Referencia de Imagen
    if estilo_seleccionado == "A partir de una imagen":
        st.info("💡 Sube la imagen de referencia. Puedes elegir si quieres personajes o un letrero basado en ella.")
        enfoque_referencia = st.radio(
            "¿Qué quieres replicar de la imagen?",
            ["Solo personajes", "Imagen completa", "Estilo de letrero/Texto"],
            horizontal=True
        )
        
        # Si es estilo de letrero, pedimos el nuevo texto
        if enfoque_referencia == "Estilo de letrero/Texto":
            texto_ingresado = st.text_input("Nuevo texto para el letrero (basado en la imagen):")
            tipo_letras = st.radio("Estructura:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])
        
        estilo_para_imagen_seleccionado = st.selectbox("Estilo artístico adicional para la imagen:", todos_los_estilos)

    # Lógica estándar para Letras/Nombres (sin imagen)
    if estilo_seleccionado in ["Initial of a word", "Full Name/Phrase"]:
        texto_ingresado = st.text_input("Escribe el texto (Nombre, frase o inicial):")
        tipo_letras = st.radio(
            "Estructura del llavero:",
            ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"]
        )
        estilo_base_personalizado = st.selectbox("Estilo base para el texto", todos_los_estilos)

    # Campos de descripción general
    label_descripcion = "Descripción de la colección (Opcional)" if estilo_seleccionado in ["A partir de una imagen", "Full Name/Phrase", "Initial of a word"] else "Descripción de la colección (Obligatorio)"
    descripcion_coleccion = st.text_area(label_descripcion, placeholder="Describe el tema o concepto.")

    # Personalización de la Base y Detalles
    st.divider()
    col_colores, col_detalles = st.columns(2)
    with col_colores:
        cantidad_colores = st.selectbox("Cantidad de colores", ["Cualquiera"] + list(range(1, 5)))
        colores_seleccionados = st.multiselect("Colores sugeridos", ["red", "blue", "green", "yellow", "black", "white", "purple", "pink", "orange"])
    with col_detalles:
        descripcion_opcional = st.text_area("Requerimientos especiales")

# --- BOTÓN DE GENERACIÓN ---
try:
    if st.button("Generar Prompt de Colección", type="primary"):
        # 1. Definir Estilo Final
        if estilo_seleccionado == "Iconic Chibi Cartoon (Contorno Cero)":
            estilo_final = "Iconic Chibi, flat vector, no outer outlines, razor-clean edges"
        elif estilo_seleccionado == "A partir de una imagen":
            estilo_final = estilo_para_imagen_seleccionado.lower()
        elif estilo_seleccionado in ["Initial of a word", "Full Name/Phrase"]:
            estilo_final = estilo_base_personalizado.lower()
        else:
            estilo_final = estilo_seleccionado.lower()

        if estilo_secundario != "Ninguno":
            estilo_final = f"hibrid fusion of {estilo_final} and {estilo_secundario.lower()}"

        # 2. Cantidad de diseños
        es_imagen_completa = (estilo_seleccionado == "A partir de una imagen" and enfoque_referencia == "Imagen completa")
        cantidad_disenos = "one single design" if es_imagen_completa else "four vibrant designs in a 2x2 grid"

        # CONSTRUCCIÓN DEL PROMPT
        prompt_coleccion_base = f"""Generate **{cantidad_disenos}** following the **{estilo_final} style**.
**CRITICAL STYLE:** Use **SOLID FLAT COLORS** only. **NO gradients, NO soft shading**.
**VOLUME:** Define depth and details exclusively with **sharp, crisp black internal lines**.
**CLEANLINESS:** No outer shadows. Pure white background (RGB 255, 255, 255).
**FORMAT:** Frontal view, no rings or holes. High-quality collectible look."""

        # LÓGICA DE TEXTO Y REFERENCIA DE IMAGEN
        if texto_ingresado:
            layout_letras = "SINGLE HORIZONTAL LINE, interconnected, no stacking"
            dim_letras = "fit within a max bounding box of 8cm x 4cm, proportional to name length"
            
            if estilo_seleccionado == "A partir de una imagen" and enfoque_referencia == "Estilo de letrero/Texto":
                prompt_coleccion_base += f"""
**ULTIMATE STYLE REFERENCE:** Use the attached image as the absolute guide for typography style, color palette, and aesthetic.
**TASK:** Create a NEW sign with the text: '{texto_ingresado}'.
**STRUCTURE:** {layout_letras}. {dim_letras}. {"Stand-alone letters, no background" if tipo_letras == "Solo las letras (Sin fondo)" else "Integrated into a decorative plaque"}.
Do not copy the original text from the image, ONLY its style and visual essence."""
            else:
                prompt_coleccion_base += f"\n**CORE SUBJECT:** Typography for: '{texto_ingresado}'.\n**STRUCTURE:** {layout_letras}. {dim_letras}. {'No background' if tipo_letras == 'Solo las letras (Sin fondo)' else 'With plaque'}."

        # REFERENCIA DE IMAGEN PARA PERSONAJES/ESCENA
        if estilo_seleccionado == "A partir de una imagen":
            if enfoque_referencia == "Solo personajes":
                prompt_coleccion_base += "\n**MANDATORY REFERENCE:** Extract ONLY characters from attached image."
            elif enfoque_referencia == "Imagen completa":
                prompt_coleccion_base += "\n**ULTIMATE REFERENCE COMMAND:** Use the attached image as a structural template. Maintain EXACT composition."

        if descripcion_coleccion: prompt_coleccion_base += f"\n**THEME:** '{descripcion_coleccion}'."
        if cantidad_colores != "Cualquiera": prompt_coleccion_base += f"\n**COLORS:** Max {cantidad_colores}."
        if colores_seleccionados: prompt_coleccion_base += f"\n**PALETTE:** {', '.join(colores_seleccionados)}."
        if descripcion_opcional: prompt_coleccion_base += f"\n**SPECIAL:** {descripcion_opcional}."

        st.divider()
        st.subheader("✅ Prompt de Colección Generado:")
        st.code(prompt_coleccion_base, language="markdown")

except Exception as e:
    st.error(f"Error: {e}")
