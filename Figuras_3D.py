import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="3D Character Generator - FDM Gap Edition",
    layout="centered"
)

st.title("🧍‍♂️🦊⭐ 3D Character Generator (FDM-Gap)")

st.markdown(
    "Generador de prompts para figuras **3D imprimibles**. "
    "Optimizado para poses naturales con **separación técnica (Gap)** para cortes por color."
)

# --------------------------------------------------
# ADVERTENCIA SUPERIOR
# --------------------------------------------------
st.warning(
    "⚠️ El sistema generará poses naturales pero asegurando un **pequeño espacio (gap)** "
    "entre brazos y torso para permitir cortes perpendiculares limpios."
)

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
char_name = ""
gender = ""
animal_type = ""

if character_type == "Person":
    gender = st.selectbox("Gender", ["Male", "Female"])
elif character_type == "Animal":
    animal_type = st.text_input("Type of animal", placeholder="e.g. fox, bear...")
elif character_type == "Character":
    char_name = st.text_input("Character name", placeholder="e.g. Mario, Batman...")

# --------------------------------------------------
# OPTIONAL INPUTS
# --------------------------------------------------
profession = st.text_input("Profession (optional)", placeholder="e.g. explorer, wizard...")
extra_details = st.text_input("Extra details (optional)", placeholder="e.g. holding a staff, smiling...")

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
if st.button("✨ Generate Prompt with Technical Gap"):

    # --- BLOQUE DE ESTILO Y REGLAS TÉCNICAS ---
    BRAND_STYLE = "STYLE: Clean 3D digital sculpture, unpainted white resin material, matte finish."
    
    # Aquí definimos la regla del GAP para poses naturales
    FDM_GAP_RULE = (
        "TECHNICAL REQUIREMENT: Ensure a mandatory small gap (minimum clearance) between the arms and the torso. "
        "Even in natural poses, limbs MUST NOT touch the body. There must be visible empty space "
        "to allow for clean perpendicular planar cuts in 3D software. No intersections."
    )
    
    TECH_BLOCK = "CONTROL: Isolated on white background, neutral studio lighting, simple round base."

    profession_block = f"Profession: {profession}." if profession.strip() else ""
    extra_block = extra_details if extra_details.strip() else ""

    # --------------------------------------------------
    # CASE: CHARACTER (DUAL STEP)
    # --------------------------------------------------
    if character_type == "Character":
        if not char_name:
            st.error("Please enter a character name.")
        else:
            st.markdown("---")
            st.subheader(f"🚀 Dual Step Workflow: {char_name}")

            # Paso 1: Referencia con Pose Natural + Gap
            prompt_paso_1 = f"""IDENTITY ANCHOR: {char_name}.
POSE: Natural and dynamic standing pose. 
CRITICAL: Maintain a subtle but clear physical gap between arms/hands and the torso. 
The limbs should be close to the body but never touching it. 
VISUALS: High-fidelity 1:1 replica, solid grey background, clear silhouettes."""

            st.info("1️⃣ **Paso 1: Generar Referencia con Separación**")
            st.code(prompt_paso_1, language="text")

            # Paso 2: Conversión
            prompt_paso_2 = f"""ACT AS A 3D SCULPTOR: Use the attached reference of {char_name}.
CONVERT TO: {BRAND_STYLE}
{FDM_GAP_RULE}
TECHNICAL: {TECH_BLOCK}
MANDATE: Keep the naturalistic pose but strictly enforce the air gap between the arms and the chest. 
Ensure the geometry is optimized for vertical/perpendicular slicing for multi-color FDM printing.
{profession_block}
{extra_block}"""

            st.write("---")
            st.info("2️⃣ **Paso 2: Conversión a 3D (Corte por Color)**")
            st.code(prompt_paso_2, language="text")

    # --------------------------------------------------
    # CASE: PERSON / ANIMAL (SINGLE STEP)
    # --------------------------------------------------
    else:
        st.markdown("---")
        st.subheader("📄 Single Step FDM Prompt")

        subject = f"{gender} person" if character_type == "Person" else f"{animal_type} animal"

        prompt_unico = (
            f"SUBJECT: {subject}.\n"
            f"POSE: Natural standing stance. Arms can be flexed or relaxed, but a visible gap must exist between limbs and torso.\n"
            f"{BRAND_STYLE}\n"
            f"{FDM_GAP_RULE}\n"
            f"{TECH_BLOCK}\n"
            f"{profession_block}\n"
            f"{extra_block}"
        )

        st.info("Prompt con Gap para corte perpendicular:")
        st.code(prompt_unico, language="text")
