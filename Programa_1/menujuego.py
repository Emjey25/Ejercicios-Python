import random
from colorama  import Fore,Back,Style

def adivina_el_numero():
    print("\nJuego 1: Adivina el número")
    numero_secreto = random.randint(1, 50)
    intentos = 0
    
    while intentos < 3:
        try:
            intento = int(input("Adivina el número entre 1 y 50: "))
            intentos += 1
            
            if intento == numero_secreto:
                print(f"¡Felicidades! ¡Has adivinado en {intentos} intentos!")
                return
            elif intento < numero_secreto:
                print("El número secreto es mayor. ¡Vamos, puedes hacerlo!")
            else:
                print("El número secreto es menor. ¡Sigue intentándolo!")
        
        except ValueError:
            print("Por favor, introduce solo números.")
    
    print(f"¡Agotaste tus intentos! El número secreto era {numero_secreto}")

continuar = True

while continuar:
    print("\nMenú principal")
    print("1. Jugar Adivina el número")
    print("2. Jugar Piedra, papel o tijera")
    print("3. Créditos")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        adivina_el_numero()
    elif opcion == "2":
        print("¡Este juego aún no está implementado!")
    elif opcion == "3":
        print("Créditos...")
    elif opcion == "4":
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
