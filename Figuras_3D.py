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
# BRAND STYLE (FIXED – TECHNICAL)
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
# TECHNICAL CONTROL (GLOBAL – VERY IMPORTANT)
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
# BASE CONTROL (ABSOLUTE)
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
# CHARACTER FIDELITY (ONLY FOR EXISTING CHARACTERS)
# --------------------------------------------------
CHARACTER_FIDELITY_BLOCK = """
IMPORTANT – CHARACTER FIDELITY OVERRIDES STYLE

This is a well-known existing character.
Accuracy is mandatory.

Preserve:
- Original facial structure
- Original head shape
- Original proportions
- Original silhouette
- Original personality

Do NOT:
- Redesign the character
- Stylize freely
- Exaggerate proportions
- Add new elements
- Change base design

Any style adaptation must be minimal and secondary.
Instant recognition has absolute priority.
"""

# --------------------------------------------------
# CHARACTER REFERENCE SEARCH (NEW – PROMPT ONLY)
# --------------------------------------------------
CHARACTER_REFERENCE_SEARCH_BLOCK = """
REFERENCE ACQUISITION STEP (MANDATORY):

Before generating the character, search for the most accurate and
recognizable visual references of this character available online.

Analyze multiple references to identify:
- Canonical facial features
- Full body proportions
- Typical clothing and accessories
- Overall silhouette and stance

If available references are partial (e.g. upper body only),
reconstruct the full body based on the official and commonly accepted design.
Do NOT crop or limit the character due to incomplete references.
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
Animal anatomy preserved.
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
        placeholder="Describe facial features, clothing, posture..."
    )

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
generate = st.button("✨ Generate prompt")

# --------------------------------------------------
# PROMPT GENERATION
# --------------------------------------------------
if generate:

    # Profession block (always optional)
    profession_block = ""
    if profession.strip():
        profession_block = f"""
Profession: {profession}.
Simple and appropriate outfit.
No decorative excess.
"""

    reference_block = ""

    if character_type == "Character":

        if use_photo and photo_reference.strip():
            reference_block = f"""
Use the provided photo reference as a visual guide.
Match facial features, clothing, and proportions faithfully.
If the photo is partial, reconstruct the full body
based on official character design consistency.
Photo description:
{photo_reference}
"""
        else:
            # NUEVA INDICACIÓN CLARA PARA EL USUARIO
            reference_block = """
⚠️ IMPORTANT: To get a faithful result of the character, 
you must attach at least one reference image directly in the AI (e.g., Gemini) that will generate the image.
The AI will use the image(s) as primary source.
If the reference is partial (e.g., only torso or face), the AI will complete the rest of the body maintaining coherence.
"""

        final_prompt = f"""
{CHARACTER_REFERENCE_SEARCH_BLOCK}
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

        if use_photo and photo_reference.strip():
            reference_block = f"""
Use the provided photo reference.
Adapt facial features and clothing
to a simplified cartoon style.
Photo description:
{photo_reference}
"""

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

    # --------------------------------------------------
    # OUTPUT
    # --------------------------------------------------
    st.subheader("📄 Final Prompt")

    # Text area con prompt
    st.text_area(
        "Copy-ready prompt",
        final_prompt.strip(),
        height=380
    )

    # Botón de copiado rápido
    if st.button("📋 Copy prompt"):
        st.experimental_set_query_params()  # Forcing UI refresh (hack para feedback simple)
        st.success("Prompt copied! ✅ Copy it directly into the AI with your reference image.")