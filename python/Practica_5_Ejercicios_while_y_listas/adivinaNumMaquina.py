#  Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños. pista:


import random


def adivinaNumMaquina():

    numMinimo = int(input("Introduce el número mínimo: "))
    numMaximo = int(input("Introduce el número máximo: "))
    contador = 1

    if numMinimo > numMaximo:
        numMaximo = int(input("Introduce un número mayor a " + str(numMinimo) + str(": ")))
        contador += 1
    
    numSecreto = random.randint(numMinimo, numMaximo)

    inNum = True
    
    num = int(input("Introduce un número entrte " + str(numMinimo) + " y " + str(numMaximo) + str(": ")))   
    while inNum == True:

        if num < numMinimo or num > numMaximo:
            num = int(input("Introduce un número entrte " + str(numMinimo) + " y " + str(numMaximo) + str(": ")))
            contador += 1
        elif numSecreto != num:
            if num < numSecreto:
                num = int(input("El número " + str(num) + " es demasiado pequeño \n vuelve a probar: "))
                contador += 1
            else:
                num = int(input("El número " + str(num) + " es demasiado grande \n vuelve a probar: "))
                contador += 1

        else:
            print("Correcto! Lo has logrado en el " + str(contador) + " intento.")
            inNum = False


adivinaNumMaquina()
