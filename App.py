import streamlit as st

# Configuración de la página (opcional pero recomendado)
st.set_page_config(
    page_title="Llavero Prompts Generator",
    page_icon="🔑",
    layout="centered"
)

def generate_base_prompt(estilo, inicial, estilo_inicial, descripcion, icono, texto, cantidad_colores, colores):
    """Genera la parte base del prompt con todas las opciones seleccionadas."""
    
    # Lógica para el estilo base
    if estilo == "Initial of a word" and inicial:
        base_prompt = f"A **creative, unique, highly detailed** design based on the letter '{inicial.upper()[0]}' in a {estilo_inicial.lower()} style."
    elif estilo == "Free Style":
        base_prompt = f"A **creative, unique, highly detailed** keychain design."
    else:
        base_prompt = f"A **creative, unique, highly detailed** {estilo.lower()} keychain design."
    
    # Añadir elementos opcionales
    if descripcion:
        base_prompt += f" Additional details: {descripcion}."
    if icono:
        base_prompt += f" Incorporate the {icono} icon."
    if texto:
        base_prompt += f" Include the text: '{texto}'."
        
    # Lógica para los colores
    colores_str = ", ".join(colores)
    if cantidad_colores != "Any":
        base_prompt += f" The design must use exactly {cantidad_colores} colors."
        if colores:
            base_prompt += f" Suggested colors: {colores_str}."
    elif colores:
        base_prompt += f" Suggested colors: {colores_str}."
        
    return base_prompt

# --- Título y descripción ---
st.title("Llavero Prompts Generator 🔑")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")
st.markdown("El prompt resultante solicitará una sola imagen con cuatro variaciones de diseño distintas.")

# --- Contenedor principal para la entrada de datos ---
with st.container():
    st.subheader("🛠️ Personaliza tu Llavero")
    st.markdown("Elige el estilo, colores y elementos para tu diseño. **Todos los campos son opcionales**, a menos que selecciones 'Initial of a word'.")

    # Estilos y descripción
    estilos_predefinidos = {
        "Específicos": ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"],
        "Generales": ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"],
        "Artísticos": ["Color Splash", "Pop Art", "Watercolor", "Pastel", "Graffiti"]
    }
    
    estilo_opciones = ["Initial of a word", "Free Style"]
    for categoria in estilos_predefinidos:
        estilo_opciones.extend(estilos_predefinidos[categoria])

    estilo_seleccionado = st.selectbox("Estilo del llavero", estilo_opciones)

    # Lógica condicional para "Initial of a word"
    inicial_palabra = None
    estilo_inicial_seleccionado = None
    if estilo_seleccionado == "Initial of a word":
        inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej. Alexandra")
        estilos_iniciales_disponibles = estilo_opciones[2:] # Excluye "Initial of a word" y "Free Style"
        estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", estilos_iniciales_disponibles)

    descripcion_opcional = st.text_area("Descripción de estilo adicional (opcional)", placeholder="Añade detalles específicos sobre el estilo o personaje aquí.")

    # Colores
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    cantidad_colores = st.slider("Número de colores", 1, 5, 5, help="Define cuántos colores usará el diseño final. Elige 5 para usar todos los colores que la IA considere apropiados.")
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=cantidad_colores if cantidad_colores < 5 else 10)

    # Elementos opcionales
    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej. rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej. 'Feliz Cumpleaños'")

# --- Botón para generar el prompt y validación ---
if st.button("Generar Prompt", type="primary"):
    # Validaciones adicionales
    if estilo_seleccionado == "Initial of a word" and not inicial_palabra:
        st.error("Por favor, especifica la palabra para la inicial.")
    elif len(colores_seleccionados) > cantidad_colores and cantidad_colores < 5:
        st.error(f"No puedes sugerir más de {cantidad_colores} colores.")
    else:
        # Generar el prompt base
        base_prompt_content = generate_base_prompt(
            estilo=estilo_seleccionado,
            inicial=inicial_palabra,
            estilo_inicial=estilo_inicial_seleccionado,
            descripcion=descripcion_opcional,
            icono=icono,
            texto=texto_opcional,
            cantidad_colores=cantidad_colores if cantidad_colores < 5 else "Any",
            colores=colores_seleccionados
        )
        
        # Construir el prompt final
        final_prompt = "Generate a single image of a keychain design with the following characteristics, split into four distinct sections arranged horizontally: "
        
        # Variaciones
        variations = {
            "far right": f"A full-color version of the {base_prompt_content}",
            "second from the right": f"A black and white line art version of the {base_prompt_content} It must have only thin outlines, no shadows, a clean vector style, and be optimized for DXF file conversion.",
            "second from the left": f"A single-color version of the {base_prompt_content} where each original color area is filled with solid black, maintaining the separation between the different parts, with fully filled shapes and no empty spaces.",
            "far left": f"A complete, solid black silhouette of the {base_prompt_content} with no internal lines."
        }
        
        # Ensamblar el prompt final
        for position, description in variations.items():
            final_prompt += f"{position}: {description.strip()} The design must include a keyring hole but no keyring attached."
        
        # Instrucciones adicionales para el layout
        final_prompt += " Ensure there is clear space separating each of the four variations to prevent overlap."
        
        # Mostrar el resultado
        st.divider()
        st.subheader("✅ Tu prompt está listo:")
        st.info("Copia el texto de abajo y pégalo en tu generador de imágenes con IA favorito (como Midjourney, DALL-E 3, etc.).")
        st.text_area("Copia tu prompt aquí:", final_prompt, height=450)
