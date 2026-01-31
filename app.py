import streamlit as st
import sys
import io
from types import ModuleType

# --- 1. PARCHE CGI ---
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

# --- 2. IMPORTACIONES ---
from PIL import Image
import pytesseract
import openai
from googletrans import Translator
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder

# --- 3. CONFIGURACIÓN ---
st.set_page_config(page_title="Traductor Pro IA", page_icon="🌐", layout="centered")
st.title("🌐 Traductor Pro Multi-Modo")

with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("OpenAI API Key:", type="password")
    motor = st.selectbox("Motor:", ["Google (Gratis)", "ChatGPT (Premium)"])

# --- 4. INTERFAZ ---
tab1, tab2, tab3 = st.tabs(["⌨️ Texto/Canción", "🎤 Voz", "📸 Imagen (OCR)"])
texto_para_traducir = ""

with tab1:
    texto_manual = st.text_area("Escribe o pega aquí:", height=200, key="manual")
    if texto_manual:
        texto_para_traducir = texto_manual

with tab2:
    st.write("Graba tu voz:")
    audio_data = mic_recorder(start_prompt="Grabar 🎙️", stop_prompt="Detener 🛑", key='recorder')
    if audio_data:
        st.audio(audio_data['bytes'])
        st.info("Audio capturado.")

with tab3:
    archivo_imagen = st.file_uploader("Sube una imagen:", type=['png', 'jpg', 'jpeg'])
    if archivo_imagen:
        img = Image.open(archivo_imagen)
        st.image(img, caption="Imagen cargada", use_container_width=True)
        # Extraemos el texto y lo guardamos
        texto_detectado = pytesseract.image_to_string(img)
        st.text_area("Texto detectado:", value=texto_detectado, height=150)
        texto_para_traducir = texto_detectado

# --- 5. LÓGICA DE TRADUCCIÓN SIN ERRORES ---
st.divider()
dest_lang = st.selectbox("Idioma destino:", ["Spanish", "English", "French", "German"])
lang_codes = {"Spanish": "es", "English": "en", "French": "fr", "German": "de"}

if st.button("TRADUCIR AHORA ✨"):
    if texto_para_traducir and texto_para_traducir.strip():
        try:
            with st.spinner("Traduciendo..."):
                if motor == "ChatGPT (Premium)" and api_key:
                    client = openai.OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": f"Traduce al {dest_lang}: {texto_para_traducir}"}]
                    )
                    resultado_final = response.choices[0].message.content
                else:
                    # Motor de Google blindado
                    translator = Translator()
                    # No usamos desempaquetado con comas aquí
                    traduccion = translator.translate(texto_para_traducir, dest=lang_codes[dest_lang])
                    resultado_final = traduccion.text

                st.success("**Resultado:**")
                st.write(resultado_final)
                
                tts = gTTS(text=resultado_final, lang=lang_codes[dest_lang])
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                st.audio(fp)
        except Exception as e:
            st.error(f"Error técnico: {e}")
    else:
        st.warning("⚠️ No hay texto para traducir. Escribe algo o sube una imagen.")
