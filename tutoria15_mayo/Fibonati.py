 
# ejercicio secuencia fibonacci

N =int(input("ingrese la cantidad de numeros de la serie que desea ver: "))

a,b = 0,1

for _ in range(N):
    print(a , end=' ')
    a,b = b, a+b