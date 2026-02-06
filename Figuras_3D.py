import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="3D Character Generator", layout="centered")

st.title("🧍‍♂️ FOX ⭐ 3D Character Generator")

# --------------------------------------------------
# BRAND & TECHNICAL BLOCKS (ESTRUCTURA GANADORA)
# --------------------------------------------------
BRAND_STYLE = "STYLE: Full body 3D digital sculpture, unpainted white resin material, matte finish. Technical model for 3D printing."
TECH_BLOCK = "CONTROL: Isolated on white background, no environment, neutral lighting, simple round base."

# --------------------------------------------------
# UI - SELECCIÓN Y ENTRADA
# --------------------------------------------------
character_type = st.selectbox("Select type", ["Character", "Person", "Animal"])

if character_type == "Character":
    char_name = st.text_input("Character name", placeholder="Master Oogway...")
    # El secreto del 100%: Instrucción de anatomía canon y arrugas originales
    subject_block = f"SUBJECT: The official character {char_name}. Exact canon anatomy, original face wrinkles, and iconic silhouette."
else:
    detail = st.text_input("Description (e.g. A futuristic soldier)")
    subject_block = f"SUBJECT: {detail}."

extra = st.text_input("Extra details (Pose, objects...)")

# --------------------------------------------------
# GENERADOR Y BOTÓN DE COPIADO RÁPIDO
# --------------------------------------------------
if st.button("✨ Generate Master Prompt"):
    if character_type == "Character" and not char_name:
        st.error("Please enter a name.")
    else:
        # Construcción del prompt basada en la imagen exitosa
        if character_type == "Character":
            final_prompt = f"""{subject_block}
{BRAND_STYLE}
{TECH_BLOCK}
DETAILS: {extra if extra else "Official outfit and signature objects."}
MANDATE: High-fidelity likeness is the priority. Do not add non-canon features. No extra hair or beards unless original."""
        else:
            final_prompt = f"{subject_block}\n{BRAND_STYLE}\n{TECH_BLOCK}\n{extra}"

        st.subheader("📄 Prompt para Nano Banana")
        
        # EL BOTÓN DE COPIADO RÁPIDO: 
        # Al usar st.code, aparece el icono de copiar automáticamente
        st.info("Haz clic en el icono de la derecha para copiar:")
        st.code(final_prompt, language="text")
        
        # Opcional: Una confirmación visual adicional
        st.success("¡Prompt generado con éxito!")

