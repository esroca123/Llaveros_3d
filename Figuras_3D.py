import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="3D Character Generator Pro",
    layout="centered"
)

st.title("🧍‍♂️🦊⭐ 3D Character Generator")

st.markdown(
    "Generador de prompts para **figuras 3D imprimibles**, "
    "con corrección de fidelidad anatómica para personajes conocidos."
)

# --------------------------------------------------
# BRAND STYLE (ESTILO VISUAL) - Ajustado para no borrar detalles
# --------------------------------------------------
BRAND_STYLE = """
STYLE: Clean 3D sculpture, unpainted white material, matte finish. 
Technical 3D model. No textures, no paint. 
Designed strictly for 3D printing.
"""

TECHNICAL_CONTROL_BLOCK = """
CONTROL: Technical model, no background, isolated on white. 
No cinematic lighting, no environment.
"""

BASE_BLOCK = """
BASE: Simple flat round base, plain cylinder, purely functional.
"""

# --------------------------------------------------
# UI – TYPE SELECTION
# --------------------------------------------------
character_type = st.selectbox(
    "Select what you want to create",
    ["Character", "Person", "Animal"]
)

base_character_block = ""
# Este bloque es el "escudo" que protege la anatomía del personaje
character_fidelity_protocol = ""

if character_type == "Person":
    gender = st.selectbox("Gender", ["Male", "Female"])
    base_character_block = f"SUBJECT: Original human, {gender}. Neutral pose."

elif character_type == "Animal":
    animal_type = st.text_input("Type of animal", placeholder="e.g. fox, turtle...")
    base_character_block = f"SUBJECT: Anthropomorphic {animal_type}."

elif character_type == "Character":
    character_name = st.text_input(
        "Character name",
        placeholder="e.g. Master Oogway, Pikachu..."
    )
    
    # EL CAMBIO CLAVE: Protocolo dinámico para cualquier personaje
    character_fidelity_protocol = f"""
    TARGET SUBJECT: {character_name}
    CRITICAL FIDELITY PROTOCOL (PRIORITY 1):
    - IDENTIFICATION: Use the official canon appearance of {character_name}.
    - ANATOMICAL INTEGRITY: You are forbidden from smoothing out unique character traits. 
    - Retain all specific wrinkles, skin folds, iconic facial expressions, and clothing geometry.
    - The 3D Style applies ONLY to the white material, NEVER to the character's original shape.
    - 1:1 Silhouette replica is mandatory.
    """
    base_character_block = f"SUBJECT: The official character '{character_name}' in its canon design."

# --------------------------------------------------
# OPTIONAL INPUTS
# --------------------------------------------------
profession = st.text_input("Profession (optional)")
extra_details = st.text_input("Extra details (optional)", placeholder="Pose, objects...")

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
generate = st.button("✨ Generate Master Prompt")

if generate:
    profession_block = f"PROFESSION: {profession}." if profession.strip() else ""
    
    if character_type == "Character":
        # ESTRUCTURA DE ALTA FIDELIDAD PARA PERSONAJES IP
        final_prompt = f"""
{character_fidelity_protocol}

{base_character_block}

REPRESENTATION RULES:
{BRAND_STYLE}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}

ADDITIONAL DETAILS:
{profession_block}
{extra_details}

FINAL MANDATE: This is a high-end collectible of {character_name}. 
The likeness must be 100% perfect. Any anatomical simplification is a failure.
3D printable sculpture.
"""
    else:
        # Prompt estándar para Personas o Animales originales
        final_prompt = f"""
{base_character_block}
{BRAND_STYLE}
{profession_block}
{extra_details}
{TECHNICAL_CONTROL_BLOCK}
{BASE_BLOCK}
3D printable sculpture.
"""

    st.subheader("📄 Prompt para Gemini / Nano Banana")
    st.text_area("Copia este texto:", final_prompt.strip(), height=450)
