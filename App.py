import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Genera un prompt detallado para crear un diseño de llavero con cuatro variaciones, usando una imagen de referencia.")

# Definición de estilos
estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash"]

todos_los_estilos = estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu llavero")
    st.markdown("Sube una imagen y describe cómo quieres que la IA la adapte al diseño del llavero.")

    imagen_subida = st.file_uploader("Sube una imagen de base:", type=["png", "jpg", "jpeg"])
    
    estilo_seleccionado = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)
    
    descripcion_adicional = st.text_area(
        "Descripción adicional para el llavero:",
        placeholder="Describe lo que quieres que aparezca, por ejemplo: 'la persona de la foto manejando una moto en un paisaje futurista'."
    )
    
    if st.button("Generar Prompt", type="primary"):
        if imagen_subida is not None and descripcion_adicional:
            # Generar el prompt con las 4 variaciones
            prompt_base = (
                f"A creative, unique, highly detailed keychain design in a {estilo_seleccionado} style, "
                f"based on the uploaded image. The design should incorporate the following: "
                f"'{descripcion_adicional}'."
            )
            
            prompt_completo = (
                f"Generate a single image of a keychain design with the following four distinct sections arranged horizontally: "
                f"1. On the far right: A full-color version of the {prompt_base} The design must include a keyring hole but no keyring attached."
                f"2. Second from the right: A black and white line art version of the {prompt_base} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion. The design must include a keyring hole but no keyring attached."
                f"3. Second from the left: A single-color version of the {prompt_base} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces. The design must include a keyring hole but no keyring attached."
                f"4. On the far left: A complete, solid black silhouette of the {prompt_base} with no internal lines. The design must include a keyring hole but no keyring attached."
                " Ensure there is clear space separating each of the four variations to prevent overlap."
            )

            # Muestra el resultado
            st.divider()
            st.subheader("✅ Tu prompt está listo:")
            st.text_area("Copia este prompt y pégalo en tu IA de preferencia (junto con la imagen subida):", prompt_completo, height=400)
        else:
            st.error("Por favor, sube una imagen y añade una descripción.")
