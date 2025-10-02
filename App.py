import streamlit as st

# Título de la app
st.title("Llavero Prompts Generator")
st.markdown("Crea prompts detallados para generar diseños de llaveros únicos con IA.")

# --- Contenedor para la entrada de datos (siempre visible) ---
with st.container():
    st.subheader("🛠️ Personaliza tu colección de llaveros")

    # Definición de estilos
    estilos_especificos = ["Anime/Manga Style", "Cartoon", "Realistic", "8-bit", "16-bit"]
    estilos_generales = ["Minimalist", "Futurist", "Vintage", "Cyberpunk", "Steampunk", "Art Deco"]
    estilos_adicionales = ["Kawaii", "Pop Art", "Gothic", "Surrealist", "Glass-like", "Metallic", "Wood-carved", "Clay-sculpted", "Flat Design", "Geometric", "Vaporwave", "Cottagecore"]
    estilos_nuevos_tematicos = ["Gamer / Arcade", "Floral / Nature", "Mandala / Zen", "Iconographic", "Cultural / Ethnic", "Urban / Graffiti", "Sporty", "Disney / Pixar", "Color Splash", "Lego", "Ghibli"]
    
    # NUEVO ESTILO COMBINABLE
    estilo_iconic_chibi_cartoon = "Iconic Chibi Cartoon"
    todos_los_estilos = [estilo_iconic_chibi_cartoon] + estilos_especificos + estilos_generales + estilos_adicionales + estilos_nuevos_tematicos

    # Selectbox principal
    estilo_seleccionado = st.selectbox(
        "Estilo de la colección de llaveros",
        ["Initial of a word", "Free Style", "A partir de una imagen", "Full Name/Phrase"] + todos_los_estilos
    )

    # Campo para la descripción de la colección
    descripcion_coleccion = st.text_area(
        "Descripción de la colección",
        placeholder="Describe el tema o concepto para los cuatro diseños (ej., 'cuatro animales de la selva', 'vehículos de carreras')."
    )

    # NUEVOS CAMPOS PARA PERSONAJES Y BÚSQUEDA
    nombre_personajes = st.text_input(
        "Personajes/Figuras de Referencia (Opcional)",
        placeholder="Ej., 'Goku, Vegeta, Krilin', 'Pikachu, Bulbasaur, Charmander'. Separa los nombres por comas."
    )
    
    buscar_referencia = st.checkbox(
        "Activar Búsqueda de Referencia Online",
        help="Si está marcada, la IA utilizará referencias en línea o su conocimiento interno para asegurar la fidelidad visual de los personajes."
    )

    # Campo para detalles adicionales
    descripcion_opcional = st.text_area(
        "Detalles adicionales para cada diseño (opcional)",
        placeholder="Añade aquí detalles específicos sobre el estilo, personajes, etc. (ej., 'todos sonríen', 'ropa azul')."
    )
    
    # Nuevo campo para el soporte
    descripcion_soporte = st.text_area(
        "Descripción especial del soporte (opcional)",
        placeholder="Ej., 'con el nombre de Juan', 'diseñado como un árbol', 'con la fecha 2024'."
    )

    # Lógica para la opción de "Initial of a word"
    inicial_palabra = None
    estilo_inicial_seleccionado = None
    if estilo_seleccionado == "Initial of a word":
        inicial_palabra = st.text_input("Palabra para la inicial", placeholder="ej., Alexandra")
        estilo_inicial_seleccionado = st.selectbox("Estilo para la inicial", todos_los_estilos)

    # Lógica para la opción "A partir de una imagen"
    estilo_para_imagen_seleccionado = None
    if estilo_seleccionado == "A partir de una imagen":
        st.markdown("La imagen de referencia debe subirse a la IA de tu elección por separado.")
        estilo_para_imagen_seleccionado = st.selectbox("Estilo para aplicar a la imagen:", todos_los_estilos)

    # Lógica para la nueva opción "Full Name/Phrase"
    nombre_completo = None
    frase_integrada = None
    estilo_nombre_seleccionado = None
    if estilo_seleccionado == "Full Name/Phrase":
        nombre_completo = st.text_input("Nombre completo", placeholder="ej., María Fernanda")
        frase_integrada = st.text_input("Frase para integrar (opcional)", placeholder="ej., 'La mejor mamá del mundo'")
        estilo_nombre_seleccionado = st.selectbox("Estilo para el nombre", todos_los_estilos)

    # Campos opcionales
    cantidad_colores = st.selectbox("Cantidad de colores (opcional)", ["Cualquiera"] + list(range(1, 5)))
    colores_opciones = ["red", "blue", "green", "yellow", "black", "white", "gray", "purple", "pink", "orange"]
    colores_seleccionados = st.multiselect("Colores sugeridos (opcional)", colores_opciones, max_selections=4)

    icono = st.text_input("Icono o símbolo (opcional)", placeholder="ej., rayo, luna, flor")
    texto_opcional = st.text_input("Texto o frase (opcional)", placeholder="ej., 'Feliz cumpleaños'")

# --- Aquí se definen todos los prompts fijos y dinámicos antes del botón ---

# -------------------------------------------------------------------------
# PROMPTS FIJOS (Soportes, Variantes y Presentación)
# -------------------------------------------------------------------------

prompt_soporte_pared = (
    f"Create a highly **creative, innovative, and aesthetic wall-mounted stand** to hang four decorative designs. "
    f"The design must be a functional art piece that **reflects and complements the theme of the collection**, not just a simple hanger. "
    f"The design must have a flat back for easy mounting, be simple and stable, with minimal overhangs, making it suitable for easy 3D printing. "
    f"It must include four hooks or holes to hang the designs. "
    f"{descripcion_soporte}"
    f"The stand must be visible in its entirety. No designs should be attached yet."
)

prompt_soporte_pie = (
    f"Create a highly **creative, innovative, and aesthetic free-standing stand** to hold four decorative designs. "
    f"The design must be a functional art piece that **reflects and complements the theme of the collection**, not just a simple hanger. "
    f"The design must have a wide, stable base and a vertical
