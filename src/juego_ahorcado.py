import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena:str)->str:
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower().strip()
    cadena = cadena.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return cadena.replace("ü","u")


def enmascarar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    res = ""
    for c in palabra_secreta:
        if c in letras_usadas:
            res += c
        else:    
            res += "_"
    return res 


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if "_" in palabra_enmascarada:
        return False
    else: 
        return True

def mostrar_estado(palabra_enmascarada,letras_usadas,intentos):
    espacio = " ".join(palabra_enmascarada)
    if letras_usadas == "":
        letras_mostrar = "Letras usadas: ninguna"
    else:
        letras_mostrar = letras_usadas

    print(f"Estado: {espacio}")
    print(f"Letras usadas: {letras_mostrar}")
    print(f"Intentos restantes: {intentos}")

def pedir_letra(letras_usadas):
    intro=input("Introduce una letra:")
    if not intro.isalpha():
        return "Debes introducir una letra"
    elif len(intro) != 1:
        return "Debes introducir una única letra"
    elif intro.lower() in letras_usadas.lower():
        return "Esa letra ya la has usado"
    else:
        return intro.lower()

def jugar(palabra_secreta,intentos):







    
# TODO: Escribe el programa principal
