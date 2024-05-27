try:
    
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    resultado = numerador/denominador
    print(f"El resultado es: {resultado}")
except ValueError:
    #este bloque maneja excepciones de valores / se ingresa una letra cuando se espera un numero
    print("ERROR PELOTUDO: debes ingresar un numero entero valido")
except ZeroDivisionError:
    print("No se puede dividir por cero")   
except:
    print("Error desconocido")    
