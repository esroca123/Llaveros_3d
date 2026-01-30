import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Definición de estilos mejorada
    estilos_artisticos = [
        "Simple & Clean (Minimalist)", "Anime Style", "Cartoon", "Cyberpunk", 
        "Kawaii", "Metallic", "Wood-carved", "8-bit", "Ghibli Style", "Pop Art"
    ]
    
    # Lista extendida de estilos
    estilos_especificos = ["Realistic", "16-bit", "Futurist", "Vintage", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Gothic", "Surrealist", "Glass-like", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave"]
    
    estilo_iconic_chibi = "Iconic Chibi Cartoon (Contorno Cero)"
    todos_los_estilos = [estilo_iconic_chibi] + estilos_artisticos + estilos_especificos + estilos_adicionales

    # --- SELECCIÓN DE ESTILOS ---
    col_estilo1, col_estilo2 = st.columns(2)
    with col_estilo1:
        estilo_seleccionado = st.selectbox("Categoría Principal", ["Full Name/Phrase", "A partir de una imagen", "Initial of a word", "Free Style"] + todos_los_estilos)
    with col_estilo2:
        estilo_secundario = st.selectbox("Estilo Visual de la Colección", ["Ninguno"] + todos_los_estilos)

    # Variables de control
    texto_ingresado = ""
    
    # LÓGICA PARA FULL NAME / PHRASE
    if estilo_seleccionado == "Full Name/Phrase":
        texto_ingresado = st.text_input("Escribe el nombre completo o frase:", placeholder="Ej: Bachir / Love Life")
        st.info("🎨 Se generarán 4 variantes: Redondo, Cuadrado, Solo Letras y Minimalista.")

    # Lógica para Imagen
    elif estilo_seleccionado == "A partir de una imagen":
        enfoque_referencia = st.radio("Enfoque:", ["Clonar Estilo de Letrero", "Solo personajes", "Imagen completa"])
        if "Letrero" in enfoque_referencia:
            texto_ingresado = st.text_input("Nuevo texto basado en la imagen:")
    
    descripcion_coleccion = st.text_area("Descripción adicional (Opcional)", placeholder="Ej: colores pastel, estilo galaxia...")

    # Colores
    st.divider()
    colores_seleccionados = st.multiselect("Colores sugeridos", ["red", "blue", "green", "yellow", "black", "white", "purple", "pink", "orange", "pastel colors", "neon colors"])

# --- GENERACIÓN DEL PROMPT ---
try:
    if st.button("Generar Colección de 4 Diseños", type="primary"):
        if estilo_seleccionado == "Full Name/Phrase" and not texto_ingresado:
            st.error("Por favor, ingresa el texto.")
        else:
            # Definir estilo final
            estilo_final = estilo_secundario.lower() if estilo_secundario != "Ninguno" else "modern and attractive"
            if estilo_seleccionado == "Simple & Clean (Minimalist)":
                estilo_final = "minimalist, simple flat colors, elegant, clean lines, high contrast"

            # Construcción del Prompt MAESTRO
            prompt = f"""**TASK:** Create a collection of **4 different keychain designs** in a 2x2 grid.
**STYLE:** {estilo_final}.
**CORE SUBJECT:** The text "{texto_ingresado.upper()}".

**COLLECTION VARIATIONS (One for each of the 4 designs):**
1. **CIRCULAR:** The text "{texto_ingresado.upper()}" perfectly centered inside a solid circular badge.
2. **SQUARE/RECTANGULAR:** The text inside a sharp square or rectangular frame (8x4 aspect ratio).
3. **DIE-CUT (LETTERS ONLY):** The text as a stand-alone piece where the silhouette follows the outer edges of the interconnected letters.
4. **SIMPLE & MINIMAL:** A very basic but attractive version using only 2 solid colors, bold clean typography, and no ornaments.

**TECHNICAL RULES:**
- **HORIZONTAL ALIGNMENT:** Text must be in a single horizontal line in all 4 versions. No stacking.
- **INTERCONNECTION:** Letters must touch/be connected to form a single solid piece.
- **VISUALS:** Solid flat colors. Sharp black internal lines. Pure white background. No gradients. No shadows.
"""
            # Añadir colores si se seleccionaron
            if colores_seleccionados:
                prompt += f"\n**COLOR PALETTE:** {', '.join(colores_seleccionados)}."
            
            if descripcion_coleccion:
                prompt += f"\n**EXTRA THEME:** {descripcion_coleccion}."

            st.divider()
            st.subheader("✅ Prompt de Colección (4 Diseños):")
            st.code(prompt, language="markdown")
            
            st.success("Este prompt generará una cuadrícula con las 4 formas solicitadas (Circular, Cuadrada, Troquelada y Simple).")

except Exception as e:
    st.error(f"Error: {e}")
