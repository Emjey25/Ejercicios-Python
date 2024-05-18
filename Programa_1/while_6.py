import random

numeroSecreto = random.randint(1,10)
print("He pensado un numero entre el 1 y 10. intenta adivinarlo!!")
intentos =0

while intentos <3:
    numeroUsuario=int(input("Ingresa tu numero: "))
    if numeroUsuario < numeroSecreto:
        print("Demasiadoo bajo, intenta de nuevo!! ")
    elif numeroUsuario>numeroSecreto:
        print("Demasiadoooo alto, intenta de nuevo!!")
    else:
        print(f"Correcto!!!, el numero era {numeroSecreto}")
        break
    intentos +=1
if intentos == 3:
    print(f"Lo siento, has usado todos tus intentos. El numero era {numeroSecreto}")