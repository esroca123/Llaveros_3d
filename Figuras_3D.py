import streamlit as st

st.set_page_config(page_title="Gemini 3D Character Creator", layout="centered")

st.title("🧍‍♂️ 3D Character Gen (Gemini Optimized)")

# --- CATEGORÍA ---
character_type = st.selectbox("Tipo de creación", ["Personaje Existente", "Original"])

# --- LÓGICA DE PERSONAJE FAMOSO ---
if character_type == "Personaje Existente":
    char_name = st.text_input("Nombre del personaje", placeholder="Ej: Buzz Lightyear, Naruto...")
    
    # Este bloque es para que Gemini (el cerebro) trabaje antes de generar
    PROMPT_INSTRUCTION = f"""
    ACTÚA COMO UN EXPERTO EN MODELADO 3D Y DISEÑO DE PERSONAJES.
    
    PASO 1: Analiza mentalmente quién es el personaje '{char_name}'. Identifica sus rasgos físicos únicos, 
    su vestimenta icónica y sus proporciones exactas.
    
    PASO 2: Genera una imagen utilizando la herramienta 'image_generation' siguiendo estas reglas:
    - Sujeto: El personaje oficial {char_name}. Debe ser 100% fiel a su diseño original.
    - Estilo: Escultura 3D técnica, material de resina blanca pura, acabado mate.
    - Detalles: Superficies lisas, sin texturas de tela o piel, optimizado para impresión 3D.
    - Base: El personaje debe estar de pie sobre una base circular plana y sencilla.
    - Entorno: Fondo blanco sólido, iluminación de estudio neutra para ver todos los ángulos.
    - Restricción: No añadidas colores, ni efectos visuales, ni fondos complejos.
    """
    
    if st.button("✨ Preparar Instrucción"):
        st.info("Copia el texto de abajo y pégalo directamente en tu chat con Gemini:")
        st.text_area("Instrucción para Gemini:", PROMPT_INSTRUCTION.strip(), height=350)

else:
    # Lógica simplificada para personajes originales...
    st.write("Configuración para personajes originales (similar a la anterior).")

st.markdown("---")
st.caption("Nota: Al usar Gemini, la descripción detallada ayuda a Nano Banana a no 'alucinar' el diseño.")
