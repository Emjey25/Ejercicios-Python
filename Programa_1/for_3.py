numero = int(input("Ingrese un numero Natural para sumar desde el 1 hasta el ingresado: "))
suma =0
for i in range(1, numero+1):
    suma +=i
print(f"La suma de los primero {numero} numeros naturales es: {suma}")