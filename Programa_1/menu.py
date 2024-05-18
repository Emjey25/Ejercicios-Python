while True:
    print("MENU")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion ")
    print("4. Potencia")
    print("5. Modulo")
    print("6. Division")
    print("7. Salir")
    opcion = int(input("Ingrese la opcion deseada: "))
    if 1<= opcion <= 6:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        
        if opcion == 1:
            resultado = num1 + num2
            operacion =  "suma"
        elif opcion == 2:
            resultado = num1 - num2
            operacion =  "Resta"
        elif opcion == 3:
            resultado = num1 * num2
            operacion =  "Multiplicacion"
        elif opcion == 4:
            resultado = num1 ** num2
            operacion =  "Potencia"
        elif opcion ==5:
            resultado = num1 % num2
            operacion =  "Modulo"
        elif opcion ==6:
            if num2 !=0:
                resultado = num1 / num2
                operacion =  "Division"
            else:
                resultado = "error"
                operacion =  "Division fallida"
        print(f"El resultado de la {operacion} es {resultado}")
    elif opcion ==7:
        print("Bye bye see later!!!")
        break
    else:
        print("La embarraste!!!")
