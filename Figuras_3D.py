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
# BRAND STYLE (FIXED)
# --------------------------------------------------
BRAND_STYLE = """
Clean 3D cartoon character.
Slightly cute but adult-oriented.
Smooth and simple surfaces.
No textures.
No tiny details.
Unpainted white 3D model.
Matte finish.
Designed for easy painting.
Stable proportions for 3D printing.
"""

# --------------------------------------------------
# CHARACTER FIDELITY BLOCK (ONLY FOR EXISTING CHARACTERS)
# --------------------------------------------------
CHARACTER_FIDELITY_BLOCK = """
IMPORTANT:
This is an existing and recognizable character.

Preserve original identity, silhouette,
facial structure, head shape, eyes,
posture and personality.

Do NOT redesign the character.
Do NOT exaggerate proportions.
Do NOT reinterpret the style.

If adapting to a cartoon style:
Only simplify shapes without losing identity.

The character must remain instantly recognizable.
"""

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
Animal features preserved.
"""

elif character_type == "Character":
    character_name = st.text_input(
        "Character name",
        placeholder="e.g. Master Oogway, Pikachu..."
    )
    base_character_block = f"""
Existing fictional character: {character_name}.
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
        placeholder="Describe facial features, hairstyle, clothing..."
    )

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
generate = st.button("✨ Generate prompt")

# --------------------------------------------------
# PROMPT GENERATION
# --------------------------------------------------
if generate:

    profession_block = ""
    if profession.strip():
        profession_block = f"""
Profession: {profession}.
Simple and appropriate outfit.
"""

    reference_block = ""

    if character_type == "Character":
        if use_photo and photo_reference.strip():
            reference_block = """
Use the provided photo reference.
Faithfully adapt facial features, clothing,
and proportions.
Simplify only where needed for 3D printing.
"""
        else:
            reference_block = """
Use the most accurate and recognizable visual references
of this character as commonly found online.
Stay faithful to the original design.
"""

        final_prompt = f"""
{CHARACTER_FIDELITY_BLOCK}
{BRAND_STYLE}
{base_character_block}
{reference_block}
{profession_block}
{extra_details}

3D printable sculpture.
Stable base.
"""
    else:
        if use_photo and photo_reference.strip():
            reference_block = """
Use the provided photo reference.
Adapt facial features and clothing
to a simplified cartoon style.
"""

        final_prompt = f"""
{BRAND_STYLE}
{base_character_block}
{reference_block}
{profession_block}
{extra_details}

3D printable sculpture.
Stable base.
"""

    # --------------------------------------------------
    # OUTPUT
    # --------------------------------------------------
    st.subheader("📄 Final Prompt")

    st.text_area(
        "Copy-ready prompt",
        final_prompt.strip(),
        height=350
    )

    st.markdown("⬆️ *You can copy the full prompt directly from the box above.*")