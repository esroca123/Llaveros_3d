import streamlit as st

# Título de la app
st.title("Generador de Prompts - Llaveros")

# Variables que vamos a pedir
forma = st.text_input("Forma del llavero (ej: corazón, estrella, circular)")
estilo = st.text_input("Estilo (ej: minimalista, futurista, cartoon)")
colores = st.text_input("Colores (máx. 4, ej: rojo, negro, blanco, azul)")
texto = st.text_input("Texto o frase opcional")
icono = st.text_input("Icono o símbolo adicional (ej: rayo, luna, flor)")

# Botón para generar el prompt
if st.button("Generar Prompt"):
    prompt = (
        f"Llavero en forma de {forma}, estilo {estilo}, "
        f"con un diseño en bajo relieve usando máximo 4 colores: {colores}. "
    )

    if texto:
        prompt += f"Incluye el texto: '{texto}'. "
    if icono:
        prompt += f"Añade el icono de {icono}. "

    prompt += (
        "El diseño debe ser claro, visualmente atractivo, "
        "sin texturas adicionales, y listo para impresión 3D."
    )

    # Mostrar el resultado
    st.subheader("✅ Prompt generado:")
    st.text_area("Copia tu prompt aquí:", prompt, height=200)