lista = [1,2,3,4,5]

#indexError: Se produce cuando se intenta acceder a ,
# un indice que no existe en la lista

try:
    lista[10]
except IndexError:
    print("Error de indice")

