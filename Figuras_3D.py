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

Face and clothing inspired by the reference image,
fully adapted to the existing cartoon style.
Simplify all features.
No realism.
No textures.
No small details.

The character must clearly belong to the same brand universe.
"""

def animal_block(animal_type, personalized=False):
    if not animal_type:
        return ""
    animal_type = animal_type.lower().strip()
    return f"""
A cartoon version of a {animal_type}, standing on two legs like a human.
Slightly cute but mature style.
Simplified shapes, clean surfaces.
No textures or tiny details.
Stable base for 3D printing.
Easy to paint.
"""

def character_block(character_name):
    if not character_name:
        return ""
    character_name = character_name.strip()
    return f"""
A stylized cartoon reinterpretation of {character_name}.
Do not copy realism or exact original design.
Adapt the character to the brand's 3D cartoon style.
Simplify shapes and details.
No logos, no text, no trademarks.
Suitable for 3D printing and painting.
"""

# =========================
# PROMPT GENERATOR
# =========================

def generate_prompt(
    character_type,
    gender,
    hairstyle,
    profession,
    animal_type,
    character_name,
    personalized,
    extra_notes
):
    prompt = BASE_PROMPT
    prompt += f"\nCharacter type: {character_type}."

    # PROFESIÓN SIEMPRE OPCIONAL
    if profession:
        prompt += profession_block(profession)

    if character_type == "Human":
        prompt += f"\nCharacter gender: {gender}."
        if personalized:
            prompt += personalization_block()
        else:
            prompt += f"\nHairstyle: {hairstyle}, simple cartoon style."
            prompt += face_block_standard()

    elif character_type == "Animal":
        prompt += animal_block(animal_type, personalized)

    elif character_type == "Character":
        prompt += character_block(character_name)
        if personalized:
            prompt += personalization_block()

    if extra_notes:
        prompt += f"\nAdditional notes: {extra_notes}"

    return prompt.strip()

# =========================
# STREAMLIT UI
# =========================

st.set_page_config(page_title="3D Character Prompt Generator", layout="centered")
st.title("🧍‍♂️🦊⭐ 3D Character Prompt Generator")
st.write(
    "Create consistent prompts for humans, animals or specific characters. "
    "All outputs are optimized for 3D printing and painting."
)

st.divider()

# --- Controls ---

character_type = st.selectbox(
    "Character type",
    ["Human", "Animal", "Character"]
)

gender = "N/A"
hairstyle = "N/A"
animal_type = ""
character_name = ""
personalized = False

if character_type == "Human":
    gender = st.selectbox("Character gender", ["Male", "Female"])
    hairstyle = st.selectbox("Hairstyle (base style)", ["Short", "Medium", "Long", "Tied"])
    personalized = st.checkbox("Personalize using a photo reference")

elif character_type == "Animal":
    animal_type = st.text_input("Animal type (e.g. dog, cat, dragon)")
    personalized = st.checkbox("Personalize using a photo reference")

elif character_type == "Character":
    character_name = st.text_input("Character name (e.g. Pikachu, Mario, Batman)")
    personalized = st.checkbox("Adapt character using a reference image")

# PROFESIÓN SIEMPRE DISPONIBLE
profession = st.text_input(
    "Profession or role (optional)",
    placeholder="e.g. doctor, chef, warrior, gamer"
)

extra_notes = st.text_area(
    "Extra notes (optional)",
    placeholder="e.g. friendly pose, heroic stance, relaxed vibe"
)

st.divider()

# --- Generate ---

if st.button("Generate Prompt"):
    final_prompt = generate_prompt(
        character_type=character_type,
        gender=gender,
        hairstyle=hairstyle,
        profession=profession,
        animal_type=animal_type,
        character_name=character_name,
        personalized=personalized,
        extra_notes=extra_notes
    )
    st.subheader("Generated Prompt")
    st.text_area(
        "Copy this prompt and use it in your AI tool",
        final_prompt,
        height=480
    )