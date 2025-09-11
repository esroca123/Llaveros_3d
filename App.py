import streamlit as st

# --- Título ---
st.title("🗝️ Llavero Collection Prompt Generator")
st.markdown(
    "Crea una colección de 4 llaveros únicos, prompts derivados, soporte innovador y frases integradas en el diseño."
)

# --- Contenedor para entrada ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Selectbox de estilos
    estilos = [
        "Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit",
        "Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco",
        "Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic",
        "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore",
        "Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic",
        "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar",
        "Color Splash", "Lego", "Ghibli"
    ]
    estilo_seleccionado = st.selectbox("Selecciona el estilo de la colección", estilos)

    # Descripción y nombre completo
    descripcion_general = st.text_area(
        "Descripción general de la colección",
        placeholder="Describe la colección de llaveros, personajes, colores o temática general."
    )
    nombre_completo = st.text_input("Nombre completo (opcional)", placeholder="ej., Alexandra Pérez")
    frase_opcional = st.text_input("Frase a integrar en la imagen (opcional)", placeholder="ej., 'Feliz cumpleaños'")

    # Icono y colores
    icono_general = st.text_input("Icono o símbolo general (opcional)", placeholder="ej., rayo, luna, flor")
    cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

# --- Función para generar prompts base ---
def generar_prompt_base(variacion_texto):
    prompt = f"A creative, unique, highly detailed {estilo_seleccionado.lower()} keychain design. {variacion_texto}{descripcion_general}"
    if nombre_completo:
        prompt += f" Include the full name '{nombre_completo}' integrated elegantly into the design."
    if frase_opcional:
        prompt += f" Integrate the phrase '{frase_opcional}' beautifully into the image, matching the artistic style."
    if icono_general:
        prompt += f" Incorporate the {icono_general} icon."
    if cantidad_colores != "Cualquiera":
        prompt += f" The design must use exactly {cantidad_colores} colors."
        if colores_seleccionados:
            prompt += f" Suggested colors: {', '.join(colores_seleccionados)}."
    elif colores_seleccionados:
        prompt += f" Suggested colors: {', '.join(colores_seleccionados)}."
    return prompt

# --- Prompts derivados fijos ---
prompt_line_art = "Convert this exact attached image to black and white line art, no shadows, high contrast, white background, suitable for DXF conversion."
prompt_single_color = "Convert this exact attached image into a single-color version, each original color area filled with solid black, with no empty spaces."
prompt_silhouette = "Convert this exact attached image into a complete solid black silhouette, with no internal lines."

# --- Prompt soporte y colección ---
def prompt_soporte_func():
    return f"Design an innovative keychain holder that complements the {estilo_seleccionado.lower()} style of the collection, suitable to display 4 keychains together in a coherent and aesthetically pleasing way."

prompt_coleccion = "Display the 4 keychains mounted on the designed holder, full color, visually coherent, showing how the collection looks together."

# --- Botón generar ---
if st.button("Generar Prompts", type="primary"):

    if not descripcion_general:
        st.error("Por favor, ingresa la descripción general de la colección.")
    else:
        st.divider()
        st.subheader("✅ Prompts generados para tu colección")

        # Generar 4 llaveros
        for i in range(4):
            variacion_texto = f"Variation {i+1}: "
            prompt_base = generar_prompt_base(variacion_texto)

            # Inicializar session_state si no existe
            if f"copiado_{i}_full" not in st.session_state:
                st.session_state[f"copiado_{i}_full"] = False
            if f"copiado_{i}_dxf" not in st.session_state:
                st.session_state[f"copiado_{i}_dxf"] = False
            if f"copiado_{i}_single" not in st.session_state:
                st.session_state[f"copiado_{i}_single"] = False
            if f"copiado_{i}_silhouette" not in st.session_state:
                st.session_state[f"copiado_{i}_silhouette"] = False

            # Mostrar prompts y botones
            st.markdown(f"### 🎨 Llavero {i+1} - Prompt Full Color")
            st.text_area(f"Prompt Llavero {i+1} Full Color", prompt_base, height=180)
            if st.button(f"Copiar Llavero {i+1} Full Color"):
                st.session_state[f"copiado_{i}_full"] = True
                st.experimental_set_query_params()  # Forzar refresh
                st.success("¡Prompt copiado al portapapeles!")

            st.markdown(f"📐 Llavero {i+1} - Prompt DXF (Line Art)")
            st.text_area(f"Prompt Llavero {i+1} DXF", prompt_line_art, height=120)
            if st.button(f"Copiar Llavero {i+1} DXF"):
                st.session_state[f"copiado_{i}_dxf"] = True
                st.success("¡Prompt copiado al portapapeles!")

            st.markdown(f"🖤 Llavero {i+1} - Prompt Single Color")
            st.text_area(f"Prompt Llavero {i+1} Single Color", prompt_single_color, height=120)
            if st.button(f"Copiar Llavero {i+1} Single Color"):
                st.session_state[f"copiado_{i}_single"] = True
                st.success("¡Prompt copiado al portapapeles!")

            st.markdown(f"⬛ Llavero {i+1} - Prompt Silhouette")
            st.text_area(f"Prompt Llavero {i+1} Silhouette", prompt_silhouette, height=120)
            if st.button(f"Copiar Llavero {i+1} Silhouette"):
                st.session_state[f"copiado_{i}_silhouette"] = True
                st.success("¡Prompt copiado al portapapeles!")

            st.divider()

        # Prompt soporte
        st.markdown("### 🏗️ Prompt para soporte")
        st.text_area("Prompt Soporte", prompt_soporte_func(), height=150)
        if st.button("Copiar Prompt Soporte"):
            st.success("¡Prompt copiado al portapapeles!")

        # Prompt colección montada
        st.markdown("### 🖼️ Prompt colección montada en soporte")
        st.text_area("Prompt Colección en soporte", prompt_coleccion, height=150)
        if st.button("Copiar Prompt Colección en soporte"):
            st.success("¡Prompt copiado al portapapeles!")