import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash", "Lego", "Ghibli", "illustration", "Photorealistic", "Hyperrealistic", "Live Action Style", "Cosplay photography", "Unreal Engine 5 Render"]
    
    estilo_iconic_chibi_cartoon = "Iconic Chibi Cartoon (Contorno Cero)"
    todos_los_estilos = [estilo_iconic_chibi_cartoon] + estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # --- SELECCIÓN DE ESTILOS (SISTEMA DUAL) ---
    col_estilo1, col_estilo2 = st.columns(2)
    with col_estilo1:
        estilo_seleccionado = st.selectbox("Estilo Principal", ["A partir de una imagen", "Full Name/Phrase", "Initial of a word", "Free Style"] + todos_los_estilos)
    with col_estilo2:
        estilo_secundario = st.selectbox("Segundo Estilo (Opcional)", ["Ninguno"] + todos_los_estilos)

    # Variables de control
    texto_ingresado = ""
    tipo_letras = None
    enfoque_referencia = None

    # Lógica de Imagen REFORZADA
    if estilo_seleccionado == "A partir de una imagen":
        st.info("💡 Modo de Referencia Visual Activo.")
        enfoque_referencia = st.radio(
            "¿Qué debe hacer la IA con la imagen?",
            ["Clonar Estilo de Letrero (Cambiar solo el texto)", "Solo personajes", "Imagen completa"],
            horizontal=True
        )
        
        if enfoque_referencia == "Clonar Estilo de Letrero (Cambiar solo el texto)":
            texto_ingresado = st.text_input("Escribe el NUEVO texto/nombre:")
            tipo_letras = st.radio("Estructura:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])
        
        estilo_para_imagen_seleccionado = st.selectbox("Estilo artístico adicional (opcional):", ["Ninguno"] + todos_los_estilos)

    # Lógica estándar para Letras (sin imagen)
    if estilo_seleccionado in ["Initial of a word", "Full Name/Phrase"]:
        texto_ingresado = st.text_input("Escribe el texto:")
        tipo_letras = st.radio("Estructura del llavero:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])

    # Campos de descripción
    descripcion_coleccion = st.text_area("Requerimientos adicionales o descripción (Opcional)", placeholder="Ej: estilo Dragon Ball, colores neón...")

# --- PROMPTS TÉCNICOS ---
try:
    if st.button("Generar Prompt Maestro", type="primary"):
        
        # 1. Definición de la estética base
        estilo_final = estilo_seleccionado.lower() if estilo_seleccionado != "A partir de una imagen" else "custom reference style"
        if estilo_secundario != "Ninguno":
            estilo_final = f"fusion of {estilo_final} and {estilo_secundario.lower()}"

        # PROMPT BASE (Reglas de Oro)
        prompt = f"""ACT AS A PROFESSIONAL GRAPHIC DESIGNER. 
Generate one high-quality design in {estilo_final}.
STRICT RULES: Solid flat colors ONLY. Sharp black internal lines for volume. NO gradients. NO shadows. Pure white background."""

        # 2. LÓGICA DE CLONACIÓN DE TEXTO (LA CLAVE DEL CAMBIO)
        if estilo_seleccionado == "A partir de una imagen" and enfoque_referencia == "Clonar Estilo de Letrero (Cambiar solo el texto)":
            prompt = f"""**STRICT STYLE TRANSFER TASK**
Use the attached image ONLY as a visual template for: Typography shape, Color palette, and Decorative ornaments.
**NEW TEXT TO RENDER:** "{texto_ingresado.upper()}"
**INSTRUCTIONS:** 1. Replace the original text from the image with "{texto_ingresado.upper()}".
2. CLONE the exact font style, textures, and 3D-effect (if any) from the reference image.
3. Keep the same color scheme.
4. COMPOSITION: Single horizontal line. Proportional spacing (kerning). Max bounding box 8cm x 4cm.
5. NO STACKING. NO extra words. Just the new text with the old style."""
            
            if tipo_letras == "Solo las letras (Sin fondo)":
                prompt += "\n6. REMOVE any background plaques. The design must be stand-alone interconnected letters."

        # 3. Lógica para otros casos de imagen
        elif estilo_seleccionado == "A partir de una imagen":
            if enfoque_referencia == "Solo personajes":
                prompt += "\n**REF:** Extract ONLY characters. Ignore background."
            else:
                prompt += "\n**REF:** Structural template. Maintain exact composition and poses."

        # 4. Inyección de descripción extra
        if descripcion_coleccion:
            prompt += f"\n**ADDITIONAL THEME:** {descripcion_coleccion}."

        st.divider()
        st.subheader("✅ Prompt para copiar en la IA:")
        st.code(prompt, language="markdown")
        st.caption("Copia este prompt y adjunta tu imagen en DALL-E 3, Midjourney o Leonardo AI.")

except Exception as e:
    st.error(f"Error: {e}")
