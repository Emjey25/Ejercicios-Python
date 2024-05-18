import random

numeroSecreto = random.randint(1,10)
print("He pensado un numero entre el 1 y 10. intenta adivinarlo!!")

while True:
    numeroUsuario=int(input("Ingresa tu numero: "))
    if numeroUsuario < numeroSecreto:
        print("Demasiadoo bajo, intenta de nuevo!! ")
    elif numeroUsuario>numeroSecreto:
        print("Demasiadoooo alto, intenta de nuevo!!")
    else:
        print(f"Correcto!!!, el numero era {numeroSecreto}")
        break