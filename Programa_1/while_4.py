passCorrecto = "123456"
intentos = 0

while intentos <3:
    passUsuario = input("Ingrese la contraseña: ")
    if  passUsuario == passCorrecto:
        print("Contraseña correcta!! ACCESO CONCEDIDO!!")
        break
    else:
        print(" Contraseña incorrecta!!! ")
        intentos += 1      # intentos = intentos +1
        print(f"Llevas {intentos} intentos ")
if intentos ==3:
    print("Has excedido el numero maximo de intentos. ACCESO DENEGADO!!!")