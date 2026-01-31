import streamlit as st
import sys
import io
from types import ModuleType

# --- PARCHE OBLIGATORIO (Línea 1-15) ---
try:
    import cgi
except ImportError:
    cgi = ModuleType('cgi')
    sys.modules['cgi'] = cgi

if not hasattr(cgi, 'parse_header'):
    def parse_header(line):
        import email.utils
        return email.utils.decode_params('; ' + line)[0]
    cgi.parse_header = parse_header
# ---------------------------------------

from PIL import Image
import pytesseract
import openai
from googletrans import Translator
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder

st.set_page_config(page_title="Traductor Pro IA", page_icon="🌐", layout="centered")

st.title("🌐 Traductor Pro Multi-Modo")

with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("OpenAI API Key:", type="password")
    motor = st.selectbox("Motor:", ["Google (Gratis)", "ChatGPT (Premium)"])

tab1, tab2, tab3 = st.tabs(["⌨️ Texto/Canción", "🎤 Voz", "📸 Imagen (OCR)"])
texto_para_traducir = ""

with tab1:
    texto_manual = st.text_area("Escribe o pega aquí:", height=200)
    if texto_manual: texto_para_traducir = texto_manual

with tab2:
    st.write("Graba tu voz:")
    audio_data = mic_recorder(start_prompt="Grabar 🎙️", stop_prompt="Detener 🛑", key='recorder')
    if audio_data:
        st.audio(audio_data['bytes'])
        st.info("Audio capturado.")
        # Nota: Aquí podrías añadir lógica de transcripción si tienes Whisper configurado

with tab3:
    archivo_imagen = st.file_uploader("Sube una imagen:", type=['png', 'jpg', 'jpeg'])
    if archivo_imagen:
        img = Image.open(archivo_imagen)
        st.image(img, caption="Imagen cargada", use_container_width=True)
        texto_para_traducir = pytesseract.image_to_string(img)
        st.text_area("Texto detectado:", value=texto_para_traducir)

st.divider()
dest_lang = st.selectbox("Idioma destino:", ["Spanish", "English", "French", "German"])
lang_codes = {"Spanish": "es", "English": "en", "French": "fr", "German": "de"}

git add app.py
git commit -m "fix: corregir error de desempaquetado de valores"
git push origin rama-arreglo-v1.0:main --force
