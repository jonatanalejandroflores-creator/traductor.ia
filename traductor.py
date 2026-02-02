import os
import streamlit as st
import openai
from googletrans import Translator

# --- 1. CONFIGURACIÓN DE SEGURIDAD (DEVOPS) ---
api_key = os.getenv("OPENAI_API_KEY")

# --- 2. CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AI Trans Pro", page_icon="🌐", layout="centered")

# Inyectar Manifest para PWA
st.markdown('<link rel="manifest" href="/manifest.json">', unsafe_allow_html=True)

# --- 3. BARRA LATERAL (LIMPIA) ---
with st.sidebar:
    # Logo y Versión (Solo una vez)
    st.image("logo_beta.png", width=150) if os.path.exists("logo_beta.png") else st.title("🌐 AI Trans")
    st.info("🚀 **Versión Beta v0.5**")
    
    st.markdown("### Configuración")
    
    # Lógica de Seguridad Inteligente
    if api_key:
        st.success("✅ Conectado a OpenAI")
        openai.api_key = api_key
    else:
        api_key = st.text_input("OpenAI API Key:", type="password", help="Introduce tu clave para activar GPT-4")
        openai.api_key = api_key

    motor = st.selectbox("Motor:", ["Google (Gratis)", "OpenAI (GPT-4)"])
    st.markdown("---")
    st.caption("👤 Creator Edition")
    st.caption("Desarrollado por Jonatan Alejandro Flores")

# --- 4. CUERPO PRINCIPAL ---
st.title("🌐 Traductor Pro Multi-Modo")

tab1, tab2, tab3 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

with tab1:
    texto_usuario = st.text_area("Escribe aquí:", height=150)

with tab2:
    st.info("Función de voz detectada. El audio capturado se procesará aquí.")
    # Aquí puedes añadir: audio_file = st.file_uploader("Subir audio", type=["mp3", "wav"])

with tab3:
    st.info("Sube una imagen o captura para traducir texto visual.")
    # Aquí puedes añadir: image_file = st.file_uploader("Subir imagen", type=["jpg", "png"])

idioma_dest = st.selectbox("Idioma destino:", ["Spanish", "English", "French", "German"])

# --- 5. ACCIÓN DE TRADUCCIÓN ---
if st.button("TRADUCIR AHORA ✨"):
    if not texto_usuario:
        st.warning("⚠️ Escribe algo para traducir.")
    else:
        try:
            with st.spinner('Traduciendo...'):
                if motor == "Google (Gratis)":
                    ts = Translator()
                    resultado = ts.translate(texto_usuario, dest=idioma_dest[:2].lower()).text
                else:
                    if not api_key:
                        st.error("❌ Necesitas una API Key para usar OpenAI.")
                        st.stop()
                    # Llamada a la API de OpenAI (Nueva Sintaxis)
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": f"Translate to {idioma_dest}: {texto_usuario}"}]
                    )
                    resultado = response.choices[0].message.content

                st.success("### Resultado:")
                st.write(resultado)
        except Exception as e:
            st.error(f"Error técnico: {e}")
