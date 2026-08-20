import streamlit as st

st.set_page_config(page_title="Generador de Kits de Arte", layout="wide")
st.title("🎨 Generador de Kits de Arte: Colorear + Llavero")
st.markdown("Crea colecciones coherentes: una hoja para colorear adaptada por edad y su llavero físico optimizado.")

# --- Configuración ---
with st.container():
    st.subheader("🛠️ Definición del Proyecto")
    
    tematica = st.text_input("Temática o Personaje", placeholder="Ej: Mario Bros, Hello Kitty, Animales de la selva")
    
    estilos = [
        "Chibi / Kawaii", "Cartoon clásico", "Estilo Anime", 
        "Line Art detallado", "Gamer / Arcade", "Floral / Nature"
    ]
    estilo_seleccionado = st.selectbox("Estilo artístico", estilos)
    
    # NUEVA OPCIÓN: Nivel de complejidad del fondo para colorear
    complejidad_fondo = st.selectbox(
        "Nivel de complejidad del fondo (Página para colorear)",
        [
            "Simple (Minimalista, pocos elementos, ideal para niños pequeños)", 
            "Intermedio (Un poco más elaborado, con más elementos temáticos pero limpio)"
        ]
    )
    
    detalles = st.text_area("Detalles del diseño", placeholder="Describe acciones o elementos extra (ej: 'Mario corriendo con un hongo', 'Hello Kitty con una manzana')")

# --- Lógica de Prompts Actualizada ---
def generar_prompts(tematica, estilo, complejidad, detalles):
    
    # Definir la instrucción del fondo según la opción elegida
    if "Simple" in complejidad:
        instruccion_fondo = "- Minimalist and very simple background, with very few elements, not crowded, very easy for toddlers to color."
    else:
        instruccion_fondo = "- Moderately detailed and engaging background with thematic elements from the character's world, balanced and fun for older kids, avoiding clutter."

    # Prompt para la Página de Colorear con Marco y complejidad variable
    prompt_colorear = f"""
    Create a clean coloring book page. 
    Subject: {tematica}. Style: {estilo}. Details: {detalles}.
    Requirements: 
    - The entire page MUST be enclosed by a clean, straight black rectangular border framing the edge of the page.
    {instruccion_fondo}
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
        p_color, p_llavero = generar_prompts(tematica, estilo_seleccionado, complejidad_fondo, detalles)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📄 Prompt para Hoja de Colorear")
            st.code(p_color, language="text")
        with col2:
            st.subheader("🔑 Prompt para Llavero")
            st.code(p_llavero, language="text")
            
        st.info("💡 Tip: Con esta nueva opción podrás alternar entre un diseño súper limpio para los más pequeños o uno con un poco más de contexto y reto para niños de mayor edad.")
    else:
        st.error("Por favor, ingresa una temática para comenzar.")
