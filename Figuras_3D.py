import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="3D Character Generator Pro", layout="centered")

st.title("🧍‍♂️ FOX ⭐ 3D Character Workflow")

st.markdown("""
### Estrategia de Dos Pasos:
1. **Generar la Identidad:** Creamos al personaje con total fidelidad.
2. **Convertir a 3D:** Usamos la imagen del Paso 1 para crear la figura imprimible.
""")

# --------------------------------------------------
# UI - ENTRADA DE DATOS
# --------------------------------------------------
char_name = st.text_input("Nombre del Personaje", placeholder="Ej: Master Oogway")
extra_details = st.text_input("Detalles adicionales (Pose, expresión, objetos)")

if st.button("✨ Generar Flujo de Trabajo"):
    if not char_name:
        st.error("Por favor, introduce el nombre de un personaje.")
    else:
        # --- PROMPT PASO 1: FIDELIDAD TOTAL ---
        prompt_paso_1 = f"""
PASO 1: GENERACIÓN DE IDENTIDAD CRÍTICA
OBJETIVO: Crear una imagen cinematográfica de alta calidad de {char_name}.
DETALLES: {extra_details if extra_details else "Apariencia canon oficial completa"}.
REGLA: Debe ser una representación 1:1 del personaje original de la película, con todas sus arrugas, texturas de piel y vestimenta original a todo color.
FONDO: Fondo neutro sólido.
"""

        # --- PROMPT PASO 2: TRADUCCIÓN A 3D ---
        prompt_paso_2 = f"""
PASO 2: TRADUCCIÓN TÉCNICA A FIGURA 3D
INSTRUCCIÓN: Usa la imagen generada en el Paso 1 como referencia geométrica absoluta.
ACCIÓN: Convierte al personaje de la imagen en una escultura digital para impresión 3D.
ESTILO: Resina blanca pura, sin pintar, acabado mate.
DETALLES TÉCNICOS: Mantén el 100% de las arrugas y formas de la cara del Paso 1. 
CONTROL: Aísla al personaje sobre un fondo blanco puro, añade una base redonda simple y elimina cualquier textura que no sea relieve.
"""

        # --- MOSTRAR RESULTADOS ---
        st.subheader("1️⃣ Paso 1: Generar la Referencia")
        st.info("Copia este prompt primero para obtener la imagen perfecta del personaje:")
        st.code(prompt_paso_1.strip(), language="text")

        st.subheader("2️⃣ Paso 2: Crear la Versión 3D")
        st.info("Una vez generada la imagen del Paso 1, adjúntala y usa este prompt:")
        st.code(prompt_paso_2.strip(), language="text")

        st.success("Flujo de trabajo generado. ¡Sigue los pasos en orden!")
