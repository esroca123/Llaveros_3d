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

    # --- SELECCIÓN DE ESTILOS ---
    col_estilo1, col_estilo2 = st.columns(2)
    with col_estilo1:
        estilo_seleccionado = st.selectbox("Estilo Principal", ["Full Name/Phrase", "A partir de una imagen", "Initial of a word", "Free Style"] + todos_los_estilos)
    with col_estilo2:
        estilo_secundario = st.selectbox("Segundo Estilo (Opcional)", ["Ninguno"] + todos_los_estilos)

    # Variables de control
    texto_ingresado = ""
    tipo_letras = None

    # LÓGICA ESPECÍFICA PARA FULL NAME / PHRASE
    if estilo_seleccionado == "Full Name/Phrase":
        texto_ingresado = st.text_input("Escribe el nombre completo o frase:", placeholder="Ej: Bachir / Mi Mascota")
        tipo_letras = st.radio("Estructura del llavero:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"], horizontal=True)
        estilo_base_letras = st.selectbox("Estilo artístico para el texto:", todos_los_estilos)

    # Lógica para otras opciones (simplificada para este ajuste)
    elif estilo_seleccionado == "A partir de una imagen":
        enfoque_referencia = st.radio("Enfoque:", ["Clonar Estilo de Letrero", "Solo personajes", "Imagen completa"])
        if "Letrero" in enfoque_referencia:
            texto_ingresado = st.text_input("Nuevo texto:")
            tipo_letras = st.radio("Estructura:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])
        estilo_base_letras = st.selectbox("Estilo artístico:", todos_los_estilos)
    
    else:
        estilo_base_letras = "custom"

    descripcion_coleccion = st.text_area("Descripción o tema adicional", placeholder="Ej: inspirado en el espacio, colores neón...")

# --- GENERACIÓN DEL PROMPT ---
try:
    if st.button("Generar Prompt de Nombre/Frase", type="primary"):
        if (estilo_seleccionado == "Full Name/Phrase" or "Letrero" in str(locals().get('enfoque_referencia', ''))) and not texto_ingresado:
            st.error("Por favor, ingresa el texto para generar el prompt.")
        else:
            # Definición de estilo final
            estilo_final = estilo_base_letras.lower() if estilo_seleccionado in ["Full Name/Phrase", "A partir de una imagen"] else estilo_seleccionado.lower()
            if estilo_secundario != "Ninguno":
                estilo_final = f"fusion of {estilo_final} and {estilo_secundario.lower()}"

            # Construcción del Prompt MAESTRO para NOMBRES
            prompt = f"""**TASK:** Professional Graphic Design for a custom keychain.
**STYLE:** {estilo_final}.
**CORE SUBJECT:** The specific text "{texto_ingresado.upper()}".

**TYPOGRAPHY RULES:**
1. **TEXT INTEGRITY:** The word "{texto_ingresado.upper()}" must be spelled correctly. No extra letters.
2. **HORIZONTAL ALIGNMENT:** Render the entire text in a SINGLE HORIZONTAL LINE. No stacking, no splitting the word into two lines.
3. **PROPORTIONAL KERNING:** Maintain balanced and attractive spacing between letters. The design must fit a maximum proportional bounding box of 8cm x 4cm based on name length.
4. **BOLD STRUCTURE:** Use thick, bold typography. All letters MUST be physically interconnected/touching to form a single solid piece."""

            if tipo_letras == "Solo las letras (Sin fondo)":
                prompt += "\n5. **DIE-CUT SHAPE:** No background plates. The outer silhouette must follow the exact shape of the letters. Pure white background."
            else:
                prompt += "\n5. **PLAQUE DESIGN:** The text is integrated into a creative decorative base or rectangular plaque."

            prompt += f"\n\n**VISUAL FINISH:** Solid flat colors. Sharp black internal vector lines. High contrast. No gradients. No shadows."
            
            if descripcion_coleccion:
                prompt += f"\n**THEME DETAILS:** {descripcion_coleccion}."

            st.divider()
            st.subheader("✅ Prompt Optimizado para Full Name/Phrase:")
            st.code(prompt, language="markdown")
            
            st.info("💡 **Consejo:** Este prompt obliga a la IA a mantener el nombre en una sola línea y asegura que las letras estén unidas para que el llavero no se rompa.")

except Exception as e:
    st.error(f"Error: {e}")
