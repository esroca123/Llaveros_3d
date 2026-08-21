import streamlit as st

st.set_page_config(page_title="Generador de Kits de Arte Pro", layout="wide")
st.title("🎨 Generador de Kits de Arte y Diseños Avanzados")
st.markdown("Herramienta profesional para crear kits infantiles y diseños avanzados de alta complejidad mediante texto libre.")

# --- Sistema de Pestañas (Tabs) ---
pestana_infantil, pestana_avanzada = st.tabs(["🧸 Kits Infantiles (Colorear + Llavero)", "🔥 Diseños Avanzados & Estilos Complejos"])

# ==========================================
# PESTAÑA 1: KITS INFANTILES
# ==========================================
with pestana_infantil:
    st.subheader("Configuración del Kit Infantil")
    
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        tematica_inf = st.text_input("Temática o Personaje (Infantil)", placeholder="Ej: Mario Bros, Hello Kitty", key="tem_inf")
        estilo_inf = st.selectbox("Estilo artístico", ["Chibi / Kawaii", "Cartoon clásico", "Estilo Anime"], key="est_inf")
    with col_i2:
        complejidad_fondo = st.selectbox(
            "Nivel de complejidad del fondo (Hoja de colorear)",
            [
                "Simple (Minimalista, pocos elementos, ideal para niños pequeños)", 
                "Intermedio (Un poco más elaborado, con más elementos temáticos pero limpio)"
            ],
            key="comp_inf"
        )
        
    detalles_inf = st.text_area("Detalles adicionales", placeholder="Ej: corriendo con un hongo, sonriendo...", key="det_inf")

    if st.button("Generar Prompts Infantiles", type="primary", key="btn_inf"):
        if tematica_inf:
            if "Simple" in complejidad_fondo:
                inst_fondo = "- Minimalist and very simple background, with very few elements, not crowded, very easy for toddlers to color."
            else:
                inst_fondo = "- Moderately detailed and engaging background with thematic elements from the character's world, balanced and fun for older kids, avoiding clutter."

            prompt_colorear = f"""
            Create a clean coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). 
            Subject: {tematica_inf}. Style: {estilo_inf}. Details: {detalles_inf}.
            Requirements: 
            - The entire page MUST be enclosed by a clean, straight black rectangular border with rounded corners framing the edge of the page.
            {inst_fondo}
            - Thick, clean, crisp black outlines.
            - Absolutely no gray, no shading, no colors, no textures inside.
            - Pure white background.
            - Composition: Centered and well-balanced inside the rounded rectangular frame, matching the 150x110 mm vertical proportion.
            """
            
            prompt_llavero = f"""
            Create a high-quality, professional 3D render design of a keychain character.
            Subject: {tematica_inf}. Style: {estilo_inf}. Details: {detalles_inf}.
            Requirements:
            - Vibrant, solid flat colors.
            - Sharp, clean edges. 
            - STRICTLY NO keyring, NO metallic ring, NO chain, and NO hole or loop for a keyring at the top.
            - Absolutely NO external colored border or surrounding outline frame around the character. The silhouette must transition directly or have a very clean finish.
            - The figure must be completely isolated on a pure white background, ready for manufacturing.
            """
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### 📄 Hoja de Colorear")
                st.code(prompt_colorear, language="text")
            with c2:
                st.markdown("#### 🔑 Llavero 3D")
                st.code(prompt_llavero, language="text")
        else:
            st.error("Por favor, ingresa una temática infantil.")

# ==========================================
# PESTAÑA 2: DISEÑOS AVANZADOS (Libre / Streetwear / Poligonal / Mandalas)
# ==========================================
with pestana_avanzada:
    st.subheader("🔥 Generador de Diseños Avanzados por Descripción Libre")
    st.markdown("Escribe exactamente lo que imaginas (un animal, un concepto, un objeto) y combínalo con estilos profesionales de gran formato.")
    
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        # CAMBIO CLAVE: Texto totalmente libre para describir la imagen o concepto deseado
        descripcion_libre = st.text_area(
            "¿Qué quieres crear? (Descripción o Imagen deseada)", 
            placeholder="Ej: Un león imponente rodeado de panteras, Un cráneo de azúcar mexicano, Un paisaje urbano futurista...", 
            key="desc_libre"
        )
        
        estilo_pro = st.selectbox(
            "Estilo Visual Avanzado",
            [
                "Streetwear Splash Art (Grafitis, salpicaduras de pintura colorida, ropa urbana con capucha y audífonos)",
                "Geometric Low-Poly / Mosaic (Facetado poligonal geométrico, mosaico moderno)",
                "Mandala Intricada (Diseño simétrico, meditativo y altamente detallado)",
                "Vector Art / Pop Illustration (Diseño limpio y vibrante para impresión en agendas/camisetas)"
            ],
            key="est_pro"
        )
    with col_a2:
        fondo_pro = st.selectbox(
            "Fondo y Contexto",
            [
                "Aislado sobre fondo negro sólido y limpio",
                "Aislado sobre fondo blanco puro",
                "Con salpicaduras de pintura expansivas y dinámicas (Paint splatters splashing around)"
            ],
            key="fon_pro"
        )
        
        iluminacion_pro = st.selectbox(
            "Paleta de Colores y Acabado",
            [
                "Colores vibrantes de neón y alto contraste",
                "Gama cromática de tonos cálidos y fríos equilibrados",
                "Monocromático con acentos de color brillantes"
            ],
            key="ilu_pro"
        )

    detalles_pro = st.text_area("Detalles técnicos o elementos extra opcionales", placeholder="Ej: Mirada penetrante, estilo simétrico perfecto, líneas finas...", key="det_pro")

    if st.button("Generar Prompt Avanzado", type="primary", key="btn_pro"):
        if descripcion_libre:
            # Lógica adaptada a la descripción libre del usuario
            if "Streetwear" in estilo_pro:
                estilo_prompt = "Vibrant Streetwear Pop Splash Art illustration, dynamic composition with modern urban elements, surrounded by colorful watercolor and paint splatters, bold outlines, highly detailed digital artwork, commercial vector style suitable for printing."
            elif "Geometric" in estilo_pro:
                estilo_prompt = "Geometric low-poly mosaic illustration, sharp triangular facets, colorful stained-glass aesthetic, intricate patterns, clean vector shapes, highly detailed."
            elif "Mandala" in estilo_pro:
                estilo_prompt = "Intricate and complex mandala design, highly symmetrical, ornate geometric and floral patterns, meditative aesthetic, clean fine-line vector art, professional graphic design."
            else:
                estilo_prompt = "High-end vector pop illustration, clean lines, vibrant flat colors, modern commercial graphic style, sharp details."

            prompt_avanzado_final = f"""
            {estilo_prompt}
            Core Subject / Concept: {descripcion_libre}. 
            Additional Details: {detalles_pro}.
            Color Palette & Atmosphere: {iluminacion_pro}.
            Background Requirement: {fondo_pro}.
            Additional Technical Specs: Masterpiece, ultra-sharp focus, perfect composition, flawless vector quality, commercial printing ready.
            """

            st.markdown("#### 🚀 Prompt Avanzado Optimizado")
            st.code(prompt_avanzado_final.strip(), language="text")
            st.info("💡 Tip: Copia este prompt en tu generador favorito. Al describir libremente el concepto, la IA interpretará exactamente los elementos visuales que buscas bajo el filtro del estilo avanzado elegido.")
        else:
            st.error("Por favor, ingresa una descripción o concepto para generar el prompt.")
