import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator PRO")
st.markdown("Generación masiva de variantes para diseño y fabricación.")

# --- Listas de Estilos ---
estilos_fuente = ["Modern Sans-Serif", "Graffiti", "Bubble Letters", "Cursive", "Blocky / Heavy", "Futuristic", "Comic / Cartoon", "Elegant", "Disney Style"]
estilos_visuales = ["Simple & Clean", "Metallic", "Neon / Glowing", "Wood-carved", "Cyberpunk", "Kawaii", "8-bit", "Pop Art", "Gold Leaf"]

with st.container():
    st.subheader("🛠️ Configuración de Colección (4 Opciones)")

    # Categoría y Texto
    estilo_seleccionado = st.selectbox("Categoría Principal", ["Full Name/Phrase", "A partir de una imagen", "Initial of a word"])
    texto_ingresado = st.text_input("Escribe el nombre o frase:")
    
    # Estilos Duales
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        fuente_principal = st.selectbox("Estilo de Letra", estilos_fuente)
    with col_f2:
        fuente_secundaria = st.selectbox("Acabado Visual", ["Ninguno"] + estilos_visuales)

    # Composición
    st.divider()
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        estructura = st.radio("Estructura Física:", ["Solo las letras (Sin fondo)", "Texto con fondo decorativo/placa"])
        disposicion = st.radio("Disposición del Texto:", ["Una sola línea horizontal", "Dos líneas (Apilado)"])
    
    with col_c2:
        incluir_argolla = st.radio("¿Incluir agujero/argolla?", ["NO", "SÍ"], index=0)
        if estructura == "Texto con fondo decorativo/placa":
            forma_fondo = st.selectbox("Forma del fondo:", ["Rectangular (8x4)", "Circular", "Orgánica"])
        else:
            st.info("📏 Variantes optimizadas para troquelado.")

    colores = st.multiselect("Paleta de colores", ["red", "blue", "green", "yellow", "black", "white", "purple", "gold", "cyan"])

# --- GENERACIÓN DEL PROMPT ---
try:
    if st.button("Generar 4 Variantes", type="primary"):
        if not texto_ingresado:
            st.error("Ingresa el texto.")
        else:
            estilo_final = fuente_principal.lower()
            if fuente_secundaria != "Ninguno":
                estilo_final = f"fusion of {fuente_principal.lower()} and {fuente_secundaria.lower()}"
            
            # --- COMANDO DE CUADRÍCULA (GRID) ---
            prompt = f"ACT AS A MASTER TYPOGRAPHER. Generate a **2x2 grid showing four different variations** of a keychain design.\n"
            prompt += f"**SUBJECT:** The text '{texto_ingresado.upper()}'.\n"
            prompt += f"**STYLE:** {estilo_final}.\n"

            # Restricción de Argolla
            if incluir_argolla == "NO":
                prompt += "**STRICT FORBIDDEN:** NO holes, NO metal rings, NO chains. Just the clean solid objects.\n"
            
            # Composición de líneas
            if disposicion == "Una sola línea horizontal":
                instruccion_lineas = "SINGLE HORIZONTAL LINE per design. No stacking."
            else:
                instruccion_lineas = "TWO STACKED LINES per design. Artistic compact blocks."

            # Estructura y Cuadrícula
            if estructura == "Solo las letras (Sin fondo)":
                prompt += f"**STRUCTURE:** Four unique die-cut versions. No background plates. {instruccion_lineas} Letters must be thick, bold, and interconnected.\n"
            else:
                prompt += f"**STRUCTURE:** Four unique versions integrated into {forma_fondo.lower()} plaques. {instruccion_lineas} Text must occupy 80% of the plaque area.\n"

            # Variedad en la cuadrícula
            prompt += "**VARIATION:** Each of the 4 designs should have slightly different typographic ornaments or creative flourishes while staying within the style.\n"

            # Visuales
            prompt += f"**VISUALS:** Correct spelling. Solid flat colors. Sharp black internal lines. Pure white background. No gradients. No shadows.\n"
            if colores: prompt += f"**COLORS:** {', '.join(colores)}."

            st.divider()
            st.subheader("✅ Prompt para 4 Diseños:")
            st.code(prompt, language="markdown")
            st.success("He forzado a la IA a generar una cuadrícula de 2x2 para que tengas 4 opciones para elegir.")

except Exception as e:
    st.error(f"Error: {e}")
