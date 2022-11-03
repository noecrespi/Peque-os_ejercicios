# Escribe un programa que pida un número y calcule su factorial.

from math import factorial


def calcFactorial():

    # numero introducido por el usuario
    num = int(input("Introduce un número: "))
    
    # 1 opción 
    # print("El factorial de " + str(num) + " es " + str(factorial(num))) 
    
    # 2 opción 
    # calcula el factorial del numero introducido
    if num >=  1:
        factorial = 1

        for i in range(1, num + 1):
            factorial = factorial * i
        print("El factorial de " + str(num) + "! es " + str(factorial))

    # controla si el numero introducido es negativo o 0
    else:
        print("Debe introducirse un número mayor que 0")

calcFactorial()
