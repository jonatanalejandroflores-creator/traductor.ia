import os
import streamlit as st
import openai
from googletrans import Translator

# --- SEGURIDAD DEVOPS ---
# Intentamos obtener la llave de la nube
api_key_env = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Trans Pro", page_icon="🌐", layout="centered")

# --- SIDEBAR PROFESIONAL (SIN REPETICIONES) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3858/3858902.png", width=80)
    st.title("Configuración")
    st.info("🚀 **Versión Beta v0.7**")
    
    # Lógica inteligente para la API Key
    if api_key_env and api_key_env.startswith("sk-"):
        st.success("✅ Conexión Protegida")
        api_key = api_key_env
    else:
        st.warning("⚠️ Introduce una clave válida")
        api_key = st.text_input("OpenAI API Key:", type="password", help="Debe empezar con sk-")
    
    openai.api_key = api_key
    motor = st.selectbox("Motor de IA:", ["Google (Gratis)", "ChatGPT (Premium)"])
    st.markdown("---")
    st.caption("Desarrollado por Jonatan Alejandro Flores")

# --- CUERPO PRINCIPAL ---
st.title("🌐 Traductor Pro Multi-Modo")

if "text_input" not in st.session_state:
    st.session_state.text_input = ""

tab1, tab2, tab3 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

with tab1:
    texto_final = st.text_area("Tu mensaje:", value=st.session_state.text_input, height=150)

with tab2:
    st.write("### 🎙️ Grabadora")
    audio_data = st.audio_input("Presiona para hablar")
    
    if audio_data and st.button("Convertir Audio 🤖"):
        if not api_key.startswith("sk-"):
            st.error("Error: Se requiere una clave real de OpenAI para usar la voz.")
        else:
            try:
                with st.spinner("Procesando voz..."):
                    # Guardado robusto para evitar el MediaFileStorageError
                    temp_name = "audio_input.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data.getbuffer())
                    
                    with open(temp_name, "rb") as f:
                        transcript = openai.audio.transcriptions.create(model="whisper-1", file=f)
                    
                    st.session_state.text_input = transcript.text
                    st.success("¡Voz capturada con éxito!")
                    st.rerun()
            except Exception as e:
                st.error(f"Error técnico: {e}")

# --- TRADUCCIÓN ---
idioma = st.selectbox("Traducir al:", ["Spanish", "English", "French", "German"])

if st.button("TRADUCIR AHORA ✨"):
    if not texto_final:
        st.warning("⚠️ Escribe o graba algo primero.")
    else:
        try:
            with st.spinner('Traduciendo...'):
                if motor == "Google (Gratis)":
                    res = Translator().translate(texto_final, dest=idioma[:2].lower()).text
                else:
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": f"Translate to {idioma}: {texto_final}"}]
                    )
                    res = response.choices[0].message.content
                st.success(f"### Resultado:\n{res}")
        except Exception as e:
            st.error("El motor falló. Verifica tu clave de OpenAI.")
