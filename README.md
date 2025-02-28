# Proyecto-Criptografía
Aquí expongo dos programas de criptografía, usando los algoritmos de Cryptography y  Cryptodome.
Los requerimientos de ambos casos, son prácticamente iguales, sólo que la librería del cifrado cambia, ya que usamos otro algoritmo, pero el resto de pasos son iguales y la explicación la misma.

Si quieres hacerlo con Visual Studio Code, pero no te funciona, ya sea descargando las librerías o cuando ejecutas el comando para que arranque el app.py, entonces tendrás que revirsar el intérprete que tienes, si te da ese error puedes crear un nuevo intérprete, que éste te creará una nueva carpeta llamada .venv, en la cuál se descargarán las las librerías.


## Cryptography
Para poder visualizar este programa de forma correcta necesitamos hacer lo siguiente.
Lo primero que haremos, será, dentro de la carpeta proyecto_cryptography, abrir un terminal, en el cuál pondremos lo siguiente:
```
pip install streamlit
```
```
pip install cryptography
```
```
streamlit run app.py
```
Con éste último comando, crearemos una url local, por el puerto 8501, en la cuál tendremos una interfaz gráfica, tendremos que insertar un fichero txt que contenga texto plano, como es el caso del que pongo de ejemplo llamado texto_plano.txt.


## Pycryptodome
Para poder visualizar este programa de forma correcta necesitamos hacer lo siguiente.
Lo primero que haremos, será, dentro de la carpeta proyecto_pycryptodome, abrir un terminal, en el cuál pondremos lo siguiente:
```
pip install streamlit
```
```
pip install pycryptodome
```
```
streamlit run app.py
```
Con éste último comando, crearemos una url local, por el puerto 8501, en la cuál tendremos una interfaz gráfica, tendremos que insertar un fichero txt que contenga texto plano, como es el caso del que pongo de ejemplo llamado texto_plano.txt.

En éste, hay un cambio a la hora de crear el fichero con el texto cifrado, ya que Pycryptodome almacena la información del texto cifrado en binario, por ello si consultas el fichero, no podrás entender los caracteres.

## Autor
Antonio Valverde Soto