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
    "enfocado en fidelidad absoluta de personajes conocidos."
)

# --------------------------------------------------
# BRAND STYLE (ESTILO VISUAL)
# --------------------------------------------------
BRAND_STYLE = """
STYLE: Clean 3D sculpture, unpainted white material, matte finish. 
Technical 3D model with smooth surfaces. No textures, no micro-details. 
Designed strictly for 3D printing.
"""

# --------------------------------------------------
# TECHNICAL & BASE CONTROL
# --------------------------------------------------
TECHNICAL_CONTROL_BLOCK = """
CONTROL: Technical model, no background, isolated on white. 
No cinematic lighting, no environment, no decorative additions.
"""

BASE_BLOCK = """
BASE: Simple flat round base, plain cylinder, purely functional.
"""

# --------------------------------------------------
# NUEVO BLOQUE: SEARCH & FIDELITY (EL CAMBIO CLAVE)
# --------------------------------------------------
# Este bloque obliga a la IA a buscar y mantener la anatomía exacta.
CHARACTER_ANALYSIS_BLOCK = """
MANDATORY REFERENCE STEP:
1. Search and analyze the official design of the character.
2. REPLICATE EXACT ANATOMY: Maintain the specific facial structure, 
   eye shape, hand/paw configuration, and unique body elements 
   (like shells, horns, or armor) with 90% fidelity to the original.
3. DO NOT stylize or simplify the character's biological or iconic traits.
4. Accuracy of the character's unique silhouette is the highest priority.
"""

# --------------------------------------------------
# UI – TYPE SELECTION
# --------------------------------------------------
character_type = st.selectbox(
    "Select what you want to create",
    ["Character", "Person", "Animal"]
)

base_character_block = ""

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
    # Refuerzo del nombre y origen
    base_character_block = f"SUBJECT: The official character '{character_name}' in its canon design."

# --------------------------------------------------
# OPTIONAL INPUTS
# --------------------------------------------------
profession = st.text_input("Profession (optional)")
extra_details = st.text_input("Extra details (optional)", placeholder="Pose, objects...")

use_photo = st.checkbox("Use photo reference description (optional)")
photo_reference = ""
if use_photo:
    photo_reference = st.text_area("Describe the photo reference")

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
generate = st.button("✨ Generate Master Prompt")

if generate:
    profession_block = f"PROFESSION: {profession}." if profession.strip() else ""
    
    if character_type == "Character":
        # PROMPT CONSTRUÍDO PARA MÁXIMA FIDELIDAD
        final_prompt = f"""
{CHARACTER_ANALYSIS_BLOCK}
{base_character_block}
{BRAND_STYLE}
{photo_reference if use_photo else ""}
{profession_block}
{extra_details}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}
3D printable sculpture.
"""
    else:
        # Prompt estándar para creaciones originales
        final_prompt = f"""
{base_character_block}
{BRAND_STYLE}
{photo_reference if use_photo else ""}
{profession_block}
{extra_details}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}
3D printable sculpture.
"""

    st.subheader("📄 Prompt para Gemini / Nano Banana")
    st.text_area("Copia este texto:", final_prompt.strip(), height=400)
