import streamlit as st

# --- Configuración de la App ---
st.set_page_config(page_title="Generador de Prompts - Llaveros 3D", page_icon="🔑", layout="centered")

st.title("🔑 Generador de Prompts para Llaveros 3D")
st.write("⚠️ **Importante:** Para mejores resultados, introduce la información en **inglés**.")

# --- Estilos de llaveros disponibles ---
estilos_llaveros = {
    "Minimalista geométrico": "Describe la forma geométrica o patrón",
    "Inicial de nombre con diseño artístico": "Indica la letra o inicial",
    "Animal estilizado": "Indica el animal",
    "Símbolo cultural": "Indica el símbolo o cultura",
    "Futurista con relieve": "Describe el elemento futurista",
    "Naturaleza (hojas, flores, montañas)": "Indica el elemento natural",
    "Steampunk con engranajes": "Indica si quieres algún elemento especial",
    "Retro 8-bit": "Indica el videojuego o personaje retro",
    "Inspirado en tatuajes": "Indica el estilo o elemento del tatuaje",
    "Abstracto artístico": "Describe el estilo abstracto"
}

# --- Selección del estilo ---
estilo = st.selectbox("Selecciona el estilo de llavero:", list(estilos_llaveros.keys()))

# --- Campo extra según el estilo ---
extra_info = st.text_input(f"{estilos_llaveros[estilo]}:")

# --- Nombre y descripción ---
nombre_llavero = st.text_input("Nombre del llavero (ej: Corazón pequeño, Hoja minimalista...)")
descripcion_llavero = st.text_area("Descripción general del llavero (en inglés):", 
                                   placeholder="Describe el diseño, tamaño pequeño, innovador, ideal para impresión 3D...")

# --- Botón para generar ---
if st.button("Generar Prompt"):
    if nombre_llavero.strip() == "" or descripcion_llavero.strip() == "" or extra_info.strip() == "":
        st.error("Por favor completa todos los campos.")
    else:
        # --- Prompts por versión ---
        prompt_color = (
            f"{descripcion_llavero}, {estilo} ({extra_info}), full color, "
            "highly detailed, creative, unique, suitable for small keychain design, "
            "3D print-ready, artistic composition"
        )

        prompt_bn = (
            f"{descripcion_llavero}, {estilo} ({extra_info}), black and white line art, "
            "thin lines, single stroke, no shadows, no thick outlines, "
            "clean vector style, optimized for DXF conversion"
        )

        # Versión para una imagen dividida
        prompt_base = f"Create a split image grid showing two versions of the same design: Left side: {prompt_color} | Right side: {prompt_bn}"

        # --- Prompts específicos ---
        prompt_dalle = prompt_base
        prompt_mj = f"{prompt_base} --ar 1:1 --v 6 --q 2 --style raw"
        prompt_sd = f"{prompt_base}, ultra detailed, 8k, photorealistic render"

        # --- Mostrar resultados ---
        st.subheader("🎯 Prompt generado para DALL·E:")
        st.code(prompt_dalle, language="text")

        st.subheader("🎯 Prompt generado para MidJourney:")
        st.code(prompt_mj, language="text")

        st.subheader("🎯 Prompt generado para Stable Diffusion:")
        st.code(prompt_sd, language="text")

        # --- Frases sugeridas para la caja ---
        frases = [
            f"Carry your style with the {nombre_llavero} keychain",
            f"Small details, big personality — {nombre_llavero}",
            f"{nombre_llavero}: Designed for everyday adventures",
            f"Your pocket-sized companion — {nombre_llavero}"
        ]

        st.subheader("📦 Frases sugeridas para la caja:")
        for frase in frases:
            st.write(f"- {frase}")
