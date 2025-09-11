import streamlit as st

# Título de la app
st.title("Generador de Prompts para Llaveros")

# Estado para almacenar el prompt
if 'prompt' not in st.session_state:
    st.session_state['prompt'] = ""

# Entrada de texto
st.session_state['prompt'] = st.text_area("Escribe tu prompt:", st.session_state['prompt'], height=200)

# Selección de estilo
estilos = ["Minimalista", "Divertido", "Colorido", "Realista"]
estilo_seleccionado = st.selectbox("Selecciona un estilo:", estilos)

# Botón para generar prompt final
if st.button("Generar Prompt"):
    # Mantener la primera letra en mayúscula
    prompt_final = st.session_state['prompt'].strip()
    if prompt_final:
        prompt_final = prompt_final[0].upper() + prompt_final[1:]
        # Agregamos el estilo seleccionado al prompt
        prompt_final += f" | Estilo: {estilo_seleccionado}"
        st.session_state['prompt'] = prompt_final
        st.success("Prompt generado correctamente!")

# Mostrar prompt final
st.text_area("Prompt Final:", st.session_state['prompt'], height=150)

# Botón copiar al portapapeles
st.button("Copiar Prompt", on_click=lambda: st.experimental_set_query_params(copied=st.session_state['prompt']))

# Nota: Aquí puedes reemplazar la función de copiar con tu método preferido para copiar al portapapeles