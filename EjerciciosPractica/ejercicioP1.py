"""Escribe un programa en Python que solicite al usuario una lista de números y luego realice las siguientes tareas:

Encuentre el número máximo y mínimo en la lista.
Calcule la suma y el promedio de los números.
Identifique y cuente cuántos números son pares e impares.
Genere una nueva lista que contenga solo los números primos de la lista original.
Requisitos:
Utiliza un bucle while para pedir los números al usuario hasta que decida detenerse.
Utiliza bucles for para iterar sobre la lista y realizar los cálculos necesarios.
Utiliza condicionales if para verificar condiciones específicas (pares, impares, primos)."""

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Función principal que realiza todas las tareas solicitadas
def numeros():
    numerolist = []  # Lista para almacenar los números introducidos por el usuario
    while True:
        entrada = input("Introduce un número (o 'stop' para terminar): ")
        if entrada.lower() == 'stop':  # Condición para detener la entrada de números
            break
        try:
            numerolist.append(int(entrada))  # Añadir el número a la lista
        except ValueError:
            print("Por favor, introduce un número válido.")  # Mensaje de error si la entrada no es un número válido

    if not numerolist:  # Verificar si la lista está vacía
        print("No se introdujeron números.")
        return

    # Encontrar el valor mínimo y máximo en la lista
    min_val = min(numerolist)
    max_val = max(numerolist)
    
    # Calcular la suma y el promedio de los números en la lista
    suma = sum(numerolist)
    promedio = suma / len(numerolist)
    
    # Identificar y contar los números pares e impares
    pares = [x for x in numerolist if x % 2 == 0]
    impares = [x for x in numerolist if x % 2 != 0]
    
    # Generar una nueva lista que contenga solo los números primos
    primos = [x for x in numerolist if es_primo(x)]

    # Imprimir los resultados
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Primos: {primos}")

# Llamada a la función principal
numeros()