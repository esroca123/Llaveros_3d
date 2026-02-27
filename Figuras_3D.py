import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="3D Character Generator",
    layout="centered"
)

st.title("🧍‍♂️🦊⭐ 3D Character Generator")

st.markdown(
    "Generador de prompts para **figuras 3D imprimibles en blanco**, "
    "listas para pintar y personalizar."
)

# --------------------------------------------------
# ADVERTENCIA SUPERIOR
# --------------------------------------------------
st.warning(
    "⚠️ Para obtener un resultado fiel de un personaje existente, "
    "asegúrate de **adjuntar al menos una imagen de referencia directamente en la IA** "
    "(por ejemplo, Gemini) que generará la imagen. "
    "Si la referencia es parcial (rostro o torso), la IA completará el resto del cuerpo "
    "manteniendo coherencia."
)

# --------------------------------------------------
# UI – TYPE SELECTION
# --------------------------------------------------
character_type = st.selectbox(
    "Select what you want to create",
    ["Person", "Animal", "Character"]
)

# --------------------------------------------------
# TYPE-SPECIFIC INPUTS
# --------------------------------------------------
base_character_block = ""
char_name = ""
gender = ""
animal_type = ""

if character_type == "Person":
    gender = st.selectbox("Gender", ["Male", "Female"])
    base_character_block = f"Original human character. Gender: {gender}. Neutral standing pose. Friendly and calm expression."

elif character_type == "Animal":
    animal_type = st.text_input(
        "Type of animal",
        placeholder="e.g. turtle, fox, cat..."
    )
    base_character_block = f"Anthropomorphic {animal_type} character. Standing on two legs like a human. Animal anatomy preserved."

elif character_type == "Character":
    char_name = st.text_input(
        "Character name",
        placeholder="e.g. Master Oogway, Pikachu..."
    )
    base_character_block = f"Existing fictional character: {char_name}."

# --------------------------------------------------
# OPTIONAL INPUTS
# --------------------------------------------------
profession = st.text_input(
    "Profession (optional)",
    placeholder="e.g. baker, samurai, doctor..."
)

extra_details = st.text_input(
    "Extra details (optional)",
    placeholder="e.g. holding a lantern, calm pose..."
)

use_photo = st.checkbox("Use photo reference (optional)")

photo_reference = ""
if use_photo:
    photo_reference = st.text_area(
        "Describe the photo reference",
        placeholder="Describe facial features, clothing, posture..."
    )

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
if st.button("✨ Generate Prompt"):

    # --- DEFINICIONES DE BLOQUES FIJOS ---
    BRAND_STYLE = "STYLE: Clean 3D digital sculpture, unpainted white resin material, matte finish."
    TECH_BLOCK = "CONTROL: Isolated on white background, no environment, neutral lighting, simple round base."

    # Profesión y detalles adicionales
    profession_block = f"Profession: {profession}. Simple and appropriate outfit. No decorative excess." if profession.strip() else ""
    extra_block = extra_details if extra_details.strip() else ""

    # --------------------------------------------------
    # CHARACTER (DUAL STEP)
    # --------------------------------------------------
    if character_type == "Character":

        if not char_name:
            st.error("Please enter a character name.")
        else:
            st.markdown("---")
            st.subheader(f"🚀 Dual Step Workflow: {char_name}")

            # Paso 1: Generar imagen de referencia
            prompt_paso_1 = f"""IDENTITY ANCHOR: {char_name} (Official Design).
VISUAL SPECIFICATIONS: High-fidelity 1:1 replica. Focus on extremely detailed anatomical features, specific skin wrinkles, and iconic facial geometry.
STAGING: Neutral standing position, flat studio lighting, solid grey background. 
MANDATE: No cinematic effects, no artistic stylization. Keep it simple and recognizable as the original character."""

            st.info("1️⃣ **Paso 1: Generar Referencia Fiel** (Copia y genera esta imagen primero)")
            st.code(prompt_paso_1, language="text")

            # Paso 2: Conversión 3D con estilo de marca
            prompt_paso_2 = f"""ACT AS A 3D SCULPTOR: Use the attached simple reference of {char_name} as a 1:1 geometric template.
CONVERT TO: {BRAND_STYLE}
TECHNICAL: {TECH_BLOCK}
MANDATE: Preserve every facial wrinkle and proportion exactly as seen in the reference. Do not simplify the geometry. High-fidelity 3D printable model.
{profession_block}
{extra_block}"""

            st.write("---")
            st.info("2️⃣ **Paso 2: Conversión a 3D** (Adjunta la imagen del paso 1 y usa este prompt)")
            st.code(prompt_paso_2, language="text")

    # --------------------------------------------------
    # PERSON / ANIMAL (SINGLE STEP)
    # --------------------------------------------------
    else:
        st.markdown("---")
        st.subheader("📄 Single Step Prompt")

        # Definir descripción del sujeto según el tipo
        if character_type == "Person":
            subject_description = f"{gender} person"
        elif character_type == "Animal":
            subject_description = f"{animal_type} animal"
        else:
            subject_description = "Subject"

        prompt_unico = f"SUBJECT: {subject_description}.\n{BRAND_STYLE}\n{TECH_BLOCK}\n{profession_block}\n{extra_block}\n3D printable figurine."

        st.info("Haz clic para copiar el prompt:")
        st.code(prompt_unico, language="text")
