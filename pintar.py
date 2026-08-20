import streamlit as st

st.set_page_config(page_title="Generador de Kits de Arte", layout="wide")
st.title("🎨 Generador de Kits de Arte: Colorear + Llavero")
st.markdown("Crea colecciones coherentes: una hoja para colorear limpia para niños y su llavero físico optimizado.")

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

# --- Lógica de Prompts Optimizado ---
def generar_prompts(tematica, estilo, detalles):
    # Prompt para la Página de Colorear (Simplificado para niños + Marco rectangular)
    prompt_colorear = f"""
    Create a clean, simple coloring book page designed specifically for young children. 
    Subject: {tematica}. Style: {estilo}. Details: {detalles}.
    Requirements: 
    - The entire page MUST be enclosed by a clean, straight black rectangular border framing the edge of the page.
    - Minimalist and simple background, not crowded, easy for kids to color.
    - Thick, clean, crisp black outlines.
    - Absolutely no gray, no shading, no colors, no textures inside.
    - Pure white background.
    - Composition: Centered and well-balanced inside the rectangular frame.
    """
    
    # Prompt para el Llavero (Sin argolla, sin borde rojo exterior)
    prompt_llavero = f"""
    Create a high-quality, professional 3D render design of a keychain character.
    Subject: {tematica}. Style: {estilo}. Details: {detalles}.
    Requirements:
    - Vibrant, solid flat colors.
    - Sharp, clean edges. 
    - STRICTLY NO keyring, NO metallic ring, NO chain, and NO hole or loop for a keyring at the top.
    - Absolutely NO external colored border or surrounding outline frame around the character. The silhouette must transition directly or have a very clean finish.
    - The figure must be completely isolated on a pure white background, ready for manufacturing.
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
            
        st.info("💡 Tip: Copia estos nuevos prompts en tu generador de imágenes. Ahora la hoja de colorear incluirá el marco y será más simple para niños, y el llavero saldrá libre de argollas y bordes extraños.")
    else:
        st.error("Por favor, ingresa una temática para comenzar.")
 
