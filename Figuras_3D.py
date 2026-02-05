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
# BRAND STYLE
# --------------------------------------------------
BRAND_STYLE = """
Clean 3D cartoon character.
Slightly cute but adult-oriented.
Technical 3D model.
Smooth and simple surfaces.
No textures.
No micro details.
Unpainted white material.
Matte finish.
Designed strictly for 3D printing.
"""

# --------------------------------------------------
# TECHNICAL CONTROL
# --------------------------------------------------
TECHNICAL_CONTROL_BLOCK = """
This is a technical 3D model, not an illustration.
No artistic interpretation.
No cinematic lighting.
No dramatic pose.
No environment.
No background elements.
No decorative additions.
"""

# --------------------------------------------------
# BASE CONTROL
# --------------------------------------------------
BASE_BLOCK = """
Base:
Simple flat round base.
Plain cylinder.
No decoration.
No texture.
No engravings.
No patterns.
No symbols.
Purely functional base only.
"""

# --------------------------------------------------
# NUEVA LÓGICA DE BÚSQUEDA Y FIDELIDAD (OPTIMIZADA)
# --------------------------------------------------
CHARACTER_FIDELITY_BLOCK = """
CRITICAL STEP: Before generating, identify the official visual design of this character.
You must replicate the canonical facial structure, body proportions, and iconic silhouette.
This prompt is for a technical 3D reference: do not deviate from the original source.
Accuracy is mandatory for 3D printing.
"""

# --------------------------------------------------
# UI – TYPE SELECTION
# --------------------------------------------------
character_type = st.selectbox(
    "Select what you want to create",
    ["Person", "Animal", "Character"]
)

base_character_block = ""

if character_type == "Person":
    gender = st.selectbox("Gender", ["Male", "Female"])
    base_character_block = f"""
Original human character.
Gender: {gender}.
Neutral standing pose.
Friendly and calm expression.
"""

elif character_type == "Animal":
    animal_type = st.text_input(
        "Type of animal",
        placeholder="e.g. turtle, fox, cat..."
    )
    base_character_block = f"""
Anthropomorphic {animal_type} character.
Standing on two legs like a human.
Animal anatomy preserved.
"""

elif character_type == "Character":
    character_name = st.text_input(
        "Character name",
        placeholder="e.g. Master Oogway, Pikachu..."
    )
    # Aquí el cambio clave: forzamos a la IA a citar el personaje específico
    base_character_block = f"""
Existing fictional character: {character_name}.
Official design from its respective franchise.
Maintain exact canonical likeness.
"""

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
generate = st.button("✨ Generate prompt")

if generate:
    profession_block = ""
    if profession.strip():
        profession_block = f"Profession: {profession}.\nSimple outfit."

    reference_block = ""

    if character_type == "Character":
        if use_photo and photo_reference.strip():
            reference_block = f"Use this photo description: {photo_reference}"
        else:
            # Instrucción de búsqueda integrada en el prompt final
            reference_block = "Search your internal database for the most accurate visual reference of this character."

        final_prompt = f"""
{CHARACTER_FIDELITY_BLOCK}
{BRAND_STYLE}
{base_character_block}
{reference_block}
{profession_block}
{extra_details}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}
3D printable sculpture.
"""
    else:
        # Lógica original para Person y Animal
        if use_photo and photo_reference.strip():
            reference_block = f"Adapt this photo to cartoon: {photo_reference}"
        
        final_prompt = f"""
{BRAND_STYLE}
{base_character_block}
{reference_block}
{profession_block}
{extra_details}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}
3D printable sculpture.
"""

    st.subheader("📄 Final Prompt")
    st.text_area("Copy-ready prompt", final_prompt.strip(), height=380)
