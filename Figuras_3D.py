import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="3D Character Generator", layout="centered")

st.title("🧍‍♂️ FOX ⭐ 3D Character Generator")

# --------------------------------------------------
# BRAND STYLE - Simplificado al máximo para no estorbar
# --------------------------------------------------
BRAND_STYLE = "Pure white unpainted 3D resin sculpture style. Matte finish."
TECH_BLOCK = "Isolated on white background, simple round base, technical 3D model."

# --------------------------------------------------
# UI
# --------------------------------------------------
character_type = st.selectbox("Select type", ["Character", "Person", "Animal"])
use_image_ref = st.checkbox("Use photo reference description (High Priority)")

if character_type == "Character":
    char_name = st.text_input("Character name", placeholder="Master Oogway...")
    # Instrucción de Identidad Crítica
    if use_image_ref:
        subject_block = f"SCULPTURE: {char_name}. REPLICATE THE ATTACHED PHOTO 1:1. EXACT WRINKLES AND ANATOMY."
    else:
        subject_block = f"SCULPTURE: The official {char_name}. Masterfully detailed face, authentic wrinkles, iconic canon body proportions."
else:
    detail = st.text_input("Description / Name")
    subject_block = f"SCULPTURE: {detail}."

extra = st.text_input("Extra details (Pose, objects...)")

# --------------------------------------------------
# GENERADOR Y COPIADO RÁPIDO
# --------------------------------------------------
if st.button("✨ Generate Master Prompt"):
    if character_type == "Character" and not char_name:
        st.error("Please enter a name.")
    else:
        # Estructura de Prompt "Limpia" para evitar alucinaciones
        # Ponemos el sujeto PRIMERO y solo al final el estilo técnico
        if character_type == "Character":
            final_prompt = f"""{subject_block}
{extra if extra else ""}
{BRAND_STYLE}
{TECH_BLOCK}
MANDATE: 100% likeness. Do not modify the original character's face or body. No beards or hair unless they belong to {char_name}."""
        else:
            final_prompt = f"{subject_block}\n{extra}\n{BRAND_STYLE}\n{TECH_BLOCK}"

        st.subheader("📄 Prompt para Nano Banana")
        st.info("Copia este prompt y adjunta la imagen de referencia en la IA:")
        st.code(final_prompt.strip(), language="text")
