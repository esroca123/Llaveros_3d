import streamlit as st

st.set_page_config(page_title="Generador de Kits de Arte Pro", layout="wide")
st.title("🎨 Generador de Kits de Arte: Infantil y Avanzado (Colorear + Llavero)")
st.markdown("Crea colecciones coherentes de hojas para colorear y llaveros físicos, adaptados tanto para niños como para un público más adulto o avanzado.")

# --- Sistema de Pestañas (Tabs) ---
pestana_infantil, pestana_avanzada = st.tabs(["🧸 Kits Infantiles", "🔥 Kits Avanzados / Adultos (Mandalas, Streetwear, Poligonal)"])

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

    if st.button("Generar Kits Infantiles", type="primary", key="btn_inf"):
        if tematica_inf:
            if "Simple" in complejidad_fondo:
                inst_fondo = "- Minimalist and very simple background, with very few elements, not crowded, very easy for toddlers to color."
            else:
                inst_fondo = "- Moderately detailed and engaging background with thematic elements from the character's world, balanced and fun for older kids, avoiding clutter."

            prompt_colorear_inf = f"""
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
            
            prompt_llavero_inf = f"""
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
                st.markdown("#### 📄 Hoja de Colorear (Infantil)")
                st.code(prompt_colorear_inf, language="text")
            with c2:
                st.markdown("#### 🔑 Llavero 3D (Infantil)")
                st.code(prompt_llavero_inf, language="text")
        else:
            st.error("Por favor, ingresa una temática infantil.")

# ==========================================
# PESTAÑA 2: KITS AVANZADOS / ADULTOS (Colorear + Llavero)
# ==========================================
with pestana_avanzada:
    st.subheader("🔥 Kit Avanzado / Adultos (Colorear Detallado + Llavero Coherente)")
    st.markdown("Crea diseños complejos de alta gama para pintar (como mandalas detalladas, estilos poligonales o arte urbano) acompañados de su llavero a juego.")
    
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        descripcion_libre = st.text_area(
            "¿Qué concepto o imagen quieres crear?", 
            placeholder="Ej: Un león geométrico, una mandala compleja de flores, un cráneo de azúcar mexicano...", 
            key="desc_libre"
        )
        
        estilo_pro = st.selectbox(
            "Estilo Visual Avanzado",
            [
                "Mandala Intricada (Diseño simétrico, meditativo y altamente detallado para colorear adultos)",
                "Geometric Low-Poly / Mosaic (Facetado poligonal geométrico, mosaico moderno)",
                "Streetwear Splash Art (Grafitis, salpicaduras detalladas de pintura y estética urbana)",
                "Line Art Complejo / Zentangle (Ilustración intrincada de alta densidad y texturas finas)"
            ],
            key="est_pro"
        )
    with col_a2:
        complejidad_pro_fondo = st.selectbox(
            "Nivel de detalle del fondo para colorear",
            [
                "Alto nivel de detalle y patrones ornamentales envolventes",
                "Fondo geométrico o simétrico estructurado de alta complejidad"
            ],
            key="comp_pro"
        )
        
        acabado_llavero = st.selectbox(
            "Estilo del Llavero / Figura Física",
            [
                "Versión 3D estilizada en alta definición con colores sólidos vibrantes",
                "Versión 3D geométrica / facetada lista para fabricación"
            ],
            key="fab_pro"
        )

    detalles_pro = st.text_area("Detalles técnicos o elementos extra opcionales", placeholder="Ej: Elementos florales adicionales, simetría perfecta, trazos muy limpios...", key="det_pro")

    if st.button("Generar Kit Avanzado (Colorear + Llavero)", type="primary", key="btn_pro"):
        if descripcion_libre:
            # Definir estilo de prompt avanzado para colorear
            if "Mandala" in estilo_pro:
                base_estilo_colorear = "Intricate and complex adult coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Highly symmetrical mandala style, ornate geometric and floral patterns."
                base_estilo_llavero = "A high-end professional 3D physical badge or decorative keychain render based on a complex mandala design, symmetrical, vibrant solid flat colors."
            elif "Geometric" in estilo_pro:
                base_estilo_colorear = "Advanced geometric low-poly coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Sharp triangular facets, mosaic stained-glass aesthetic, intricate line art."
                base_estilo_llavero = "A high-quality 3D geometric low-poly render model of a keychain character or object, sharp clean edges, solid vibrant multi-colors."
            elif "Streetwear" in estilo_pro:
                base_estilo_colorear = "Detailed streetwear pop art coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Dynamic composition, urban textures, bold clean outlines."
                base_estilo_llavero = "A high-quality 3D render design of a streetwear urban character keychain, vibrant solid flat colors, sharp edges."
            else:
                base_estilo_colorear = "Complex and detailed Zentangle line art coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Dense patterns, fine intricate black outlines."
                base_estilo_llavero = "A professional 3D render design of an intricate detailed keychain, vibrant solid colors, sharp clean edges."

            # Prompt avanzado para la hoja de colorear (con marco redondeado, medida 150x110 y nivel adulto)
            prompt_colorear_avanzado = f"""
            {base_estilo_colorear}
            Subject / Concept: {descripcion_libre}. Details: {detalles_pro}.
            Background/Environment: {complejidad_pro_fondo}.
            Requirements:
            - The entire page MUST be enclosed by a clean, straight black rectangular border with rounded corners framing the edge of the page.
            - Thick, clean, crisp black outlines suitable for older kids, teens, or adults.
            - Absolutely no gray, no shading, no colors, no textures inside.
            - Pure white background.
            - Composition: Centered and well-balanced inside the rounded rectangular frame, matching the 150x110 mm vertical proportion.
            """
            
            # Prompt avanzado para el llavero/figura física correspondiente
            prompt_llavero_avanzado = f"""
            {base_estilo_llavero}
            Subject / Concept: {descripcion_libre}. Details: {detalles_pro}.
            Style type: {acabado_llavero}.
            Requirements:
            - Vibrant, solid flat colors.
            - Sharp, clean edges. 
            - STRICTLY NO keyring, NO metallic ring, NO chain, and NO hole or loop for a keyring at the top.
            - Absolutely NO external colored border or surrounding outline frame around the object. 
            - Completely isolated on a pure white background, ready for manufacturing.
            """

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### 📄 Hoja de Colorear (Avanzada / Adultos)")
                st.code(prompt_colorear_avanzado.strip(), language="text")
            with c2:
                st.markdown("#### 🔑 Llavero / Figura 3D (Avanzado)")
                st.code(prompt_llavero_avanzado.strip(), language="text")
                
            st.info("💡 Tip: Ambas salidas mantienen la coherencia temática del concepto ingresado, generando una página para colorear de formato 150x110 mm con esquinas redondeadas y su respectivo llavero físico sin argollas adaptado al estilo avanzado elegido.")
        else:
            st.error("Por favor, ingresa una descripción o concepto para generar el kit avanzado.")
