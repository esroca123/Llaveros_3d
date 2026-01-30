import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Estilos
    estilos_artisticos = ["Simple & Clean", "Anime Style", "Cartoon", "Cyberpunk", "Kawaii", "Metallic", "8-bit", "Pop Art"]
    todos_los_estilos = ["Full Name/Phrase", "A partir de una imagen", "Initial of a word"] + estilos_artisticos

    col_estilo1, col_estilo2 = st.columns(2)
    with col_estilo1:
        estilo_seleccionado = st.selectbox("Categoría Principal", todos_los_estilos)
    with col_estilo2:
        estilo_secundario = st.selectbox("Estilo Visual (Opcional)", ["Ninguno"] + estilos_artisticos)

    # --- LÓGICA DE TEXTO Y ESTRUCTURA (RESTAURADA) ---
    texto_ingresado = ""
    modo_generacion = None
    tipo_estructura = None

    if estilo_seleccionado in ["Full Name/Phrase", "Initial of a word", "A partir de una imagen"]:
        texto_ingresado = st.text_input("Escribe el nombre o frase:")
        
        # Opción para elegir entre un solo diseño o la colección
        modo_generacion = st.radio(
            "¿Qué deseas generar?",
            ["Un diseño específico", "Colección de 4 variantes (2x2)"],
            horizontal=True
        )

        if modo_generacion == "Un diseño específico":
            tipo_estructura = st.radio(
                "Estructura del llavero:",
                ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"],
                horizontal=True
            )

    # Lógica de Imagen
    if estilo_seleccionado == "A partir de una imagen":
        enfoque_referencia = st.radio("Enfoque de imagen:", ["Clonar Estilo de Letrero", "Solo personajes", "Imagen completa"])

    descripcion_coleccion = st.text_area("Descripción extra (Opcional)")
    colores = st.multiselect("Colores sugeridos", ["red", "blue", "green", "yellow", "black", "white", "purple", "pastel colors"])

# --- GENERACIÓN DEL PROMPT ---
try:
    if st.button("Generar Prompt Maestro", type="primary"):
        if not texto_ingresado and estilo_seleccionado != "A partir de una imagen":
            st.error("Por favor, ingresa el texto.")
        else:
            # Estilo base
            estilo_final = estilo_secundario.lower() if estilo_secundario != "Ninguno" else "modern"
            
            # Encabezado según cantidad
            cant = "one single design" if modo_generacion == "Un diseño específico" else "four different designs in a 2x2 grid"
            
            prompt = f"Generate **{cant}** in {estilo_final} style.\n"
            prompt += f"**CORE SUBJECT:** The text '{texto_ingresado.upper()}'.\n"

            # Lógica de estructura recuperada
            if modo_generacion == "Un diseño específico":
                if tipo_estructura == "Solo las letras (Sin fondo)":
                    prompt += "**STRUCTURE:** Die-cut style. Only the interconnected letters. No background plates. The silhouette follows the letters. Bounding box max 8x4cm (proportional).\n"
                else:
                    prompt += "**STRUCTURE:** Text integrated into a solid decorative background or plaque (circular or rectangular).\n"
            else:
                # Lógica de colección de 4 variantes
                prompt += "**COLLECTION RULES:** Provide 4 variations: 1) Circular badge, 2) Rectangular plaque (2:1 ratio), 3) Die-cut letters only (no background), 4) Simple/Minimalist version.\n"

            # Reglas críticas de texto
            prompt += f"**MANDATORY:** Single horizontal line. No stacking letters. Correct spelling of '{texto_ingresado.upper()}'. Letters must be interconnected.\n"
            prompt += "**VISUALS:** Solid flat colors. Sharp black internal lines. Pure white background. No gradients.\n"

            if colores: prompt += f"**COLORS:** {', '.join(colores)}.\n"
            if descripcion_coleccion: prompt += f"**THEME:** {descripcion_coleccion}."

            st.divider()
            st.subheader("✅ Prompt Generado")
            st.code(prompt, language="markdown")

except Exception as e:
    st.error(f"Error: {e}")
