import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator PRO")
st.markdown("Generador de prompts de alta fidelidad con control total de composición.")

# --- Listas Completas de Estilos ---
estilos_fuente = [
    "Modern Sans-Serif", "Classic Serif", "Graffiti / Urban", "Cursive / Script", 
    "Blackletter / Gothic", "Bubble Letters", "Stencil", "Blocky / Heavy", 
    "Futuristic / Sci-Fi", "Comic / Cartoon", "Elegant / Luxury", "Handwritten", "Disney Style", "Neon Sign Font"
]

estilos_visuales = [
    "Simple & Clean", "Metallic / Chrome", "Neon / Glowing", "Wood-carved", 
    "Glass-like", "Cyberpunk", "Kawaii / Pastel", "8-bit / Pixel", "Pop Art", 
    "Ghibli Style", "Anime/Manga", "Realistic", "Futurist", "Vintage", "Steampunk", 
    "Art Deco", "Gothic", "Surrealist", "Clay-sculpted", "Flat Design", 
    "Geometric", "Vaporwave", "Cottagecore", "Urban / Graffiti", "Sporty", 
    "Lego Style", "Color Splash", "Hyperrealistic", "Unreal Engine 5 Render"
]

# --- Contenedor de Personalización ---
with st.container():
    st.subheader("🛠️ Configuración de Diseño")

    # Selección de Categoría
    estilo_seleccionado = st.selectbox("Categoría Principal", ["Full Name/Phrase", "A partir de una imagen", "Initial of a word"])

    # Variables de control
    texto_ingresado = st.text_input("Escribe el nombre o frase:", placeholder="Ej: Bachir / Adventure Awaits")
    
    # --- SISTEMA DE DOBLE ESTILO (RESTAURADO) ---
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        fuente_principal = st.selectbox("Estilo de Letra (Fuente)", estilos_fuente)
    with col_f2:
        fuente_secundaria = st.selectbox("Estilo Visual (Acabado/Material)", ["Ninguno"] + estilos_visuales)

    # --- COMPOSICIÓN DINÁMICA ---
    st.divider()
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        estructura = st.radio("Estructura Física:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])
        disposicion = st.radio("Disposición del Texto:", ["Una sola línea horizontal", "Dos líneas (Apilado decorativo)"])
    
    with col_c2:
        if estructura == "Texto con fondo decorativo/placa":
            forma_fondo = st.selectbox("Forma del fondo:", ["Rectangular (8x4)", "Circular", "Forma orgánica personalizada"])
        else:
            st.info("📏 Optimizado para 8cm x 4cm max (proporcional).")
    
    descripcion_extra = st.text_area("Detalles adicionales (Ej: 'Inspirado en galaxias', 'Colores de superhéroe')")
    colores = st.multiselect("Paleta de colores", ["red", "blue", "green", "yellow", "black", "white", "purple", "gold", "silver", "cyan", "pink", "neon colors", "pastel colors"])

# --- GENERACIÓN DEL PROMPT ---
try:
    if st.button("Generar Prompt Maestro", type="primary"):
        if not texto_ingresado:
            st.error("Por favor, ingresa el texto.")
        else:
            # Mezcla de estilos
            estilo_final = fuente_principal.lower()
            if fuente_secundaria != "Ninguno":
                estilo_final = f"fusion of {fuente_principal.lower()} and {fuente_secundaria.lower()}"
            
            # --- CONSTRUCCIÓN DEL PROMPT TÉCNICO ---
            prompt = f"ACT AS A MASTER TYPOGRAPHER AND KEYCHAIN DESIGNER. Generate a highly attractive professional design.\n"
            prompt += f"**SUBJECT:** The text '{texto_ingresado.upper()}'.\n"
            prompt += f"**STYLE:** {estilo_final}.\n"

            # Lógica de Disposición
            if disposicion == "Una sola línea horizontal":
                instruccion_lineas = "Rendered in a SINGLE HORIZONTAL LINE. No stacking."
            else:
                instruccion_lineas = "Rendered in TWO STACKED LINES. The words must be artistically arranged one above the other to create a compact, balanced, and solid block."

            # Lógica de Estructura y Proporción
            if estructura == "Solo las letras (Sin fondo)":
                prompt += f"**STRUCTURE:** Die-cut style. No background plates. The outer silhouette must follow the exact shape of the letters.\n"
                prompt += f"**COMPOSITION:** {instruccion_lineas} All letters must be thick, bold, and interconnected to form a single solid piece. Max bounding box 8cm x 4cm proportional to name length.\n"
            else:
                prompt += f"**STRUCTURE:** Integrated into a {forma_fondo.lower()} plaque.\n"
                prompt += f"**COMPOSITION:** {instruccion_lineas} **CRITICAL:** The text must be LARGE, BOLD, and EYE-CATCHING, occupying at least 80% of the plaque's surface area. The text should dominate the design.\n"

            # Reglas de Calidad
            prompt += f"**MANDATORY:** Correct spelling of '{texto_ingresado.upper()}'. Solid flat colors. Sharp black internal vector lines. Pure white background (RGB 255, 255, 255). No gradients. No external shadows.\n"
            
            if colores: prompt += f"**COLORS:** {', '.join(colores)}.\n"
            if descripcion_extra: prompt += f"**THEME/CONTEXT:** {descripcion_extra}."

            st.divider()
            st.subheader("✅ Prompt Maestro Generado")
            st.code(prompt, language="markdown")
            
            st.success("¡Todo listo! He restaurado todos los estilos y configurado la composición máxima.")

except Exception as e:
    st.error(f"Error: {e}")
