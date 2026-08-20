import streamlit as st

st.set_page_config(page_title="Generador de Kits de Arte", layout="wide")
st.title("🎨 Generador de Kits de Arte: Colorear + Llavero")
st.markdown("Crea colecciones coherentes: una hoja para colorear y su llavero físico.")

# --- Configuración ---
with st.container():
    st.subheader("🛠️ Definición del Proyecto")
    
    tematica = st.text_input("Temática o Personaje", placeholder="Ej: Mario Bros, Hello Kitty, Animales de la selva")
    
    estilos = [
        "Chibi / Kawaii", "Cartoon clásico", "Estilo Anime", 
        "Line Art detallado", "Gamer / Arcade", "Floral / Nature"
    ]
    estilo_seleccionado = st.selectbox("Estilo artístico", estilos)
    
    detalles = st.text_area("Detalles del diseño", placeholder="Describe acciones o elementos extra (ej: 'Mario corriendo con un hongo', 'Hello Kitty con una manzana')")

# --- Lógica de Prompts ---
def generar_prompts(tematica, estilo, detalles):
    # Prompt para la Página de Colorear
    prompt_colorear = f"""
    Create a professional coloring book page for kids. 
    Subject: {tematica}. Style: {estilo}. Details: {detalles}.
    Requirements: 
    - Pure black and white line art only.
    - Thick, clean, crisp black outlines.
    - Absolutely no gray, no shading, no colors, no textures.
    - Pure white background.
    - The character must have a thematic background related to its world (e.g., pipes/blocks for Mario).
    - Composition: Centered, occupying the full page, ready to print.
    """
    
    # Prompt para el Llavero (Versión Color)
    prompt_llavero = f"""
    Create a high-quality, professional 3D render design of a keychain character.
    Subject: {tematica}. Style: {estilo}. Details: {detalles}.
    Requirements:
    - Vibrant, solid flat colors.
    - Sharp, clean edges. 
    - The design should be the character alone, without any external frame or background.
    - The figure must be isolated on a pure white background, ready for die-cut/manufacturing.
    - Professional, appealing collectible style.
    """
    return prompt_colorear, prompt_llavero

# --- Ejecución ---
if st.button("Generar Prompts del Kit", type="primary"):
    if tematica:
        p_color, p_llavero = generar_prompts(tematica, estilo_seleccionado, detalles)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📄 Prompt para Hoja de Colorear")
            st.code(p_color, language="text")
        with col2:
            st.subheader("🔑 Prompt para Llavero")
            st.code(p_llavero, language="text")
            
        st.info("💡 Tip: Usa estos prompts en tu herramienta de IA generativa (DALL-E, Midjourney, etc.) para obtener tus dos productos.")
    else:
        st.error("Por favor, ingresa una temática para comenzar.")
