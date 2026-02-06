import streamlit as st
import numpy as np
from PIL import Image
from deep_translator import GoogleTranslator

# Configuración de página
st.set_page_config(page_title="Traductor Pro Multi-Modo", layout="wide")

# --- LÓGICA DE IDIOMAS (+100 AUTOMÁTICOS) ---
@st.cache_data # Para que no descargue la lista cada vez que tocas un botón
def obtener_idiomas():
    try:
        # Descarga la lista oficial de Google
        dict_soporte = GoogleTranslator().get_supported_languages(as_dict=True)
        # Convertimos a formato "Nombre": "código" (ej: "Spanish": "es")
        return {name.title(): code for name, code in dict_soporte.items()}
    except:
        return {"Spanish": "es", "English": "en", "French": "fr"}

idiomas_dict = obtener_idiomas()
lista_nombres = sorted(list(idiomas_dict.keys()))

# --- SIDEBAR (Configuración Original) ---
st.sidebar.image("logo_beta.png", width=150)
st.sidebar.title("Configuración")

openai_key = st.sidebar.text_input("OpenAI API Key:", type="password")
motor = st.sidebar.selectbox("Motor:", ["Google (Gratis)", "OpenAI (GPT-4)"])

st.sidebar.markdown("---")
st.sidebar.info("Versión Beta v0.5")
st.sidebar.info("Desarrollado por Jonatan Alejandro Flores")

# --- CUERPO PRINCIPAL ---
st.title("🌐 Traductor Pro Multi-Modo")

tabs = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

with tabs[0]:
    texto_origen = st.text_area("Escribe aquí:", height=150)
    
    # Selector con los +100 idiomas ordenados de la A a la Z
    idioma_nombre = st.selectbox("Idioma destino:", lista_nombres, 
                                 index=lista_nombres.index("Spanish") if "Spanish" in lista_nombres else 0)
    idioma_cod = idiomas_dict[idioma_nombre]
    
    if st.button("TRADUCIR AHORA ✨"):
        if texto_origen:
            if motor == "OpenAI (GPT-4)":
                if not openai_key:
                    st.error("❌ Ingresa tu API Key en la barra lateral.")
                else:
                    st.info("Conectando con OpenAI...")
            else:
                res = GoogleTranslator(source='auto', target=idioma_cod).translate(texto_origen)
                st.success(f"**Traducción ({idioma_nombre}):** {res}")

# --- SECCIÓN DE ÁLGEBRA (NumPy) ---
st.markdown("---")
st.header("📐 Laboratorio de Álgebra (NumPy)")
st.write("Carga los vectores de tu cuaderno para calcular el Producto Punto y Vectorial.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Vector A")
    ax = st.number_input("Ax", value=3.0)
    ay = st.number_input("Ay", value=-2.0)
    az = st.number_input("Az", value=1.0)
with col2:
    st.subheader("Vector B")
    bx = st.number_input("Bx", value=0.0)
    by = st.number_input("By", value=4.0)
    bz = st.number_input("Bz", value=-3.0)

if st.button("CALCULAR OPERACIONES 🧮"):
    vec_a = np.array([ax, ay, az])
    vec_b = np.array([bx, by, bz])
    
    punto = np.dot(vec_a, vec_b)
    vectorial = np.cross(vec_a, vec_b)
    
    st.divider()
    st.subheader("Resultados:")
    st.write(f"🔹 **Producto Punto:** {punto}")
    # Usamos 'rf' para evitar el Warning de los logs
    st.write(rf"🔹 **Producto Vectorial:** ({vectorial[0]}, {vectorial[1]}, {vectorial[2]})")
    
    if punto == 0:
        st.success("✅ ¡Los vectores son ortogonales!")
