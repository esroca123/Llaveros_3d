import streamlit as st

# =========================
# BASE PROMPT (NO TOCAR)
# =========================

BASE_PROMPT = """
A clean 3D cartoon character designed for 3D printing.
Style is slightly cute but mature, suitable for both kids and adults.
Smooth, simple surfaces, no textures, no tiny details.
Unpainted white model, matte finish.
Friendly and calm expression.

Medium-sized head, balanced cartoon proportions.
Compact body, stable and solid.
Neutral standing pose, arms relaxed along the body.
Simplified hands and feet.
Flat and stable base.

3D sculpture style.
Not illustration.
Not realistic.
"""

# =========================
# PROMPT BLOCKS
# =========================

def face_block_standard():
    return """
Simple friendly face.
Soft rounded facial features.
Small nose and gentle smile.
Cartoon eyes, clean and minimal.
"""

def profession_block(profession):
    if not profession:
        return ""
    profession = profession.lower().strip()
    return f"""
Add a {profession} outfit.
Profession-related clothing and accessories only.
Simple shapes.
No logos, no text, no patterns.
Easy to paint.
Suitable for 3D printing.
"""

def personalization_block():
    return """
Use the same character style, proportions, and design language.
Do not change the overall look of the character.

Face, hairstyle, and clothing are inspired by the reference photo,
but fully adapted to match the existing cartoon style.
Simplify all features.
No realism.
No textures.
No small details.

Clothing inspired by the reference photo,
redesigned using simple cartoon shapes.
Easy to paint and suitable for 3D printing.

The character must clearly belong to the same brand universe.
"""

# =========================
# PROMPT GENERATOR
# =========================

def generate_prompt(
    gender,
    hairstyle,
    profession,
    personalized,
    extra_notes
):
    prompt = BASE_PROMPT
    prompt += f"\nCharacter gender: {gender}."

    if personalized:
        prompt += personalization_block()
    else:
        prompt += f"\nHairstyle: {hairstyle}, simple cartoon style."
        prompt += face_block_standard()
        prompt += profession_block(profession)

    if extra_notes:
        prompt += f"\nAdditional notes: {extra_notes}"

    return prompt.strip()

# =========================
# STREAMLIT UI
# =========================

st.set_page_config(page_title="3D Character Prompt Generator", layout="centered")

st.title("🧍‍♂️🧍‍♀️ 3D Character Prompt Generator")
st.write(
    "Generate consistent, brand-safe prompts for 3D printable characters. "
    "Designed for generic figures, professions, and photo-based personalization."
)

st.divider()

# --- Controls ---

gender = st.selectbox(
    "Character gender",
    ["Male", "Female"]
)

hairstyle = st.selectbox(
    "Hairstyle (base style)",
    ["Short", "Medium", "Long", "Tied"]
)

profession = st.text_input(
    "Profession or role (free text)",
    placeholder="e.g. doctor, chef, teacher, gamer, musician"
)

personalized = st.checkbox(
    "Personalize using a photo reference (face + clothing)"
)

extra_notes = st.text_area(
    "Extra notes (optional)",
    placeholder="e.g. calm personality, relaxed posture, friendly vibe"
)

st.divider()

# --- Generate ---

if st.button("Generate Prompt"):
    final_prompt = generate_prompt(
        gender=gender,
        hairstyle=hairstyle,
        profession=profession,
        personalized=personalized,
        extra_notes=extra_notes
    )

    st.subheader("Generated Prompt")
    st.text_area(
        "Copy this prompt and use it in your AI tool",
        final_prompt,
        height=450
    )