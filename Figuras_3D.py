import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="3D Character Generator", layout="centered")

st.title("🧍‍♂️ FOX ⭐ 3D Character Generator")

# --------------------------------------------------
# BRAND & TECHNICAL BLOCKS
# --------------------------------------------------
BRAND_STYLE = "STYLE: Full body 3D digital sculpture, unpainted white resin material, matte finish. Technical model for 3D printing."
TECH_BLOCK = "CONTROL: Isolated on white background, no environment, neutral lighting, simple round base."

# --------------------------------------------------
# UI - SELECCIÓN Y CONFIGURACIÓN
# --------------------------------------------------
character_type = st.selectbox("Select type", ["Character", "Person", "Animal"])

# OPCIÓN DE REFERENCIA (IMPORTANTE)
use_image_ref = st.checkbox("Use photo reference description (optional)")

if character_type == "Character":
    char_name = st.text_input("Character name", placeholder="Master Oogway...")
    
    if use_image_ref:
        subject_block = f"SUBJECT: The character {char_name}. Use the attached image as the absolute reference for anatomy, proportions, and wrinkles."
    else:
        subject_block = f"SUBJECT: The official character {char_name}. Exact canon anatomy, original face wrinkles, and iconic silhouette."
else:
    detail = st.text_input("Description / Name")
    if use_image_ref:
        subject_block = f"SUBJECT: {detail}. Replicate the exact proportions and features shown in the attached photo."
    else:
        subject_block = f"SUBJECT: {detail}."

extra = st.text_input("Extra details (Pose, objects...)")

# --------------------------------------------------
# GENERADOR Y BOTÓN DE COPIADO RÁPIDO
# --------------------------------------------------
if st.button("✨ Generate Master Prompt"):
    if character_type == "Character" and not char_name:
        st.error("Please enter a name.")
    else:
        # Construcción del prompt
        ref_instruction = "PHOTO REFERENCE: Analyze the attached image carefully to replicate 1:1 geometry." if use_image_ref else ""
        
        if character_type == "Character":
            final_prompt = f"""{ref_instruction}
{subject_block}
{BRAND_STYLE}
{TECH_BLOCK}
DETAILS: {extra if extra else "Official outfit and signature objects."}
MANDATE: 100% fidelity. Do not simplify or add non-canon features. No extra hair or beards."""
        else:
            final_prompt = f"{ref_instruction}\n{subject_block}\n{BRAND_STYLE}\n{TECH_BLOCK}\n{extra}"

        st.subheader("📄 Prompt para Nano Banana")
        st.info("Haz clic en el icono de la derecha para copiar:")
        st.code(final_prompt.strip(), language="text")
        st.success("¡Prompt con referencia de imagen listo!")
