import os
import streamlit as st
import openai
from googletrans import Translator

# --- 1. CONFIGURACIÓN DE SEGURIDAD ---
# Intenta obtener la clave del sistema
api_key = os.getenv("OPENAI_API_KEY")

# --- 2. INTERFAZ Y ESTILO ---
st.set_page_config(page_title="AI Trans Pro", page_icon="🌐", layout="centered")

# Inyectar el manifest para PWA
st.markdown('<link rel="manifest" href="/manifest.json">', unsafe_allow_html=True)

with st.sidebar:
    st.image("logo_beta.png", width=150) if os.path.exists("logo_beta.png") else st.title("🌐 AI Trans")
    st.info("🚀 **Versión Beta v0.5.2**")
    
    # Si la clave en Secrets es válida (no es la de ejemplo), ocultamos el input
    if api_key and "sk-tu-clave" not in api_key:
        st.success("✅ Sistema: Conectado")
        openai.api_key = api_key
    else:
        st.warning("⚠️ Configura tu API Key Real")
        api_key = st.text_input("OpenAI API Key:", type="password", help="Pega tu clave sk-...")
        openai.api_key = api_key

    st.markdown("---")
    motor = st.selectbox("Motor de traducción:", ["Google (Gratis)", "OpenAI (GPT-4)"])
    idioma_dest = st.selectbox("Idioma destino:", ["Spanish", "English", "French", "German", "Italian"])

# --- 3. CUERPO DE LA APP ---
st.title("🌐 Traductor Pro Multi-Modo")

tab1, tab2, tab3 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

with tab1:
    # Usamos session_state para que el texto de voz aparezca aquí automáticamente
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""
    
    texto_usuario = st.text_area("Escribe aquí:", value=st.session_state.input_text, height=150)

with tab2:
    st.write("### Asistente de Voz")
    audio_data = st.audio_input("Graba tu mensaje")
    
    if audio_data:
        if st.button("Transcibir Audio 🔊"):
            if not api_key or "sk-" not in api_key:
                st.error("Se requiere una API Key real para procesar voz.")
            else:
                try:
                    with st.spinner("Whisper está escuchando..."):
                        # Guardar temporalmente
                        with open("temp.wav", "wb") as f:
                            f.write(audio_data.read())
                        
                        # Transcripción con OpenAI
                        with open("temp.wav", "rb") as f:
                            transcript = openai.audio.transcriptions.create(model="whisper-1", file=f)
                        
                        st.session_state.input_text = transcript.text
                        st.success(f"Texto detectado: {transcript.text}")
                        st.info("Vuelve a la pestaña 'Texto' para traducir.")
                except Exception as e:
                    st.error(f"Error de voz: {e}")

with tab3:
    st.info("Módulo de Visión Artificial: Próximamente.")

# --- 4. ACCIÓN DE TRADUCCIÓN ---
if st.button("TRADUCIR AHORA ✨"):
    texto_final = st.session_state.input_text if not texto_usuario else texto_usuario
    if not texto_final:
        st.warning("Escribe o graba algo primero.")
    else:
        try:
            with st.spinner('Traduciendo...'):
                if motor == "Google (Gratis)":
                    translator = Translator()
                    resultado = translator.translate(texto_final, dest=idioma_dest[:2].lower()).text
                else:
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": f"Translate to {idioma_dest}: {texto_final}"}]
                    )
                    resultado = response.choices[0].message.content
                
                st.success("### Resultado:")
                st.write(resultado)
        except Exception as e:
            st.error(f"Error en traducción: {e}")

st.markdown("---")
st.caption("Desarrollado por Jonatan Alejandro Flores | Creator Edition")
