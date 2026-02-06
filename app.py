import streamlit as st
import io

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Mi Nueva App",
    page_icon="🚀",
    layout="centered"
)

# --- 2. LÓGICA / CÁLCULOS (Zona Offline) ---
def procesar_datos(entrada):
    # Aquí es donde escribes tu "magia" o cálculos
    resultado = entrada.upper() # Ejemplo: convertir a mayúsculas
    return resultado

# --- 3. INTERFAZ DE USUARIO (UI) ---
st.title("🚀 Generador de Ideas")
st.write("---")

# Bloque de Entrada
usuario_input = st.text_input("Escribe algo para procesar:")

# Bloque de Acción
if st.button("Ejecutar Acción ✨"):
    if usuario_input:
        with st.spinner("Procesando..."):
            # Llamamos a la lógica
            final = procesar_datos(usuario_input)
            
            # Bloque de Salida
            st.success(f"**Resultado:** {final}")
    else:
        st.warning("⚠️ Por favor, escribe algo primero.")

# --- 4. BARRA LATERAL (Sidebar) ---
with st.sidebar:
    st.header("Configuración")
    st.info("Esta es una plantilla base para futuros proyectos.")
    st.caption("Desarrollado por Jonatan Alejandro Flores")
