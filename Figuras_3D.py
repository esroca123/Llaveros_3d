import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="3D Character Generator Pro",
    layout="centered"
)

st.title("🧍‍♂️🦊⭐ 3D Character Generator")

st.markdown(
    "Generador de prompts para **figuras 3D imprimibles**, "
    "enfocado en fidelidad absoluta de personajes conocidos."
)

# --------------------------------------------------
# BRAND STYLE (ESTILO VISUAL)
# --------------------------------------------------
# Eliminamos palabras que sugieran "simplificación" para evitar pérdida de rasgos.
BRAND_STYLE = """
STYLE: Clean 3D digital sculpture, unpainted white material, matte resin finish. 
Technical 3D model. No textures, no paint. 
Designed strictly for 3D printing.
"""

TECHNICAL_CONTROL_BLOCK = """
CONTROL: Technical model, no background, isolated on white. 
No cinematic lighting, no environment, no decorative additions.
"""

BASE_BLOCK = """
BASE: Simple flat round base, plain cylinder, purely functional.
"""

# --------------------------------------------------
# UI – TYPE SELECTION
# --------------------------------------------------
character_type = st.selectbox(
    "Select what you want to create",
    ["Character", "Person", "Animal"]
)

# Inicialización de variables
base_character_block = ""
character_name = ""

if character_type == "Person":
    gender = st.selectbox("Gender", ["Male", "Female"])
    base_character_block = f"SUBJECT: Original human, {gender}. Neutral pose."

elif character_type == "Animal":
    animal_type = st.text_input("Type of animal", placeholder="e.g. fox, turtle...")
    base_character_block = f"SUBJECT: Anthropomorphic {animal_type}."

elif character_type == "Character":
    character_name = st.text_input(
        "Character name",
        placeholder="e.g. Master Oogway, Pikachu..."
    )
    base_character_block = f"SUBJECT: The official character '{character_name}' in its canon design."

# --------------------------------------------------
# OPTIONAL INPUTS
# --------------------------------------------------
profession = st.text_input("Profession / Pose (optional)")
extra_details = st.text_input("Extra details (optional)", placeholder="Objects, specific expression...")

# --------------------------------------------------
# GENERATE BUTTON (FINAL FIDELITY VERSION)
# --------------------------------------------------
generate = st.button("✨ Generate Master Prompt")

if generate:
    # Bloques de soporte
    profession_block = f"PROFESSION/POSTURE: {profession}." if profession.strip() else ""
    extra_details_block = f"ADDITIONAL DETAILS: {extra_details}." if extra_details.strip() else ""
    
    if character_type == "Character":
        if not character_name.strip():
            st.error("Please enter a character name.")
        else:
            # ESTRUCTURA DE ALTA FIDELIDAD (EL SANDWICH DE IDENTIDAD)
            final_prompt = f"""
### MANDATORY IDENTITY PROTOCOL: {character_name.upper()} ###
- CORE SUBJECT: You are sculpting the official, canon version of {character_name}.
- ANATOMICAL FIDELITY: Maintain 1:1 proportions. Do not simplify, do not stylize, and do not smooth out iconic features.
- KEY DETAILS: If {character_name} has wrinkles, scars, specific armor patterns, or organic textures, they MUST be present in the 3D sculpt.
- POSTURE: {profession_block}

### BRAND STYLE CONSTRAINTS (SECONDARY) ###
- MATERIAL: All-white unpainted resin/sculpture material.
- FINISH: Matte, clean technical 3D model look.
{BRAND_STYLE}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}

### FINAL VERIFICATION ###
- Is the face 100% recognizable as {character_name}? Yes.
- Are the anatomical details intact despite the white material? Yes.
{extra_details_block}
- FINAL OUTPUT: One 3D printable sculpture of {character_name}, high-fidelity.
"""
            st.subheader("📄 Prompt para Gemini / Nano Banana")
            st.text_area("Copia este texto:", final_prompt.strip(), height=500)
    
    else:
        # Prompt estándar para humanos y animales originales
        final_prompt = f"""
{base_character_block}
{BRAND_STYLE}
{profession_block}
{extra_details_block}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}
3D printable sculpture.
"""
        st.subheader("📄 Prompt para Gemini / Nano Banana")
        st.text_area("Copia este texto:", final_prompt.strip(), height=400)

