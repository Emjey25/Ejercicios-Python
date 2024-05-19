# Description: Ejemplo de como multiplicar los elementos de una lista

def multiplicarlist(items):
    total = 1
    for x in items:
        total *= x
    return total

print(multiplicarlist([1,2]))
