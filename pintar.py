import streamlit as st

st.set_page_config(page_title="Generador de Kits de Arte Pro", layout="wide")
st.title("🎨 Generador de Kits de Arte: Infantil y Avanzado (Colorear + Llavero)")
st.markdown("Crea colecciones coherentes con estilos urbanos avanzados y equilibrados para un público mayor.")

# --- Sistema de Pestañas (Tabs) ---
pestana_infantil, pestana_avanzada = st.tabs(["🧸 Kits Infantiles", "🔥 Kits Avanzados / Adultos (Streetwear & Estilos Urbanos)"])

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
# PESTAÑA 2: KITS AVANZADOS / ADULTOS (Streetwear equilibrado)
# ==========================================
with pestana_avanzada:
    st.subheader("🔥 Kit Avanzado / Adultos (Estilo Urbano, Streetwear y Detalles Finos)")
    st.markdown("Crea diseños complejos de estilo urbano (como las referencias de streetwear con sudaderas, audífonos y salpicaduras) adaptados perfectamente para colorear sin perder detalle ni saturarse.")
    
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        descripcion_libre = st.text_area(
            "¿Qué concepto o imagen quieres crear?", 
            placeholder="Ej: Luigi con sudadera urbana y audífonos, un león con estilo street art...", 
            key="desc_libre"
        )
        
        estilo_pro = st.selectbox(
            "Estilo Visual Avanzado",
            [
                "Streetwear Urban Pop Art (Ropa moderna, sudadera con capucha, audífonos, salpicaduras de pintura estilizadas en líneas)",
                "Mandala Elegante / Detallada (Diseño simétrico avanzado y refinado)",
                "Geometric Low-Poly / Mosaic (Facetado geométrico moderno)",
                "Line Art Detallado y Sofisticado (Ilustración intrincada de alta calidad)"
            ],
            key="est_pro"
        )
    with col_a2:
        tipo_fondo_urbano = st.selectbox(
            "Estilo de las salpicaduras y fondo",
            [
                "Salpicaduras de pintura y elementos urbanos en líneas limpias (Paint splatters line-art)",
                "Fondo geométrico o simétrico sutil de alta gama",
                "Composición centrada con detalles gráficos limpios"
            ],
            key="fon_pro_urb"
        )
        
        acabado_llavero = st.selectbox(
            "Estilo del Llavero / Figura Física Coherente",
            [
                "Versión 3D Streetwear en alta definición con colores sólidos vibrantes",
                "Versión 3D estilizada en alta definición con acabado limpio"
            ],
            key="fab_pro"
        )

    detalles_pro = st.text_area("Detalles técnicos o elementos extra opcionales", placeholder="Ej: Usando hoodie moderna, audífonos de DJ, expresión decidida...", key="det_pro")

    if st.button("Generar Kit Avanzado Estilo Urbano", type="primary", key="btn_pro"):
        if descripcion_libre:
            # Definir prompts especializados según el estilo urbano o avanzado
            if "Streetwear" in estilo_pro:
                base_estilo_colorear = "Detailed Streetwear Urban Pop Art coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Dynamic character wearing a modern urban hoodie and headphones, surrounded by stylish paint splatters and graphic urban elements converted into clean black line art."
                base_estilo_llavero = "A high-quality 3D render design of a streetwear urban character keychain wearing modern hoodie and headphones, vibrant solid flat colors, sharp edges."
            elif "Mandala" in estilo_pro:
                base_estilo_colorear = "Sophisticated adult coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Balanced symmetrical mandala style, elegant fine-line patterns."
                base_estilo_llavero = "A high-end professional 3D physical badge or decorative keychain render based on an elegant mandala design, symmetrical, vibrant solid flat colors."
            elif "Geometric" in estilo_pro:
                base_estilo_colorear = "Advanced geometric low-poly coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Sharp triangular facets, intricate clean line art."
                base_estilo_llavero = "A high-quality 3D clean geometric render model of a keychain character or object, sharp clean edges, solid vibrant multi-colors."
            else:
                base_estilo_colorear = "Detailed intricate line art coloring book page with a vertical rectangular aspect ratio (approx. 150 mm height by 110 mm width). Sophisticated patterns, sharp fine black outlines."
                base_estilo_llavero = "A professional 3D render design of a detailed keychain, vibrant solid colors, sharp clean edges."

            # Prompt avanzado para la hoja de colorear (con los requerimientos de estilo urbano equilibrado)
            prompt_colorear_avanzado = f"""
            {base_estilo_colorear}
            Subject / Concept: {descripcion_libre}. Details: {detalles_pro}.
            Background Style: {tipo_fondo_urbano}.
            Requirements:
            - The entire page MUST be enclosed by a clean, straight black rectangular border with rounded corners framing the edge of the page.
            - The illustration must look like professional adult coloring art: detailed, stylish, capturing the urban streetwear aesthetic without being overcrowded or overly simplistic.
            - Thick, clean, crisp black outlines.
            - Absolutely no gray, no shading, no colors, no textures inside.
            - Pure white background.
            - Composition: Centered and well-balanced inside the rounded rectangular frame, matching the 150x110 mm vertical proportion.
            """
            
            # Prompt avanzado para el llavero correspondiente
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
                st.markdown("#### 📄 Hoja de Colorear (Urbana / Avanzada)")
                st.code(prompt_colorear_avanzado.strip(), language="text")
            with c2:
                st.markdown("#### 🔑 Llavero / Figura 3D (Coherente)")
                st.code(prompt_llavero_avanzado.strip(), language="text")
                
            st.info("💡 Tip: Este ajuste fuerza a la IA a renderizar la estética de las referencias urbanas (sudaderas, audífonos y salpicaduras gráficas) pero pasadas a un formato de líneas limpias para colorear, evitando tanto el exceso de barullo visual como el diseño simplón.")
        else:
            st.error("Por favor, ingresa una descripción o concepto para generar el kit avanzado.")
