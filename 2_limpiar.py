import os
import re

ruta_origen = './paginas'
ruta_destino = './paginas_limpias'


os.makedirs(ruta_destino, exist_ok=True)

def guardarTexto(texto, nombre_archivo):
    with open(os.path.join(ruta_destino, nombre_archivo), 'w') as f:
        f.write(texto)

def limparTexto(texto, file):
    texto = re.sub(r" \n", " ", texto)
    print(texto)
    guardarTexto(texto, file)
    

   

def main():
    for root, dirs, files in os.walk(ruta_origen):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    texto = f.read()
                    limparTexto(texto, file)
      

if __name__ == '__main__':
    main()