import os
import streamlit as st
import openai
from googletrans import Translator

# --- 1. SEGURIDAD DEVOPS ---
api_key = os.getenv("OPENAI_API_KEY")

# --- 2. CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(page_title="AI Trans Pro", page_icon="🌐")

with st.sidebar:
    st.image("logo_beta.png", width=150) if os.path.exists("logo_beta.png") else st.title("🌐 AI Trans")
    st.info("🚀 **Versión Beta v0.5.5**")
    
    # Si la clave es la de ejemplo o no está, pedimos la real
    if api_key and "sk-tu-clave" not in api_key:
        st.success("✅ IA Conectada")
        openai.api_key = api_key
    else:
        st.warning("⚠️ Falta Key de OpenAI")
        api_key = st.text_input("OpenAI API Key:", type="password")
        openai.api_key = api_key

    st.markdown("---")
    motor = st.selectbox("Motor:", ["Google (Gratis)", "OpenAI (GPT-4)"])

# --- 3. CUERPO PRINCIPAL ---
st.title("🌐 Traductor Pro Multi-Modo")
tab1, tab2, tab3 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

# Usamos session_state para que el texto persista entre pestañas
if "texto_capturado" not in st.session_state:
    st.session_state.texto_capturado = ""

with tab1:
    texto_usuario = st.text_area("Escribe o graba algo:", value=st.session_state.texto_capturado, height=150)

with tab2:
    st.write("### 🎙️ Grabadora de Voz")
    # Este es el componente que ya tienes funcionando en tu captura
    audio_file = st.audio_input("Haz clic para hablar")
    
    if audio_file:
        if st.button("Transcribir mi voz 🤖"):
            if not api_key or "sk-" not in api_key:
                st.error("Necesitas una API Key real para transcribir.")
            else:
                try:
                    with st.spinner("Whisper está procesando tu audio..."):
                        # Guardar el audio temporalmente
                        with open("temp_audio.wav", "wb") as f:
                            f.write(audio_file.read())
                        
                        # Llamada a la API de Whisper
                        with open("temp_audio.wav", "rb") as audio:
                            transcripcion = openai.audio.transcriptions.create(
                                model="whisper-1", 
                                file=audio
                            )
                        
                        st.session_state.texto_capturado = transcripcion.text
                        st.success(f"Texto detectado: {transcripcion.text}")
                        st.rerun() # Refresca para que el texto aparezca en la Tab 1
                except Exception as e:
                    st.error(f"Error de procesamiento: {e}")

with tab3:
    st.info("📸 Módulo de visión: Próximamente.")

# --- 4. TRADUCCIÓN ---
idioma_dest = st.selectbox("Idioma destino:", ["Spanish", "English", "French", "German"])

if st.button("TRADUCIR AHORA ✨"):
    texto_a_procesar = st.session_state.texto_capturado if not texto_usuario else texto_usuario
    if not texto_a_procesar:
        st.warning("Escribe o graba algo primero.")
    else:
        with st.spinner('Traduciendo...'):
            try:
                if motor == "Google (Gratis)":
                    res = Translator().translate(texto_a_procesar, dest=idioma_dest[:2].lower()).text
                else:
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": f"Translate to {idioma_dest}: {texto_a_procesar}"}]
                    )
                    res = response.choices[0].message.content
                st.success(f"### Resultado:\n{res}")
            except Exception as e:
                st.error(f"Hubo un problema: {e}")
