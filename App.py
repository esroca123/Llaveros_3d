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

# --- Campo extra opcional ---
extra_info = st.text_input(f"{estilos_llaveros[estilo]} (opcional):")

# --- Nombre del llavero ---
nombre_llavero = st.text_input("Nombre del llavero (ej: Corazón pequeño, Hoja minimalista...)")

# --- Botón para generar ---
if st.button("Generar Prompt"):
    if nombre_llavero.strip() == "":
        st.error("Por favor, ingresa el nombre del llavero.")
    else:
        # Descripción base por defecto
        descripcion_base_color = (
            f"{estilo} {f'({extra_info})' if extra_info else ''}, "
            "full color, highly detailed, creative, unique, small size for keychain, "
            "3D print-ready, artistic composition"
        )

        descripcion_base_bn = (
            f"{estilo} {f'({extra_info})' if extra_info else ''}, "
            "black and white line art, thin lines, single stroke, no shadows, no thick outlines, "
            "clean vector style, optimized for DXF conversion"
        )

        # Prompt para la imagen combinada
        prompt_base = (
            f"Create a single image split in two halves showing the same keychain design: "
            f"Left side: {descripcion_base_color} | Right side: {descripcion_base_bn}"
        )

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
