# Guardar inputs en session_state si no existen
if "descripcion_general" not in st.session_state:
    st.session_state.descripcion_general = ""
if "nombre_completo" not in st.session_state:
    st.session_state.nombre_completo = ""
if "frase_opcional" not in st.session_state:
    st.session_state.frase_opcional = ""
if "icono_general" not in st.session_state:
    st.session_state.icono_general = ""
if "cantidad_colores" not in st.session_state:
    st.session_state.cantidad_colores = "Cualquiera"
if "colores_seleccionados" not in st.session_state:
    st.session_state.colores_seleccionados = []

# Luego en cada input
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
    index=["Cualquiera"] + list(range(1,5)).index(st.session_state.cantidad_colores) if st.session_state.cantidad_colores!="Cualquiera" else 0
)
st.session_state.colores_seleccionados = st.multiselect(
    "Colores sugeridos (opcional)",
    colores_opciones,
    default=st.session_state.colores_seleccionados
)