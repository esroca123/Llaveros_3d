import streamlit as st

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

3D sculpture style, not illustration, not realistic.
"""

def face_block(personalized):
    if personalized:
        return """
Face inspired by the reference photo.
Slightly adapted facial features to resemble the person.
Keep the same cartoon style.
Do not create a realistic portrait.
"""
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
Simple shapes, no small details.
Easy to paint.
"""

def generate_prompt(gender, hairstyle, profession, personalized, extra):
    prompt = BASE_PROMPT
    prompt += f"\nCharacter gender: {gender}."
    prompt += f"\nHairstyle: {hairstyle}, simple cartoon style."
    prompt += face_block(personalized)
    prompt += profession_block(profession)
    if extra:
        prompt += f"\nAdditional details: {extra}"
    return prompt

st.title("3D Character Prompt Generator")

gender = st.selectbox("Gender", ["Male", "Female"])
hairstyle = st.selectbox("Hairstyle", ["Short", "Medium", "Long", "Tied"])
profession = st.text_input("Profession or role", placeholder="e.g. doctor, chef, teacher, gamer")
personalized = st.checkbox("Personalized face (photo reference)")
extra = st.text_area("Extra notes (optional)")

if st.button("Generate Prompt"):
    final_prompt = generate_prompt(gender, hairstyle, profession, personalized, extra)
    st.text_area("Generated Prompt", final_prompt, height=420)