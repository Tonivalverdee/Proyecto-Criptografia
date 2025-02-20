# Importamos las librerías necesarias
import streamlit as st
import os

# Importamos las funciones de cifrado y descifrado
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Definimos el título de la página
st.title("Cifrado PyCryptography - Codificación y Decodificación")

# Si no existe texto_cifrado, crea la variable, pero sin información en su interior
if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

# Creamos para crear la variable clave, con un random:_byte de 16, si perdemos esta clave y almacenamos el texto cifrado, no podremos restaurarlo
if "clave" not in st.session_state:
    st.session_state.clave = get_random_bytes(16)

# En la variable nonce, no almacenamos nada, para poder crear la variable y poder usarla antes si generar conflicto
if "nonce" not in st.session_state:
    st.session_state.nonce = None

# En la variable tag, no almacenamos nada, para poder crear la variable y poder usarla antes si generar conflicto
if "tag" not in st.session_state:
    st.session_state.tag = None

# Guardamos en la variable archivo el archivo que se subirá
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_2")

# Si existe el archivo, pasará lo siguiente
if archivo:
    texto = archivo.read().decode("utf-8")  # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    st.text_area("Contenido del archivo:", texto, height=200)  # Mostramos el contenido en un área de texto
    st.session_state.texto_cifrado = texto # En la variable nueva, almacenamos la información de texto

    if st.button("Cifrar"):
        st.session_state.cipher = AES.new(st.session_state.clave, AES.MODE_EAX)
        st.session_state.texto_cifrado = texto.encode()
        st.session_state.cifrado, st.session_state.tag = st.session_state.cipher.encrypt_and_digest(st.session_state.texto_cifrado)
        st.session_state.nonce = st.session_state.cipher.nonce

        if not os.path.exists("archivos"):
            os.makedirs("archivos")

        with open("archivos/cifrado.txt", "wb") as f:
            f.write(st.session_state.cifrado)
        st.markdown(f"**Aquí texto cifrado:** `{st.session_state.cifrado}`")

    if st.button("Descifrar"):

        if st.session_state.texto_cifrado and st.session_state.nonce and st.session_state.tag:
            cipher_dec = AES.new(st.session_state.clave, AES.MODE_EAX, st.session_state.cipher.nonce)

            try:
                st.session_state.texto_descifrado = cipher_dec.decrypt(st.session_state.cifrado).decode()

                with open("archivos/descifrado.txt", "w") as f:
                    f.write(st.session_state.texto_descifrado)

                st.markdown(f"**Texto descifrado** `{st.session_state.texto_descifrado}`")

            except:
                st.error("Error: El texto cifrado no es válido o la clave es incorrecta")

        else:
            st.warning("No hay un texto cifrado válido para descifrar. Cifra un texto primero")