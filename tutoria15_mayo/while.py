

def sumar(a,b):
    return a + b


def Calcular():
 num1 = int(input("primer numero: "))
 num2 = int(input("segundo numero: "))
 print("la suma es" ,sumar(num1,num2))
 
while(True):
    opcion = int(input("1. Continuar\n2. finalizar"))
    if(opcion == 1):
        Calcular()
    else:
        break    



