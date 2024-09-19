import os
import re

ruta_origen = './paginas'
ruta_destino = './paginas_limpias'

os.makedirs(ruta_destino, exist_ok=True)

def guardarTexto(texto, nombre_archivo):
def guardarTexto(texto, nombre_archivo):
    """
    Guarda el texto en un archivo con el nombre proporcionado.

    Parameters:
    texto (str): El texto a guardar.
    nombre_archivo (str): El nombre del archivo donde se guardará el texto.

    Returns:
    None
    """
    with open(os.path.join(ruta_destino, nombre_archivo), 'w') as f:
        f.write(texto)
    with open(os.path.join(ruta_destino, nombre_archivo), 'w') as f:
        f.write(texto)

def limpiarTexto(texto, file):
def limpiarTexto(texto, file):
    """
    Cleans the given text by replacing occurrences of " \n" with a single space,
    and then saves the cleaned text to a file with the given name.

    Parameters:
    texto (str): The text to be cleaned.
    file (str): The name of the file where the cleaned text will be saved.

    Returns:
    None
    """
    texto = re.sub(r" \n", " ", texto)
    print(texto)
    guardarTexto(texto, file)
    texto = re.sub(r" \n", " ", texto)
    print(texto)
    guardarTexto(texto, file)   

def main():
def main():
    """
    Walks through the directory tree starting at ruta_origen and performs the following actions for each .txt file found:
    1. Constructs the full path of the file.
    2. Opens the file and reads its contents.
    3. Calls the limpiarTexto function with the file contents and the file name as arguments.

    Parameters:
    None

    Returns:
    None
    """
    for root, dirs, files in os.walk(ruta_origen):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    texto = f.read()
                    limpiarTexto(texto, file)
    for root, dirs, files in os.walk(ruta_origen):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    texto = f.read()
                    limpiarTexto(texto, file)      

if __name__ == '__main__':
    main()