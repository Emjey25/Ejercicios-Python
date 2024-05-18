

def Factorial(numero):
    if numero ==0:
        return 1
    else:
        return numero * Factorial(numero -1)

numero = 4
print("el factorial de", numero, "es",Factorial(numero))    