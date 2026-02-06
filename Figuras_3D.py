import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="3D Character Generator Pro", layout="centered")

st.title("🧍‍♂️ FOX ⭐ 3D Character Generator")

# --------------------------------------------------
# UI - SELECCIÓN DE TIPO (RESTAURADO)
# --------------------------------------------------
character_type = st.selectbox(
    "Select what you want to create",
    ["Character", "Person", "Animal"]
)

# Variables de control
subject_description = ""
extra_details = ""

if character_type == "Person":
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.selectbox("Age group", ["Child", "Adult", "Elderly"])
    profession = st.text_input("Profession (e.g. Warrior, Doctor)")
    extra_details = st.text_input("Special description (Physical traits, outfit)")
    subject_description = f"A {age} {gender} {profession}. {extra_details}"

elif character_type == "Animal":
    animal_kind = st.text_input("Type of animal", placeholder="e.g. Fox, Turtle, Lion")
    animal_traits = st.selectbox("Style", ["Natural", "Anthropomorphic (Human-like)"])
    extra_details = st.text_input("Special description (Pose, clothing)")
    subject_description = f"A {animal_traits} {animal_kind}. {extra_details}"

elif character_type == "Character":
    char_name = st.text_input("Character name", placeholder="e.g. Master Oogway")
    extra_details = st.text_input("Specific details (Pose, expression, objects)")
    subject_description = f"{char_name}. {extra_details}"

# --------------------------------------------------
# LÓGICA DE GENERACIÓN
# --------------------------------------------------
if st.button("✨ Generate Workflow / Prompt"):
    
    # ESTILO TÉCNICO BASE PARA EL PASO FINAL
    BRAND_STYLE = "STYLE: Clean 3D digital sculpture, unpainted white resin material, matte finish."
    TECH_BLOCK = "CONTROL: Isolated on white background, no environment, neutral lighting, simple round base."

    if character_type == "Character":
        if not char_name:
            st.error("Please enter a character name.")
        else:
            # FLUJO DE DOS PASOS PARA PERSONAJES
            st.markdown("---")
            st.subheader("🚀 Dual Step Workflow for Characters")
            
            # Paso 1: Identidad Visual
            st.info("1️⃣ **Step 1: Generate Visual Identity**\nUse this prompt to get the perfect reference:")
            p1 = f"GENERATE IDENTITY: Full color cinematic render of {char_name}. {extra_details if extra_details else 'Official canon appearance'}. 1:1 anatomical fidelity, highly detailed skin and textures, solid neutral background."
            st.code(p1, language="text")

            # Paso 2: Conversión a 3D
            st.info("2️⃣ **Step 2: 3D Translation**\nAttach the image from Step 1 and use this prompt:")
            p2 = f"3D TRANSLATION: Use the attached image as absolute geometry reference. Convert this exact character into a {BRAND_STYLE} {TECH_BLOCK} Maintain 100% of facial wrinkles and canonical proportions."
            st.code(p2, language="text")
    
    else:
        # PROMPT ÚNICO PARA PERSONAS Y ANIMALES (Lógica original)
        st.markdown("---")
        st.subheader("📄 Single Step Prompt")
        final_prompt = f"SUBJECT: {subject_description}.\n{BRAND_STYLE}\n{TECH_BLOCK}\n3D printable figurine."
        st.code(final_prompt.strip(), language="text")
        st.success("Prompt generated successfully!")
