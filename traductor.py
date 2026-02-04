import os
import streamlit as st
import openai
from googletrans import Translator

# --- CONFIGURACIÓN DE SEGURIDAD ---
api_key_env = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title="AI Trans Pro v1.1", page_icon="🌐")

# --- INICIALIZAR LA "CAJA DE MEMORIA" (HISTORIAL) ---
if "historial" not in st.session_state:
    st.session_state.historial = []

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("Configuración")
    st.info("🚀 Fase 2: Memoria Activa")
    
    # Lógica de la API Key
    if api_key_env and api_key_env.startswith("sk-"):
        api_key = api_key_env
    else:
        api_key = st.text_input("API Key:", type="password")
    
    openai.api_key = api_key
    motor = st.selectbox("Motor:", ["Google (Gratis)", "ChatGPT (Premium)"])

# --- CUERPO PRINCIPAL ---
st.title("🌐 AI Trans Pro")

# Definición de Pestañas
tab1, tab2, tab3, tab4 = st.tabs(["⌨️ Texto", "🎤 Voz", "📸 Imagen", "📜 Historial"])

with tab1:
    texto_input = st.text_area("Escribe aquí:", height=100, key="txt_input")

with tab2:
    st.write("### Grabadora")
    audio_data = st.audio_input("Habla ahora")

with tab3:
    st.write("📸 Próximamente: Traducción por cámara")

# --- LÓGICA DE TRADUCCIÓN (PROCESO) ---
idioma = st.selectbox("Traducir a:", ["English", "Spanish", "French", "German"])

if st.button("TRADUCIR AHORA ✨"):
    if texto_input:
        try:
            # 1. Ejecutar traducción
            if motor == "Google (Gratis)":
                res = Translator().translate(texto_input, dest=idioma[:2].lower()).text
            else:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": f"Translate to {idioma}: {texto_input}"}]
                )
                res = response.choices[0].message.content
            
            # 2. Mostrar resultado inmediato
            st.success(f"**Resultado:** {res}")
            
            # 3. GUARDAR EN LA CAJA DE MEMORIA (Tu dibujo)
            nueva_entrada = {"original": texto_input, "traducido": res, "idioma": idioma}
            st.session_state.historial.insert(0, nueva_entrada)
            
            # Forzar actualización para que aparezca en el historial
            st.rerun()
            
        except Exception as e:
            st.error(f"Error en el proceso: {e}")

# --- PESTAÑA DE HISTORIAL (La que faltaba) ---
with tab4:
    st.header("📜 Últimas Traducciones")
    if not st.session_state.historial:
        st.info("Aún no hay registros. ¡Haz tu primera traducción!")
    else:
        for i, item in enumerate(st.session_state.historial[:10]):
            with st.expander(f"🕒 {item['idioma']}: {item['original'][:20]}..."):
                st.write(f"**Original:** {item['original']}")
                st.write(f"**Traducción:** {item['traducido']}")
