# 📘 Manual de Desarrollo: Traductor Creator Edition

Este documento resume la estructura y comandos clave utilizados para crear la App v0.5.

## 1. Configuración del Servidor (Debian)
Para preparar el entorno y Git:
- **Identidad:** `git config --global user.name "Tu Nombre"`
- **Seguridad:** Uso de Personal Access Tokens (PAT) en lugar de contraseñas.
- **Limpieza:** Archivo `.gitignore` para evitar subir basura (`.cache/`, `__pycache__/`).

## 2. Estructura de Archivos Críticos
- **traductor.py:** El código fuente (Interfaz Streamlit + Lógica IA).
- **requirements.txt:** Lista de librerías para el servidor (openai, gTTS, etc.).
- **packages.txt:** Motores del sistema (tesseract-ocr) necesarios para Linux.
- **logo_beta.png:** El activo visual de la marca.

## 3. Comandos de Git (Flujo de Trabajo)
Para subir cambios de forma segura:
1. `git add .`
2. `git commit -m "Descripción del cambio"`
3. `git push origin estable-v0.5:main --force` (Para actualizar la web inmediatamente).

## 4. Parches de Estabilidad (Python 3.13)
Se incluyó un parche manual en el código para la librería `cgi`, ya que fue eliminada en Python 3.13, lo que permite que `streamlit-mic-recorder` funcione sin errores.

## 5. UI & PWA (Móvil)
Se inyectó HTML mediante `st.markdown` para forzar el icono en dispositivos móviles usando etiquetas:
- `<link rel="apple-touch-icon" ...>`
- `<link rel="icon" ...>`
