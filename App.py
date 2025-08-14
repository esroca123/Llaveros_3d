import streamlit as st
from pathlib import Path

# ---------- CONFIGURACIÓN ----------
st.set_page_config(
    page_title="Generador de Prompts – Llaveros 3D",
    page_icon="🔑",
    layout="wide"
)

# Carpeta con iconos
ICON_DIR = Path("icons")
ICON_MAP = {
    "Initials Creative": "initials.png",
    "Mini Icons": "mini_icons.png",
    "Mini Worlds": "mini_worlds.png",
    "Geek Icons": "geek_icons.png",
    "Minimal Art": "minimal_art.png",
    "Mini Phrases": "mini_phrases.png",
    "Tiny Animals": "tiny_animals.png",
    "Shields & Crests": "shields_crests.png",
    "Travel Key": "travel_key.png",
}

# ---------- FUNCIÓN PARA GENERAR PROMPT ----------
def build_prompt(
    collection, name, style, shape, desc, palette, ring, engrave, layout, size
):
    ringTxt = (
        "Include a small metal-like ring and an integrated loop in the keychain design."
        if ring
        else "Do not show a ring; include only the keychain charm silhouette with a loop hole."
    )
    engraveTxt = (
        "Allow a tiny back engraving area for text (do not show text)."
        if engrave
        else "No back engraving."
    )
    paletteTxt = (
        f"Use at most four flat colors: {palette}."
        if palette
        else "Use at most four flat, solid colors with high contrast."
    )

    orientationTxt = (
        "Compose a single image with two versions side by side: LEFT = full-color; RIGHT = pure black-and-white DXF-safe outline."
        if layout == "side-by-side"
        else "Compose a single image with two versions stacked vertically: TOP = full-color; BOTTOM = pure black-and-white DXF-safe outline."
    )

    prompt = f"""
Create ONE high-resolution image ({size}) that shows TWO versions of the same keychain design in a single canvas. {orientationTxt}

Project: "{collection}" — Keychain name: "{name}"
Style family: {style}. Shape: {shape}.
Design description: {desc}

COLOR VERSION (for layered 3D printing):
- Front view only, flat background, no perspective, no shadow.
- {paletteTxt}
- Clean low-relief look, smooth edges, no textures or gradients.
- Max 4 colors; emphasize crisp separation between color areas.
- {ringTxt}
- {engraveTxt}

BLACK-AND-WHITE VERSION (DXF-ready):
- Front view only, flat background.
- Crisp, single thin stroke lines (hairline/1px equivalent), uniform width.
- No fills, no shadows, no double lines, no hatching, no grayscale, no embossing.
- Continuous paths with clean intersections; avoid overlaps and inside duplicates.
- Identical proportions and composition to the color version.

General constraints:
- Keep the two versions perfectly aligned and proportionally identical.
- Center each version in its half of the canvas; leave generous margins; no cropping.
- Avoid text unless it was explicitly requested in the description.
- Output must be neat, minimal noise, and export-friendly for DXF.

Metadata (optional overlay OFF): collection, name, style, shape.
"""
    return prompt.strip()

# ---------- UI ----------
st.title("🔑 Generador de Prompts – Llaveros 3D")
st.markdown(
    "Crea prompts que muestren **una versión a color** y **otra en B/N optimizada para DXF** en una sola imagen."
)

with st.expander("📌 Instrucciones rápidas"):
    st.write("""
    1. Completa los campos.
    2. Mira el ícono de referencia del estilo.
    3. Pulsa **Generar**.
    4. Si quieres catálogo, usa la opción de duplicar prompt.
    """)

col1, col2 = st.columns([1, 1])
with col1:
    collection = st.text_input("Nombre de la colección", "Tiny Animals")
    name = st.text_input("Nombre del llavero", "Moon Cat")
    style = st.selectbox("Estilo del llavero", list(ICON_MAP.keys()))
    shape = st.selectbox(
        "Forma", ["round", "square", "hexagon", "rectangle", "custom silhouette"]
    )
    desc = st.text_area(
        "Descripción del llavero (en inglés)",
        "A minimalist cat silhouette with a tiny moon on the ear, cute, smooth edges.",
    )

with col2:
    palette = st.text_input("Paleta sugerida (máx. 4 colores, opcional)", "black, white, sky blue, beige")
    ring = st.checkbox("Incluir argolla y ojal", value=True)
    engrave = st.checkbox("Incluir grabado trasero pequeño", value=False)
    layout = st.selectbox(
        "Orientación de las dos versiones", ["side-by-side", "stacked"]
    )
    size = st.text_input("Tamaño objetivo", "1024x1024")
    multiplicar = st.number_input("Multiplicar prompt (ej. catálogo 3x3 = 9)", min_value=1, max_value=20, value=1)

# Mostrar icono del estilo
st.markdown("### 🎨 Referencia visual del estilo seleccionado")
icon_path = ICON_DIR / ICON_MAP[style]
if icon_path.exists():
    st.image(str(icon_path), width=250)
else:
    st.info("No hay ícono para este estilo todavía.")

# Botón para generar
if st.button("🚀 Generar prompt"):
    base_prompt = build_prompt(collection, name, style, shape, desc, palette, ring, engrave, layout, size)
    if multiplicar > 1:
        full_prompt = "\n\n".join([base_prompt for _ in range(multiplicar)])
    else:
        full_prompt = base_prompt

    st.success("✅ Prompt generado")
    st.code(full_prompt, language="text")
    st.download_button(
        label="💾 Descargar como TXT",
        data=full_prompt,
        file_name=f"{collection}_{name}_prompt.txt",
        mime="text/plain",
    )
