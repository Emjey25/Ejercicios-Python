cadena = input("Ingresa una cadena de caracteres: ")
contadoDigitos = 0

for caracter in cadena:
    if caracter.isdigit():
        contadoDigitos+=1
print(f"La cadena contiene {contadoDigitos} digitos")

#.............................................................

while True:
    password = input("Crea una contraseña (debe tener al menos 6 caracteres y un numero): ")
    digitos = sum(caracter.isdigit() for caracter in password)
    if len(password)>=6 and digitos ==2:
        print("contraseña valida")
        break
    else: 
        print("contraseña invalida, intentalo de nuevo")
