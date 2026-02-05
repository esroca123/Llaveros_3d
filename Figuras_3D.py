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
    "Generador de prompts para **figuras 3D imprimibles**, "
    "listas para pintar, personalizar o coleccionar."
)

# --------------------------------------------------
# STYLE PRESETS
# --------------------------------------------------
STYLE_PRESETS = {
    "Default Brand": """
Clean 3D cartoon character.
Slightly cute but mature.
Smooth surfaces, no textures.
Simple shapes, easy to paint.
Matte white unpainted 3D model.
Stable proportions for 3D printing.
""",

    "Minimal 3D Print": """
Ultra-clean 3D model.
Very minimal details.
Extremely smooth surfaces.
Optimized for easy painting and printing.
""",

    "Cute Chibi": """
Chibi-style cartoon character.
Cute and friendly appearance.
Simplified shapes.
IMPORTANT: Do not exaggerate proportions.
No oversized head or eyes.
""",

    "Semi-Adult Cartoon": """
Stylized cartoon character.
More mature proportions.
Soft expression.
Clean and modern look.
""",

    "Toy Figure": """
Collectible toy figure style.
Compact body.
Solid and stable stance.
Simple geometry.
""",

    "Animal Mascot": """
Friendly anthropomorphic mascot style.
Standing on two legs.
Clean shapes.
Brand-friendly look.
"""
}

# --------------------------------------------------
# CHARACTER FIDELITY BLOCK (ONLY FOR EXISTING CHARACTERS)
# --------------------------------------------------
CHARACTER_FIDELITY_BLOCK = """
IMPORTANT:
This is a well-known existing character.

Preserve the original identity, silhouette,
facial structure, head shape, eyes, posture,
and personality.

Do NOT redesign the character.
Do NOT change key proportions.
Do NOT modernize or reinterpret.

Style adjustments must be subtle.
If applying a cartoon or chibi style:
- No exaggeration
- No head enlargement
- No eye enlargement
- No body deformation

The character must remain instantly recognizable.
"""

# --------------------------------------------------
# UI – TYPE SELECTION
# --------------------------------------------------
character_type = st.selectbox(
    "Select character type",
    ["Person", "Animal", "Character"]
)

# --------------------------------------------------
# COMMON OPTIONS
# --------------------------------------------------
style_preset = st.selectbox(
    "Style preset",
    list(STYLE_PRESETS.keys())
)

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
# PROFESSION BLOCK (OPTIONAL ALWAYS)
# --------------------------------------------------
profession_block = ""
if profession.strip():
    profession_block = f"""
Profession: {profession}.
Appropriate simple outfit and accessories.
"""

# --------------------------------------------------
# PHOTO / REFERENCE BLOCK
# --------------------------------------------------
reference_block = ""

if character_type == "Character":
    if use_photo and photo_reference.strip():
        reference_block = f"""
Use the provided photo reference.
Faithfully adapt facial features, clothing and proportions.
Simplify only where needed for 3D printing.
"""
    else:
        reference_block = """
Use the most accurate and recognizable visual references
of this character as commonly found online.
Stay faithful to the original design.
"""

elif use_photo and photo_reference.strip():
    reference_block = f"""
Use the provided photo reference.
Adapt facial features and clothing.
Simplified cartoon interpretation.
"""

# --------------------------------------------------
# FINAL PROMPT ASSEMBLY
# --------------------------------------------------
if character_type == "Character":
    final_prompt = f"""
{CHARACTER_FIDELITY_BLOCK}
{STYLE_PRESETS[style_preset]}
{base_character_block}
{reference_block}
{profession_block}
{extra_details}

Unpainted white 3D model.
Matte finish.
Smooth surfaces.
No textures.
No tiny details.
Stable base.
3D printable sculpture.
"""
else:
    final_prompt = f"""
{STYLE_PRESETS[style_preset]}
{base_character_block}
{reference_block}
{profession_block}
{extra_details}

Unpainted white 3D model.
Matte finish.
Smooth surfaces.
No textures.
No tiny details.
Stable base.
3D printable sculpture.
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