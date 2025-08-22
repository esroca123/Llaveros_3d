import streamlit as st

# Título de la app
st.title("Generador de Prompts - Llaveros Personalizados")
st.markdown("Crea prompts detallados para generar diseños únicos de llaveros con IA.")
st.markdown("El prompt resultante solicitará una imagen con tres variaciones del diseño.")

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu llavero")

    # Contenedor para el estilo y la descripción
    with st.container():
        estilos_opciones = ["Minimalista", "Futurista", "Cartoon", "Inicial de palabra (especificar abajo)"]
        estilo_seleccionado = st.selectbox("Estilo del llavero", estilos_opciones)
        descripcion_opcional = st.text_area("Descripción adicional del estilo (opcional)", placeholder="Añade detalles específicos sobre el estilo aquí.")

        if estilo_seleccionado == "Inicial de palabra (especificar abajo)":
            inicial_palabra = st.text_input("Palabra para extraer la inicial", placeholder="Ej: Alejandra")
        else:
            inicial_palabra = None

    # Contenedor para los colores
    with st.container():
        colores_opciones = ["rojo", "azul", "verde", "amarillo", "negro", "blanco", "gris", "morado", "rosa", "naranja"]
        colores_seleccionados = st.multiselect("Colores (máx. 4)", colores_opciones, max_selections=4)

    # Campo opcional para el icono
    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej: rayo, luna, flor")

# --- Botón para generar el prompt y validación ---
if st.button("Generar Prompt", type="primary"):
    if not estilo_seleccionado or (estilo_seleccionado == "Inicial de palabra (especificar abajo)" and not inicial_palabra):
        st.error("Por favor, selecciona un estilo y especifica la palabra para la inicial si es necesario.")
    elif not colores_seleccionados:
        st.error("Por favor, selecciona al menos un color.")
    else:
        # Generamos el prompt base
        prompt = "Generar una imagen de un llavero con las siguientes características: "

        # Añadimos la parte del estilo
        if estilo_seleccionado == "Inicial de palabra (especificar abajo)" and inicial_palabra:
            prompt += f"Estilo basado en la letra '{inicial_palabra.upper()[0]}'."
        else:
            prompt += f"Estilo {estilo_seleccionado.lower()}."

        # Añadimos la descripción opcional si existe
        if descripcion_opcional:
            prompt += f" Detalles adicionales: {descripcion_opcional}."

        # Añadimos los colores
        colores_str = ", ".join(colores_seleccionados)
        prompt += f" Diseño con los colores: {colores_str}."

        # Añadimos el icono si existe
        if icono:
            prompt += f" Incorporar el icono de {icono}."

        # Especificamos la generación de las tres imágenes en una
        prompt += (
            " La imagen generada debe incluir tres variaciones del mismo diseño: "
            "1. Una versión a todo color. "
            "2. Una versión en blanco y negro optimizada para generar un archivo DXF (contornos claros y definidos). "
            "3. Una versión donde cada color del diseño original se reemplaza por negro, manteniendo la forma y las proporciones para identificar las áreas de cada color."
        )

        # Mostrar el resultado
        st.divider()
        st.subheader("✅ Tu prompt está listo:")
        st.text_area("Copia tu prompt aquí:", prompt, height=250)
        st.balloons()
