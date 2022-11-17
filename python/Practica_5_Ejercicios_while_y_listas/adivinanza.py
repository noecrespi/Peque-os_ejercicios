# Desarrolla un programa que tenga las siguientes características:
    # Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
    # Dicho problema resuélvelo con bucles for y while. 
    # Justifica en el propio programa porque una opción es adecuada y la otra no.
    # ¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente una solución es más eficiente? Investiga para comprobarlo.

# programa para adivinar una adivinanza

def adivinanza():

    print("A ver si te atreves a adivinar las tres adivinanzas")
    
    print("¿Qué es lo que tiene cuatro patas en la mañana, dos en la tarde y tres en la noche? ")
    adivinanza1 = input()
    contador = 1
    intentos = []

    user = True

    while user == True:
        if adivinanza1 != "un hombre" or adivinanza1 != "hombre" :
            adivinanza1 = input("No has acertado, vuelve a intentarlo: ")
            contador += 1
        else:
            print("\nHas acertado!!! \nSigamos con la siguiente adivinanza")
            user = False
            intentos.append(contador)
    
    print("Soy pequeña y de cristal, méteme al hoyo y no perderás.")
    adivinanza2 = input()
    contador = 1

    while user == False:
        if adivinanza2 != "canica" :
            adivinanza2 = input("No has acertado, vuelve a intentarlo: ")
            contador += 1
        else:
            print("Has acertado")
            user = True
            intentos.append(contador)

    print("Zapatos de goma, ojos de cristal, con una manguera me alimentas y dentro de la cochera me guardas.")
    adivinanza3 = input()
    contador = 1
    
    while user == True:
        if adivinanza3 != "coche" :
            adivinanza3 = input("No has acertado, vuelve a intentarlo: ")
            contador += 1
        else:
            print("Has acertado")
            user = False
            intentos.append(contador)
    contador = 1

    for i in intentos:
        i += 1
        print("Has necesitado " + str(i) + " intentos para acertar en la " + str(contador) + "acertijo")
        contador += 1


adivinanza()