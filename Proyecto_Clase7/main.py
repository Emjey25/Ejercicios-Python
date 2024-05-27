import random
import string
from paquetes import bd_palabras,diagramas

def obtener_palabra_aleatoria():
    try:
        palabra = random.choice(bd_palabras.bdPalabras).upper()
        return palabra
    except IndexError as e:
        # si la lista esta vacia , imprime un error y devuelve NONE
        print(f"Error al obtener palabra aleatoria: {e}")
        return None

def obtener_letra_usuario():
    while True:
        try:
            letra_usuario = input("Ingrese una letra: ").upper()
            if letra_usuario in string.ascii_uppercase:
                return letra_usuario
            else:
                #si la letra no se encuentra en el abecedario string.ascii_Uppercase,se levanta una excepcion
                raise ValueError("la entrada no es una letra valida")
        except ValueError as e:
            print(f"Se produjo el siguiente error: {e}")

def juego_ahorcados(palabra):
    print("=====================================")
    print("Bienvenido al juego del ahorcado")
    print("=====================================")

    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()
    
    intentos = 7
    
    while len(letras_por_adivinar) > 0 and intentos > 0:
        #informacion del estado actual del juego.
        # numero de intentos que quedan (vidas)
        print(f"te quedan {intentos} intentos y has usado estas letras:{''.join(letras_adivinadas)}")
        # se arman la palabra encriptada con guiones bajos que se le mostrara al usuario
        palabra_lista = [] # compresion : [letra if letra in letras_adivinadas else "_" for letra in palabra]
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_lista.append(letra)
            else:
                palabra_lista.append("_")    
        print(diagramas.vidas[intentos])
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        #intenta obtener una letra ingresada por el usuario
        try:
            letra = obtener_letra_usuario()
            if letra in abecedario - letras_adivinadas:
                letras_adivinadas.add(letra)
                # verificar si la letra ingresada esta en la palabra adivinar
                if letra in letras_por_adivinar:
                    letras_por_adivinar.remove(letra)
                    print("")
                else:
                    #si la letra no esta en la palabra, disminuye el numero de intentos
                    intentos -= 1
                    print(f"\nTu letra, {letra}, no esta en la palabra")
            elif letra in letras_adivinadas:
                # si la letra ya ha sido usada , muestra un mensaje de advertencia
                print(f"\nYa usaste esa letra, ingresa una letra nueva")
        except KeyboardInterrupt:
            # captura la excepcion cuando el usuario interrumpe el juego con ctrl+c
            print("juego interrumpido")
        except Exception as e:
            print(f"Error inesperado: {e}")    
    #comprueba si el jugador gano o perdio el juego y muestra un mensaje apropiado
    
    if intentos == 0:
        print(diagramas.vidas[intentos])
        print(f"\nAhorcado Pelotudo!, la palabra era: {palabra}")
    else:
        print(f"\nFelicidades! Adivinaste la palabra: {palabra}")

def main():
    palabra = obtener_palabra_aleatoria()
    if palabra:   
     juego_ahorcados(palabra)

#verifica si este scrip se ejecuta como programa principal y llama a la funcion main

if __name__ == "__main__":
    main()
