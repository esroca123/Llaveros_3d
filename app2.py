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

    # Lógica para la opción "A partir de una imagen" (SUB-OPCIONES)
    estilo_para_imagen_seleccionado = None
    enfoque_referencia = None
    if estilo_seleccionado == "A partir de una imagen":
        st.info("💡 Sube la imagen de referencia. 'Imagen completa' generará un solo diseño fiel a la original.")
        enfoque_referencia = st.radio(
            "Enfoque de la referencia:",
            ["Solo personajes de la imagen", "Imagen completa (composición y fondo)"],
            horizontal=True
        )
        estilo_para_imagen_seleccionado = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)

    # Campos de descripción
    label_descripcion = "Descripción de la colección (Opcional)" if estilo_seleccionado == "A partir de una imagen" else "Descripción de la colección (Obligatorio)"
    descripcion_coleccion = st.text_area(
        label_descripcion,
        placeholder="Describe el tema o concepto."
    )

    nombre_personaje = st.text_input("Nombres de personajes (opcional)")
    busqueda_referencia = st.checkbox("Activar búsqueda intensiva de referencia", value=False)

    # Lógica para "Initial of a word"
    inicial_palabra = None
    estilo_inicial_seleccionado = None
    if estilo_seleccionado == "Initial of a word":
        inicial_palabra = st.text_input("Palabra para la inicial")
        estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)

    # Lógica para "Full Name/Phrase"
    nombre_completo = None
    estilo_nombre_seleccionado = None
    if estilo_seleccionado == "Full Name/Phrase":
        nombre_completo = st.text_input("Nombre completo / Frase")
        estilo_nombre_seleccionado = st.selectbox("Estilo para el nombre", todos_los_estilos)

    # Personalización de la Base
    st.divider()
    st.subheader("📝 Personalización de la Base")
    estilo_base_personalizacion = st.text_input("Estilo para la base (opcional)")

    # Detalles finales
    cantidad_colores = st.selectbox("Cantidad de colores", ["Cualquiera"] + list(range(1, 5)))
    colores_seleccionados = st.multiselect("Colores sugeridos", ["red", "blue", "green", "yellow", "black", "white", "purple", "pink", "orange"])
    descripcion_opcional = st.text_area("Requerimientos especiales")

# --- PROMPTS DE POST-PROCESADO ---
prompt_limpieza_contorno = "Clean the design. REMOVE outer shadows/outlines. Sharp perimeter edges. Keep internal black lines."
prompt_base_personalizacion_template = "Place the design on a horizontal rectangular base. Solid, empty front. Match theme."
prompt_dxf = "B&W line art. Thin outlines, no shadows. White background."
prompt_silhouette = "100% solid black silhouette of the outer perimeter."

# --- BOTÓN DE GENERACIÓN ---
try:
    if st.button("Generar Prompt de Colección", type="primary"):
        if not descripcion_coleccion and estilo_seleccionado != "A partir de una imagen":
            st.error("Por favor, describe la colección.")
        else:
            # Definir estilo y cantidad de imágenes
            cantidad_disenos = "one single design" if (estilo_seleccionado == "A partir de una imagen" and enfoque_referencia == "Imagen completa (composición y fondo)") else "four vibrant designs in a 2x2 grid"
            
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

            # CONSTRUCCIÓN DEL PROMPT BASE
            prompt_coleccion_base = f"""Generate **{cantidad_disenos}** in **{estilo_prompt} style**.
**CRITICAL STYLE:** Use **SOLID FLAT COLORS** only. **NO gradients, NO soft shading, NO color fading**.
**VOLUME:** Define all muscles, depth, and details exclusively with **sharp, crisp black internal lines**.
**ORIGINALITY:** Unique interpretation. **NO direct replication of copyrighted logos or branding.**
**CLEANLINESS:** No outer borders, no surrounding frames, no external shadows. Pure white background (RGB 255, 255, 255).
**FORMAT:** Frontal view, no rings or holes. High-quality collectible look."""

            # Inyección de Referencia
            if estilo_seleccionado == "A partir de una imagen":
                if enfoque_referencia == "Solo personajes de la imagen":
                    prompt_coleccion_base += " **REF:** Extract ONLY characters, create 4 separate designs. Ignore background."
                else:
                    prompt_coleccion_base += " **REF:** Replicate the EXACT composition, poses, and atmosphere of the reference image, but transform it into the selected style. Generate only ONE main scene."
            
            if descripcion_coleccion:
                prompt_coleccion_base += f" **THEME:** '{descripcion_coleccion}'."
            
            if nombre_personaje:
                prompt_coleccion_base += f" **CHARACTERS:** {nombre_personaje}."
                if busqueda_referencia:
                    prompt_coleccion_base += " Use high-fidelity canonical references."

            # Detalles finales
            if cantidad_colores != "Cualquiera": prompt_coleccion_base += f" Use {cantidad_colores} colors max."
            if colores_seleccionados: prompt_coleccion_base += f" Colors: {', '.join(colores_seleccionados)}."
            if descripcion_opcional: prompt_coleccion_base += f" Special requirements: {descripcion_opcional}."

            st.divider()
            st.subheader("✅ Prompt Generado:")
            st.code(prompt_coleccion_base, language="markdown")

except Exception as e:
    st.error(f"Error: {e}")
