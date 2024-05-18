continuar = 's'

while continuar.lower() == 's':

 numero = int(input("Ingrese el numero de la tabla de multiplicar: "))
 print(f"Tabla de multiplicar del numero {numero}")
 for i in range(1,11):
    resultado = numero * i
    print(f"{numero} X{i} = {resultado}")
continuar = input("deseas ver otra tabla? (s/n)")
print("gracias  por utilizar el programa!!!")    