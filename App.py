opciones_estilos = ["Initial of a word", "Free Style", "A partir de una imagen"] + todos_los_estilos

# Validar valor en session_state
if "estilo_seleccionado" not in st.session_state or st.session_state.estilo_seleccionado not in opciones_estilos:
    st.session_state.estilo_seleccionado = opciones_estilos[0]

# Ahora sí se puede usar index seguro
st.session_state.estilo_seleccionado = st.selectbox(
    "Estilo del llavero",
    opciones_estilos,
    index=opciones_estilos.index(st.session_state.estilo_seleccionado)
)