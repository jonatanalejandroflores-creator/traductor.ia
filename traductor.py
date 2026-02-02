import os
import streamlit as st
import openai
from googletrans import Translator

# --- CONFIGURACIÓN DE SEGURIDAD ---
api_key_env = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Traductor Pro", page_icon="🌐")

# --- BARRA LATERAL LIMPIA ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3858/3858902.png", width=100)
    st.title("Configuración")
    st.info("🚀 **Versión Beta v0.6**")
    
    # Solo pedimos la clave si la de la nube no es válida
    if api_key_env and api_key_env.startswith("sk-"):
        st.success("✅ IA Conectada")
        api_key = api_key_env
    else:
        api_key = st.text_input("Introduce OpenAI API Key:", type="password")
    
    openai.api_key = api_key
    motor = st.selectbox("Motor:", ["Google (Gratis)", "OpenAI (GPT-4)"])
    st.markdown("---")
    st.caption("Desarrollado por Jonatan Alejandro Flores")

# --- CUERPO PRINCIPAL ---
st.title("🌐 Traductor Pro Multi-Modo")

if "texto_voz" not in st.session_state:
    st.session_state.texto_voz = ""

tab1, tab2, tab3 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen"])

with tab1:
    texto_input = st.text_area("Escribe aquí:", value=st.session_state.texto_voz, height=150)

with tab2:
    st.write("### Graba tu mensaje")
    audio_data = st.audio_input("Escuchando...")
    
    if audio_data and st.button("Convertir Voz a Texto 🤖"):
        try:
            with st.spinner("Procesando audio..."):
                # Solución al error de archivos: Usamos un nombre fijo
                with open("audio_temp.wav", "wb") as f:
                    f.write(audio_data.read())
                
                with open("audio_temp.wav", "rb") as f:
                    transcript = openai.audio.transcriptions.create(model="whisper-1", file=f)
                
                st.session_state.texto_voz = transcript.text
                st.success(f"Detectado: {transcript.text}")
                st.rerun()
        except Exception as e:
            st.error("Para usar voz necesitas una clave real de OpenAI (sk-...)")

# --- LÓGICA DE TRADUCCIÓN ---
idioma = st.selectbox("Destino:", ["Spanish", "English", "French", "German"])

if st.button("TRADUCIR AHORA ✨"):
    if not texto_input:
        st.warning("Escribe algo primero.")
    else:
        try:
            if motor == "Google (Gratis)":
                res = Translator().translate(texto_input, dest=idioma[:2].lower()).text
                st.success(res)
            else:
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": f"Translate to {idioma}: {texto_input}"}]
                )
                st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
