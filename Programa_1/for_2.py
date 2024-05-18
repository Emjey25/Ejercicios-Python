while True:
    frase = input("Ingrese una frase para contar las vocales: (Escriba SALIR para terminar)").lower()
    if frase =="salir":
        print("Hasta vista baby!!!")
        break
    a=0
    e=0
    i=0
    o=0
    u=0
    for caracter in frase:
        if caracter =='a':
            a+=1
        elif caracter =='e':
            e+=1
        elif caracter =='i':
            i+=1
        elif caracter =='o':
            o+=1
        elif caracter =='u':
            u+=1
    print("Conteo de vocales en la frase: ")
    print(f"el numero de la vocal a: {a}")
    print(f"el numero de la vocal e: {e}")
    print(f"el numero de la vocal i: {i}")
    print(f"el numero de la vocal o: {o}")
    print(f"el numero de la vocal u: {u}")