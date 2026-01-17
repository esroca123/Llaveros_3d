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

    # Lógica para la opción "A partir de una imagen"
    estilo_para_imagen_seleccionado = None
    enfoque_referencia = None
    if estilo_seleccionado == "A partir de una imagen":
        st.info("💡 Sube la imagen de referencia. 'Imagen completa' obligará a la IA a calcar la estructura original.")
        enfoque_referencia = st.radio(
            "Enfoque de la referencia:",
            ["Solo personajes de la imagen", "Imagen completa (composición y fondo)"],
            horizontal=True
        )
        estilo_para_imagen_seleccionado = st.selectbox("Estilo artístico para la imagen:", todos_los_estilos)

    # Lógica para "Initial of a word" / "Full Name/Phrase" (CON NUEVA OPCIÓN DE FONDO)
    texto_ingresado = ""
    estilo_texto_base = None
    tipo_letras = None
    if estilo_seleccionado in ["Initial of a word", "Full Name/Phrase"]:
        texto_ingresado = st.text_input("Escribe el texto (Nombre, frase o inicial):")
        tipo_letras = st.radio(
            "Estructura del llavero:",
            ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"],
            help="Selecciona 'Solo las letras' para que el llavero tenga la forma física del nombre."
        )
        estilo_texto_base = st.selectbox("Estilo base para el texto", todos_los_estilos)

    # Campos de descripción general
    label_descripcion = "Descripción de la colección (Opcional)" if estilo_seleccionado in ["A partir de una imagen", "Full Name/Phrase", "Initial of a word"] else "Descripción de la colección (Obligatorio)"
    descripcion_coleccion = st.text_area(
        label_descripcion,
        placeholder="Describe el tema o concepto (ej. inspirado en galaxias)."
    )

    nombre_personaje = st.text_input("Personajes adicionales (opcional)")

    # Personalización de la Base
    st.divider()
    st.subheader("📝 Personalización de la Base")
    estilo_base_personalizacion = st.text_input("Estilo para la base (opcional)")

    # Detalles finales
    cantidad_colores = st.selectbox("Cantidad de colores", ["Cualquiera"] + list(range(1, 5)))
    colores_seleccionados = st.multiselect("Colores sugeridos", ["red", "blue", "green", "yellow", "black", "white", "purple", "pink", "orange"])
    descripcion_opcional = st.text_area("Requerimientos especiales")

# --- PROMPTS DE SOPORTE ---
prompt_limpieza_contorno = "Clean the design. REMOVE outer shadows/outlines. Sharp perimeter edges. Keep internal black lines."
prompt_base_personalizacion_template = "Place the design on a horizontal rectangular base. Solid, empty front. Match theme."

# --- BOTÓN DE GENERACIÓN ---
try:
    if st.button("Generar Prompt de Colección", type="primary"):
        if estilo_seleccionado in ["Full Name/Phrase", "Initial of a word"] and not texto_ingresado:
            st.error("Por favor, escribe el texto.")
        elif not descripcion_coleccion and estilo_seleccionado not in ["A partir de una imagen", "Full Name/Phrase", "Initial of a word"]:
            st.error("Por favor, describe la colección.")
        else:
            # 1. Definir Estilo Base
            if estilo_seleccionado == "Iconic Chibi Cartoon (Contorno Cero)":
                estilo_final = "Iconic Chibi, flat vector, no outer outlines, razor-clean edges"
            elif estilo_seleccionado == "A partir de una imagen":
                estilo_final = estilo_para_imagen_seleccionado.lower()
            elif estilo_seleccionado in ["Initial of a word", "Full Name/Phrase"]:
                estilo_final = estilo_texto_base.lower()
            elif estilo_seleccionado == "Free Style":
                estilo_final = "creative and modern"
            else:
                estilo_final = estilo_seleccionado.lower()

            # 2. Mezclar con Estilo Secundario si existe
            if estilo_secundario != "Ninguno":
                estilo_sec_nombre = "Iconic Chibi, flat vector, no outer outlines" if estilo_secundario == estilo_iconic_chibi_cartoon else estilo_secundario.lower()
                estilo_final = f"hibrid fusion of {estilo_final} and {estilo_sec_nombre}"

            # 3. Cantidad de diseños
            es_imagen_completa = (estilo_seleccionado == "A partir de una imagen" and enfoque_referencia == "Imagen completa (composición y fondo)")
            cantidad_disenos = "one single design" if es_imagen_completa else "four vibrant designs in a 2x2 grid"

            # CONSTRUCCIÓN DEL PROMPT BASE
            prompt_coleccion_base = f"""Generate **{cantidad_disenos}** strictly following the **{estilo_final} style**.
**CRITICAL STYLE:** Use **SOLID FLAT COLORS** only. **NO gradients, NO soft shading, NO color fading**.
**VOLUME:** Define all depth and details exclusively with **sharp, crisp black internal lines**.
**CLEANLINESS:** No outer borders, no surrounding frames, no external shadows. Pure white background (RGB 255, 255, 255).
**FORMAT:** Frontal view, no rings or holes. High-quality collectible look."""

            # LÓGICA DE TEXTO Y ESTRUCTURA (SOLO LETRAS VS FONDO)
            if estilo_seleccionado in ["Full Name/Phrase", "Initial of a word"]:
                if tipo_letras == "Solo las letras (Sin fondo)":
                    prompt_coleccion_base += f"""
**CORE SUBJECT:** The design is ONLY the typography of the text: '{texto_ingresado}'. 
**STRUCTURE:** The text must be stand-alone. No background plates, no backing shapes, no rectangles behind. 
The silhouette of the design must follow the outer edges of the letters. The letters must be interconnected to form a single solid piece."""
                else:
                    prompt_coleccion_base += f"""
**CORE SUBJECT:** The text '{texto_ingresado}' integrated into a decorative background or plaque."""

            # INSTRUCCIÓN DE REFERENCIA
            if estilo_seleccionado == "A partir de una imagen":
                if enfoque_referencia == "Solo personajes de la imagen":
                    prompt_coleccion_base += "\n**MANDATORY REFERENCE:** Extract ONLY characters from attached image."
                else:
                    prompt_coleccion_base += "\n**ULTIMATE REFERENCE COMMAND:** Use the attached image as a structural template. Maintain EXACT composition."
            
            if descripcion_coleccion:
                prompt_coleccion_base += f"\n**THEME:** '{descripcion_coleccion}'."

            # Detalles finales
            if cantidad_colores != "Cualquiera": prompt_coleccion_base += f"\n**COLORS:** Max {cantidad_colores}."
            if colores_seleccionados: prompt_coleccion_base += f"\n**PALETTE:** {', '.join(colores_seleccionados)}."
            if descripcion_opcional: prompt_coleccion_base += f"\n**SPECIAL:** {descripcion_opcional}."

            st.divider()
            st.subheader("✅ Prompt de Colección Generado:")
            st.code(prompt_coleccion_base, language="markdown")

except Exception as e:
    st.error(f"Error: {e}")
