# Importamos las librerías necesarias
import streamlit as st
import os

from cryptography.fernet import Fernet

st.title("Cifrado Cryptography - Codificación y Decodificación")

if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

if "clave" not in st.session_state:
    st.session_state.clave = Fernet.generate_key()

# Guardamos en la variable archivo el archivo que se subirá

archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_2")

if archivo:
    texto = archivo.read().decode("utf-8")  # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    st.text_area("Contenido del archivo:", texto, height=200)  # Mostramos el contenido en un área de texto
    st.session_state.texto_cifrado = texto
    if st.button("Cifrar"):
        st.session_state.cipher = Fernet(st.session_state.clave)
        st.session_state.cifrado = st.session_state.cipher.encrypt(texto.encode())
        if not os.path.exists("archivos"):
            os.makedirs("archivos")
        with open("archivos/cifrado.txt", "wb") as f:
            f.write(st.session_state.cifrado)
        st.markdown(f"**Aquí texto cifrado:** `{st.session_state.cifrado}`")
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado:
            st.session_state.cipher_dec = Fernet(st.session_state.clave)
            try:
                st.session_state.texto_descifrado = st.session_state.cipher_dec.decrypt(st.session_state.cifrado).decode()
                with open("archivos/descifrado.txt", "w") as f:
                    f.write(st.session_state.texto_descifrado)
                st.markdown(f"**Texto descifrado** `{st.session_state.texto_descifrado}`")
            except:
                st.error("Error: El texto cifrado no es válido o la clave es incorrecta")
        else:
            st.warning("No hay un texto cifrado válido para descifrar. Cifra un texto primero")