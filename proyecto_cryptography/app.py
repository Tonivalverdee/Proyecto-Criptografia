# Importamos las librerías necesarias
import streamlit as st
import os

# Importamos las funciones necesarias de la librería cryptography
from cryptography.fernet import Fernet

# Ahora definimos el título
st.title("Cifrado Cryptography - Codificación y Decodificación")

# Si la variable clave no existe, generará una clave dentro de esa variable con Fernet
if "texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Inicializamos una variable para guardar el texto cifrado

# Aquí, si la variable clave no existe, generará una clave dentro de esa variable con Fernet
if "clave" not in st.session_state:
    st.session_state.clave = Fernet.generate_key()

# Guardamos en la variable archivo el archivo que se subirá
archivo = st.file_uploader("Sube un archivo TXT", type=["txt"], key="file_uploader_2")

# Si el archivo no está vacío, se ejecutará el siguiente código
if archivo:
    texto = archivo.read().decode("utf-8")  # Leemos el contenido del archivo y lo decodificamos en formato UTF-8
    st.text_area("Contenido del archivo:", texto, height=200)  # Mostramos el contenido en un área de texto
    st.session_state.texto_cifrado = texto # En la variable texto_cifrado guardamos el texto del archivo

# Creamos el botón para cifrar
    if st.button("Cifrar"):
        st.session_state.cipher = Fernet(st.session_state.clave) # En la variable cipher almacenamos la clave
        st.session_state.cifrado = st.session_state.cipher.encrypt(texto.encode()) # Ciframos el texto usando la clave y texto.encode()

# Si no existe la carpeta archivo, la crea, en la que almacenaremos los ficheros con el texto cifrado y descifrado
        if not os.path.exists("archivos"):
            os.makedirs("archivos")

# Guardamos el texto cifrado en un archivo cifrado.txt
        with open("archivos/cifrado.txt", "wb") as f:
            f.write(st.session_state.cifrado)
        st.markdown(f"**Aquí texto cifrado:** `{st.session_state.cifrado}`")

# Creamos el botón descifrar
    if st.button("Descifrar"):
        if st.session_state.texto_cifrado: # Si existe la variable texto cifrado, se ejecuta lo siguiente
            st.session_state.cipher_dec = Fernet(st.session_state.clave) # En la variable cipher_dec almacenamos la clave de descifrado

# Si lo anterior se ha podido hacer, entonces se intenta lo que está dentro de try
            try:
                st.session_state.texto_descifrado = st.session_state.cipher_dec.decrypt(st.session_state.cifrado).decode() # En la variable texto_descifrado, almacenamos el texto descifrado usando la variable cipher_dec con el algoritmo de cifrado


                with open("archivos/descifrado.txt", "w") as f:
                    f.write(st.session_state.texto_descifrado)
                st.markdown(f"**Texto descifrado** `{st.session_state.texto_descifrado}`")

# Si el try no se ha podido realizar correctamente, se indica el error especificado
            except:
                st.error("Error: El texto cifrado no es válido o la clave es incorrecta")

# Si no existía la variable texto_cifrado, muestra el siguiente error
        else:
            st.warning("No hay un texto cifrado válido para descifrar. Cifra un texto primero")