while True:
    print("Menu de opciones ")
    print("1. Calcular la suma de los primeros N numeros naturales ")
    print("2. mostrar los primeros N numeros naturales ")
    print("3. salir")
    opcion = int(input("Ingresa el numero de la opcion que deseas: "))
    if opcion ==1:
        numero = int(input("Ingrese un numero: "))
        suma = sum(range(1, numero+1))
        print(f"La suma de los primeros {numero} numeros naturales es: {suma}")
    elif opcion ==2:
        numero=int(input("Ingrese un numero: "))
        print("Los primeros N numero naturales son: ")
        for i in range(1, numero+1):
            print(i, end=' ')
        print()
    elif opcion == 3:
        print("Que te vya bien!!!")
        break
    else:
        print("Opcion no valida!!! por favor intenta de nuevo")