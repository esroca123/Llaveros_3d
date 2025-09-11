import streamlit as st

st.set_page_config(page_title="Llavero 3D Prompt Generator", layout="wide")

# --- Función para copiar al portapapeles ---
def copiar_al_portapapeles(texto):
    st.markdown(f"""
    <button onclick="navigator.clipboard.writeText(`{texto}`).then(()=>{{alert('¡Prompt copiado al portapapeles!')}})">
    Copiar Prompt
    </button>
    """, unsafe_allow_html=True)

# --- Inicializar session_state para inputs ---
inputs = ["descripcion_general", "nombre_completo", "frase_opcional",
          "icono_general", "cantidad_colores", "colores_seleccionados",
          "estilo_seleccionado", "inicial_palabra", "estilo_inicial_seleccionado",
          "estilo_para_imagen_seleccionado"]

for inp in inputs:
    if inp not in st.session_state:
        st.session_state[inp] = "" if "colores_seleccionados" not in inp else []

# --- Título ---
st.title("🗝️ Llavero 3D Collection Prompt Generator")
st.markdown("Genera una colección de 4 llaveros 3D con prompts derivados y soporte innovador.")

# --- Estilos ---
estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic",
                       "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic",
                            "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar",
                            "Color Splash", "Lego", "Ghibli"]
todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

# --- Selección de estilo ---
st.session_state.estilo_seleccionado = st.selectbox(
    "Estilo del llavero",
    ["Initial of a word", "Free Style", "A partir de una imagen"] + todos_los_estilos,
    index=0 if not st.session_state.estilo_seleccionado else todos_los_estilos.index(st.session_state.estilo_seleccionado)
)

# --- Inputs principales ---
st.session_state.descripcion_general = st.text_area(
    "Descripción general de la colección",
    value=st.session_state.descripcion_general
)
st.session_state.nombre_completo = st.text_input(
    "Nombre completo (opcional)",
    value=st.session_state.nombre_completo
)
st.session_state.frase_opcional = st.text_input(
    "Frase a integrar en la imagen (opcional)",
    value=st.session_state.frase_opcional
)
st.session_state.icono_general = st.text_input(
    "Icono o símbolo general (opcional)",
    value=st.session_state.icono_general
)
st.session_state.cantidad_colores = st.selectbox(
    "Cantidad de colores (opcional)",
    ["Cualquiera"] + list(range(1, 5)),
    index=0 if st.session_state.cantidad_colores=="Cualquiera" else int(st.session_state.cantidad_colores)
)
colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
st.session_state.colores_seleccionados = st.multiselect(
    "Colores sugeridos (opcional)",
    colores_opciones,
    default=st.session_state.colores_seleccionados
)

# --- Inputs adicionales según opción ---
if st.session_state.estilo_seleccionado == "Initial of a word":
    st.session_state.inicial_palabra = st.text_input(
        "Palabra para la inicial",
        value=st.session_state.inicial_palabra
    )
    st.session_state.estilo_inicial_seleccionado = st.selectbox(
        "Estilo para la inicial",
        todos_los_estilos,
        index=0 if not st.session_state.estilo_inicial_seleccionado else todos_los_estilos.index(st.session_state.estilo_inicial_seleccionado)
    )

if st.session_state.estilo_seleccionado == "A partir de una imagen":
    st.markdown("La imagen de referencia debe subirse a la IA de tu elección por separado.")
    st.session_state.estilo_para_imagen_seleccionado = st.selectbox(
        "Estilo para aplicar a la imagen",
        todos_los_estilos,
        index=0 if not st.session_state.estilo_para_imagen_seleccionado else todos_los_estilos.index(st.session_state.estilo_para_imagen_seleccionado)
    )

# --- Función para generar prompt base ---
def generar_prompt_base(variacion_texto, llavero_num):
    prompt = ""
    estilo = st.session_state.estilo_seleccionado
    if estilo == "Initial of a word" and st.session_state.inicial_palabra:
        prompt = f"A 3D printed keychain design based on the letter '{st.session_state.inicial_palabra.upper()[0]}' in {st.session_state.estilo_inicial_seleccionado.lower()} style, low relief for 3D printing. {variacion_texto}{st.session_state.descripcion_general}"
    elif estilo == "A partir de una imagen":
        prompt = f"A 3D printed keychain design in {st.session_state.estilo_para_imagen_seleccionado.lower()} style based on an attached reference image, low relief for 3D printing. {variacion_texto}{st.session_state.descripcion_general}"
    else:
        prompt = f"A 3D printed keychain design in {estilo.lower()} style, low relief for 3D printing. {variacion_texto}{st.session_state.descripcion_general}"

    if st.session_state.nombre_completo:
        prompt += f" Include the full name '{st.session_state.nombre_completo}' elegantly."
    if st.session_state.frase_opcional:
        prompt += f" Integrate the phrase '{st.session_state.frase_opcional}' beautifully into the image."
    if st.session_state.icono_general:
        prompt += f" Incorporate the {st.session_state.icono_general} icon."
    if st.session_state.cantidad_colores != "Cualquiera":
        prompt += f" Use exactly {st.session_state.cantidad_colores} colors."
        if st.session_state.colores_seleccionados:
            prompt += f" Suggested colors: {', '.join(st.session_state.colores_seleccionados)}."
    elif st.session_state.colores_seleccionados:
        prompt += f" Suggested colors: {', '.join(st.session_state.colores_seleccionados)}."

    prompt += " Include a keyring hole and ensure the design is stable for 3D printing."
    return prompt

# --- Prompts derivados ---
prompt_line_art = "Convert this exact attached image to black and white line art, no shadows, high contrast, white background, suitable for DXF conversion."
prompt_single_color = "Convert this exact attached image into a single-color version, each original color area filled with solid black, no empty spaces."
prompt_silhouette = "Convert this exact attached image into a complete solid black silhouette, with no internal lines."

# --- Prompt soporte y colección ---
def prompt_soporte_func():
    return f"Design an innovative 3D printed keychain holder that complements the {st.session_state.estilo_seleccionado.lower()} style, suitable for displaying 4 keychains together coherently."

prompt_coleccion = "Display the 4 keychains mounted on the designed holder, full color, visually coherent."

# --- Botón generar ---
if st.button("Generar Prompts"):
    if st.session_state.estilo_seleccionado == "Initial of a word" and not st.session_state.inicial_palabra:
        st.error("Por favor, ingresa la palabra para la inicial.")
    elif not st.session_state.descripcion_general:
        st.error("Por favor, ingresa la descripción general.")
    else:
        st.divider()
        st.subheader("✅ Prompts generados para tu colección")

        for i in range(4):
            variacion_texto = f"Variation {i+1}: "
            prompt_base = generar_prompt_base(variacion_texto, i+1)

            st.markdown(f"### 🎨 Llavero {i+1} - Prompt Full Color")
            st.text_area(f"Prompt Llavero {i+1} Full Color", prompt_base, height=180)
            copiar_al_portapapeles(prompt_base)

            st.markdown(f"📐 Llavero {i+1} - Prompt DXF (Line Art)")
            st.text_area(f"Prompt Llavero {i+1} DXF", prompt_line_art, height=120)
            copiar_al_portapapeles(prompt_line_art)

            st.markdown(f"🖤 Llavero {i+1} - Prompt Single Color")
            st.text_area(f"Prompt Llavero {i+1} Single Color", prompt_single_color, height=120)
            copiar_al_portapapeles(prompt_single_color)

            st.markdown(f"⬛ Llavero {i+1} - Prompt Silhouette")
            st.text_area(f"Prompt Llavero {i+1} Silhouette", prompt_silhouette, height=120)
            copiar_al_portapapeles(prompt_silhouette)

            st.divider()

        # Prompt soporte
        st.markdown("### 🏗️ Prompt para soporte")
        st.text_area("Prompt Soporte", prompt_soporte_func(), height=150)
        copiar_al_portapapeles(prompt_soporte_func())

        # Prompt colección montada
        st.markdown("### 🖼️ Prompt colección montada en soporte")
        st.text_area("Prompt Colección en soporte", prompt_coleccion, height=150)
        copiar_al_portapapeles(prompt_coleccion)