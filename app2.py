import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor de Personalización ---
with st.container():
    st.subheader("🛠️ Configuración de Diseño Llamativo")

    # Estilos de Letra y Acabados
    estilos_fuente = ["Modern Sans-Serif", "Graffiti", "Bubble Letters", "Cursive", "Blocky / Heavy", "Futuristic", "Comic / Cartoon", "Elegant"]
    estilos_visuales = ["Simple & Clean", "Metallic / Chrome", "Neon / Glowing", "Kawaii", "Cyberpunk", "8-bit", "Pop Art", "Gold Leaf"]
    
    # Selección de Categoría
    estilo_seleccionado = st.selectbox("Categoría Principal", ["Full Name/Phrase", "A partir de una imagen", "Initial of a word"])

    # Variables de control
    texto_ingresado = st.text_input("Escribe el nombre o frase:")
    
    # --- SISTEMA DE DOBLE ESTILO ---
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        fuente_principal = st.selectbox("Estilo de Letra", estilos_fuente)
    with col_f2:
        fuente_secundaria = st.selectbox("Estilo Visual / Acabado", ["Ninguno"] + estilos_visuales)

    # --- COMPOSICIÓN DINÁMICA ---
    st.divider()
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        estructura = st.radio("Estructura Física:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])
    with col_c2:
        disposicion = st.radio("Disposición del Texto:", ["Una sola línea horizontal", "Dos líneas (Apilado decorativo)"], help="La opción de dos líneas es ideal para nombres largos o frases.")

    # Ajuste de "Llamatividad" para Fondos
    if estructura == "Texto con fondo decorativo/placa":
        forma_fondo = st.selectbox("Forma del fondo:", ["Rectangular (8x4)", "Circular", "Forma orgánica personalizada"])
    
    descripcion_extra = st.text_area("Detalles adicionales (Ej: 'Inspirado en Spider-Man', 'Estilo Galaxia')")
    colores = st.multiselect("Paleta de colores", ["red", "blue", "green", "yellow", "black", "white", "purple", "gold", "cyan", "pink"])

# --- GENERACIÓN DEL PROMPT ---
try:
    if st.button("Generar Diseño Profesional", type="primary"):
        if not texto_ingresado:
            st.error("Por favor, ingresa el texto.")
        else:
            # Mezcla de estilos
            estilo_final = fuente_principal.lower()
            if fuente_secundaria != "Ninguno":
                estilo_final = f"fusion of {fuente_principal.lower()} and {fuente_secundaria.lower()}"
            
            # --- CONSTRUCCIÓN DEL PROMPT TÉCNICO ---
            prompt = f"ACT AS A MASTER TYPOGRAPHER AND KEYCHAIN DESIGNER. Generate a highly attractive design.\n"
            prompt += f"**SUBJECT:** The text '{texto_ingresado.upper()}'.\n"
            prompt += f"**STYLE:** {estilo_final}.\n"

            # Lógica de Disposición
            if disposicion == "Una sola línea horizontal":
                instruccion_lineas = "Rendered in a SINGLE HORIZONTAL LINE. No stacking."
            else:
                instruccion_lineas = "Rendered in TWO STACKED LINES. The words must be artistically arranged one above the other to create a compact and balanced block."

            # Lógica de Estructura y Proporción
            if estructura == "Solo las letras (Sin fondo)":
                prompt += f"**STRUCTURE:** Die-cut style. No background. The silhouette follows the letters.\n"
                prompt += f"**COMPOSITION:** {instruccion_lineas} All letters must be thick, bold, and interconnected to form a single solid piece.\n"
            else:
                prompt += f"**STRUCTURE:** Integrated into a {forma_fondo.lower()} plaque.\n"
                prompt += f"**COMPOSITION:** {instruccion_lineas} **CRITICAL:** The text must be LARGE and BOLD, occupying at least 80% of the plaque's surface area. The text should dominate the space, not look small or isolated.\n"

            # Reglas de Calidad y Visuales
            prompt += f"**MANDATORY:** Correct spelling of '{texto_ingresado.upper()}'. Solid flat colors. Sharp black internal vector lines. Pure white background (RGB 255, 255, 255). No gradients. No external shadows.\n"
            
            if colores: prompt += f"**COLORS:** {', '.join(colores)}.\n"
            if descripcion_extra: prompt += f"**THEME/CONTEXT:** {descripcion_extra}."

            st.divider()
            st.subheader("✅ Prompt Maestro Generado")
            st.code(prompt, language="markdown")
            
            # Nota de éxito según la selección
            if estructura == "Texto con fondo decorativo/placa":
                st.success("🎨 El prompt incluye la orden de 'Texto Gigante' para que el fondo no opaque tu nombre.")
            else:
                st.success(f"📏 El prompt está optimizado para un diseño de {'una línea' if disposicion == 'Una sola línea horizontal' else 'dos líneas'} troquelado.")

except Exception as e:
    st.error(f"Error: {e}")
