import os
import streamlit as st
import openai
from googletrans import Translator

# --- 1. SEGURIDAD ---
api_key = os.getenv("OPENAI_API_KEY")

# --- 2. CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AI Trans Pro", page_icon="🌐", layout="centered")

with st.sidebar:
    # Logo y versión (Limpiamos la redundancia aquí)
    st.image("logo_beta.png", width=150) if os.path.exists("logo_beta.png") else st.title("🌐 AI Trans")
    st.info("🚀 **Versión Beta v0.5.5**")
    
    # Lógica de detección de llave
    if api_key and "sk-tu-clave" not in api_key:
        st.success("✅ IA Conectada")
        openai.api_key = api_key
    else:
        st.warning("⚠️ Configura tu API Key Real en Secrets")
        api_key = st.text_input("O introduce Key manualmente:", type="password")
        openai.api_key = api_key

    st.markdown("---")
    motor = st.selectbox("Motor de traducción:", ["Google (Gratis)", "OpenAI (GPT-4)"])

# --- 3. CUERPO PRINCIPAL ---
st.title("🌐 Traductor Pro Multi-Modo")

# Usamos st.session_state para que el texto no se borre al cambiar de pestaña
if "texto_a_traducir" not in st.session_state:
    st.session_state.texto_a_traducir = ""

tab1, tab2, tab3 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

with tab1:
    # El área de texto ahora está conectada a la memoria de la app
    texto_usuario = st.text_area("Escribe o revisa el audio:", 
                                value=st.session_state.texto_a_traducir, 
                                height=150)

with tab2:
    st.write("### 🎙️ Grabadora de Voz")
    audio_file = st.audio_input("Haz clic para hablar") # El componente de tu captura
    
    if audio_file:
        if st.button("Transcribir Voz 🤖"):
            if not api_key or "sk-" not in api_key:
                st.error("Se requiere una API Key real para procesar audio.")
            else:
                try:
                    with st.spinner("Whisper está escuchando..."):
                        # Guardar temporalmente el audio
                        with open("temp.wav", "wb") as f:
                            f.write(audio_file.read())
                        
                        # Transcripción oficial de OpenAI
                        with open("temp.wav", "rb") as audio:
                            transcripcion = openai.audio.transcriptions.create(
                                model="whisper-1", 
                                file=audio
                            )
                        
                        # Guardamos el resultado en la memoria
                        st.session_state.texto_a_traducir = transcripcion.text
                        st.success(f"Texto detectado: {transcripcion.text}")
                        st.rerun() # Refresca para mostrar el texto en la Tab 1
                except Exception as e:
                    st.error(f"Error procesando audio: {e}")

with tab3:
    st.info("📸 Visión Artificial: Próximamente.")

# --- 4. ACCIÓN FINAL ---
idioma_dest = st.selectbox("Idioma destino:", ["Spanish", "English", "French", "German"])

if st.button("TRADUCIR AHORA ✨"):
    # Prioriza el texto que el usuario editó o el que vino de la voz
    final_text = texto_usuario if texto_usuario else st.session_state.texto_a_traducir
    
    if not final_text:
        st.warning("Escribe algo o graba un audio primero.")
    else:
        with st.spinner('Traduciendo...'):
            try:
                if motor == "Google (Gratis)":
                    res = Translator().translate(final_text, dest=idioma_dest[:2].lower()).text
                else:
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": f"Translate to {idioma_dest}: {final_text}"}]
                    )
                    res = response.choices[0].message.content
                st.success(f"### Resultado:\n{res}")
            except Exception as e:
                st.error(f"Error en traducción: {e}")
