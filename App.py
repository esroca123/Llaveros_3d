import streamlit as st

# --- Función para copiar al portapapeles usando JS ---
def copiar_al_portapapeles(texto):
    st.write(f'<script>navigator.clipboard.writeText(`{texto}`).then(()=>{{alert("¡Prompt copiado al portapapeles!")}})</script>', unsafe_allow_html=True)

# --- Título ---
st.title("🗝️ Llavero Collection Prompt Generator")
st.markdown(
    "Crea una colección de 4 llaveros 3D únicos, con prompts derivados y soporte innovador."
)

# --- Entrada de datos ---
st.subheader("🛠️ Personaliza tu colección de llaveros")

# Estilos
estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash", "Lego", "Ghibli"]
todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

# Selectbox principal
estilo_seleccionado = st.selectbox(
    "Estilo del llavero",
    ["Initial of a word", "Free Style", "A partir de una imagen"] + todos_los_estilos
)

# Inputs comunes
descripcion_general = st.text_area("Descripción general de la colección", placeholder="Describe la colección de llaveros, personajes, colores o temática general.")
nombre_completo = st.text_input("Nombre completo (opcional)", placeholder="ej., Alexandra Pérez")
frase_opcional = st.text_input("Frase a integrar en la imagen (opcional)", placeholder="ej., 'Feliz cumpleaños'")
icono_general = st.text_input("Icono o símbolo general (opcional)", placeholder="ej., rayo, luna, flor")
cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

# Inputs específicos
inicial_palabra = None
estilo_inicial_seleccionado = None
if estilo_seleccionado == "Initial of a word":
    inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej., Alexandra")
    estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)

estilo_para_imagen_seleccionado = None
if estilo_seleccionado == "A partir de una imagen":
    st.markdown("La imagen de referencia debe subirse a la IA de tu elección por separado.")
    estilo_para_imagen_seleccionado = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)

# --- Función para generar prompts base ---
def generar_prompt_base(variacion_texto, llavero_num):
    prompt = ""
    if estilo_seleccionado == "Initial of a word" and inicial_palabra:
        prompt = f"A 3D printed keychain design based on the letter '{inicial_palabra.upper()[0]}' in a {estilo_inicial_seleccionado.lower()} style, with low relief suitable for 3D printing. {variacion_texto}{descripcion_general}"
    elif estilo_seleccionado == "A partir de una imagen":
        prompt = f"A 3D printed keychain design in {estilo_para_imagen_seleccionado.lower()} style based on an attached reference image, low relief suitable for 3D printing. {variacion_texto}{descripcion_general}"
    else:
        prompt = f"A 3D printed keychain design in {estilo_seleccionado.lower()} style, low relief suitable for 3D printing. {variacion_texto}{descripcion_general}"
    
    if nombre_completo:
        prompt += f" Include the full name '{nombre_completo}' integrated elegantly into the design."
    if frase_opcional:
        prompt += f" Integrate the phrase '{frase_opcional}' beautifully into the image, matching the artistic style."
    if icono_general:
        prompt += f" Incorporate the {icono_general} icon."
    if cantidad_colores != "Cualquiera":
        prompt += f" Use exactly {cantidad_colores} colors."
        if colores_seleccionados:
            prompt += f" Suggested colors: {', '.join(colores_seleccionados)}."
    elif colores_seleccionados:
        prompt += f" Suggested colors: {', '.join(colores_seleccionados)}."
    
    # Agregar soporte para colgar
    prompt += " Include a keyring hole and make sure the design is stable for 3D printing."
    
    return prompt

# --- Prompts derivados ---
prompt_line_art = "Convert this exact attached image to black and white line art, no shadows, high contrast, white background, suitable for DXF conversion."
prompt_single_color = "Convert this exact attached image into a single-color version, each original color area filled with solid black, no empty spaces."
prompt_silhouette = "Convert this exact attached image into a complete solid black silhouette, with no internal lines."

# Prompt soporte y colección
def prompt_soporte_func():
    return f"Design an innovative 3D printed keychain holder that complements the {estilo_seleccionado.lower()} style of the collection, suitable to display 4 keychains together in a coherent and aesthetically pleasing way."

prompt_coleccion = "Display the 4 keychains mounted on the designed holder, full color, visually coherent, showing how the collection looks together."

# --- Botón generar ---
if st.button("Generar Prompts", type="primary"):
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Por favor, ingresa la palabra para la inicial.")
    elif not descripcion_general:
        st.error("Por favor, ingresa la descripción general de la colección.")
    else:
        st.divider()
        st.subheader("✅ Prompts generados para tu colección")

        # Generar 4 llaveros
        for i in range(4):
            variacion_texto = f"Variation {i+1}: "
            prompt_base = generar_prompt_base(variacion_texto, i+1)

            st.markdown(f"### 🎨 Llavero {i+1} - Prompt Full Color")
            st.text_area(f"Prompt Llavero {i+1} Full Color", prompt_base, height=180)
            if st.button(f"Copiar Llavero {i+1} Full Color"):
                copiar_al_portapapeles(prompt_base)

            st.markdown(f"📐 Llavero {i+1} - Prompt DXF (Line Art)")
            st.text_area(f"Prompt Llavero {i+1} DXF", prompt_line_art, height=120)
            if st.button(f"Copiar Llavero {i+1} DXF"):
                copiar_al_portapapeles(prompt_line_art)

            st.markdown(f"🖤 Llavero {i+1} - Prompt Single Color")
            st.text_area(f"Prompt Llavero {i+1} Single Color", prompt_single_color, height=120)
            if st.button(f"Copiar Llavero {i+1} Single Color"):
                copiar_al_portapapeles(prompt_single_color)

            st.markdown(f"⬛ Llavero {i+1} - Prompt Silhouette")
            st.text_area(f"Prompt Llavero {i+1} Silhouette", prompt_silhouette, height=120)
            if st.button(f"Copiar Llavero {i+1} Silhouette"):
                copiar_al_portapapeles(prompt_silhouette)

            st.divider()

        # Prompt soporte
        st.markdown("### 🏗️ Prompt para soporte")
        st.text_area("Prompt Soporte", prompt_soporte_func(), height=150)
        if st.button("Copiar Prompt Soporte"):
            copiar_al_portapapeles(prompt_soporte_func())

        # Prompt colección montada
        st.markdown("### 🖼️ Prompt colección montada en soporte")
        st.text_area("Prompt Colección en soporte", prompt_coleccion, height=150)
        if st.button("Copiar Prompt Colección en soporte"):
            copiar_al_portapapeles(prompt_coleccion)