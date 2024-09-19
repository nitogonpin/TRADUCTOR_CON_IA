import os
import re
import ollama

ruta_origen = './paginas_limpias'
ruta_destino = './paginas_traducidas'

os.makedirs(ruta_destino, exist_ok=True)

def traducir(texto):
  """
  Traducir un texto del ingles al espanol.

  Parameters
  ----------
  texto : str
    El texto a traducir.

  Returns
  -------
  str
    El texto traducido.
  """
  # Hacer una solicitud a la API de traduccion de Ollama
  response = ollama.chat(model='llama3.1:8b', messages=[
    {
      'role': 'user',
      'content': 'Te voy a proporciona un texto para traducir del ingles al espanol. Solo traduce. No respondas ni hagas comentarios. El texto es posible que contenga errores o fragmentos de codigo. En ese caso, ignora los mismos.' + texto,
    },
  ])
  # Devolver el resultado de la traduccion
  return response['message']['content']

def main():
    """
    Iterar sobre los archivos de la carpeta especificada y traducir
    cada archivo. Luego, guardar el resultado en una carpeta
    diferente.
    """
    for root, dirs, files in os.walk(ruta_origen):
        for file in files:
            texto_a_insertar = ""
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    texto = f.readlines()
                    for linea in texto:
                        # Hacer una solicitud a la API de traduccion de Ollama
                        # y guardar el resultado en la variable traducion
                        traducion = traducir(linea)
                        # Imprimir el resultado para depurar
                        print(traducion)
                        # Agregar el resultado a la variable texto_a_insertar
                        texto_a_insertar += traducion

                # Abrir el archivo en la carpeta de destino
                with open(os.path.join(ruta_destino, file), 'w') as f:
                    # Escribir el resultado en el archivo
                    f.write(texto_a_insertar)

if __name__ == '__main__':
    main()
