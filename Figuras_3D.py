import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="3D Character Generator Pro", layout="centered")

st.title("🧍‍♂️ FOX ⭐ 3D Character Generator")

# --------------------------------------------------
# BRAND STYLE - Bloque de protección de estilo
# --------------------------------------------------
BRAND_STYLE = "STYLE: High-end 3D digital sculpt, matte white resin material, unpainted. Clean surfaces but with 100% detail retention."
TECH_BLOCK = "CONTROL: Isolated on white, neutral studio lighting, no environment. Simple circular base."

# --------------------------------------------------
# UI
# --------------------------------------------------
character_type = st.selectbox("Select type", ["Character", "Person", "Animal"])
use_image_ref = st.checkbox("Use photo reference (CRITICAL FIDELITY)")

if character_type == "Character":
    char_name = st.text_input("Character name", placeholder="Master Oogway...")
    
    # Este es el bloque que funcionó: Mezcla de nombre + detalles específicos
    if use_image_ref:
        subject_block = f"SUBJECT: {char_name}. Use the attached photo as the PRIMARY GEOMETRY REFERENCE. Replicate the exact face, wrinkles, and body proportions shown in the image."
    else:
        subject_block = f"SUBJECT: The official {char_name}. Focus on highly detailed facial wrinkles, aged skin texture, and accurate canon proportions."
else:
    detail = st.text_input("Description / Name")
    subject_block = f"SUBJECT: {detail}."

extra = st.text_input("Extra details (Pose, objects...)")

# --------------------------------------------------
# GENERADOR Y COPIADO RÁPIDO
# --------------------------------------------------
if st.button("✨ Generate Master Prompt"):
    if character_type == "Character" and not char_name:
        st.error("Please enter a name.")
    else:
        # Re-introducimos el "Mandato de Identidad" que funcionó al principio
        if character_type == "Character":
            final_prompt = f"""
### MANDATE: ABSOLUTE FIDELITY ###
{subject_block}

### STYLE & MATERIAL ###
{BRAND_STYLE}
{TECH_BLOCK}

### CHARACTER ANCHOR ###
- Character: {char_name}
- Pose: {extra if extra else "Standard iconic pose"}
- Rule: Do not simplify the geometry. If the reference image has wrinkles or complex shapes, they must be sculpted in the 3D model.
- Final Look: A professional 3D printable figurine that looks exactly like {char_name}.
"""
        else:
            final_prompt = f"{subject_block}\n{BRAND_STYLE}\n{TECH_BLOCK}\n{extra}"

        st.subheader("📄 Prompt para Nano Banana")
        st.info("Copia el código y recuerda adjuntar la imagen real en el chat de la IA.")
        st.code(final_prompt.strip(), language="text")
