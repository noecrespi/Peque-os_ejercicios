from ast import Num

# Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares



def isPar():

    print("Escribe dos números y comprueba si son pares o impares")

    # numeros introcinidos por el usuario
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    # 1 opción, es más optimo 
    
    # cambia el orden de los números, en el caso que el nummero 1 sea mayor que el numero 2
    if num1 > num2:
        num1, num2 = num2, num1

    # comprueba entre los numeros  si el número es par o impar
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print("El número " + str(i) + " es par")
        else:
            print("El número " + str(i) + " es impar")

    # 2 opción, es menos recomendable
    # if num1 < num2:
    #     for i in range(num1, num2 + 1):
    #         if i % 2 == 0:
    #             print("El número " + str(i) + " es par")
    #         else:
    #             print("El número " + str(i) + " es impar")
    # else:
    #     for i in range(num2, num1 + 1):
    #         if i % 2 == 0:
    #             print("El número " + str(i) + " es par")
    #         else:
    #             print("El número " + str(i) + " es impar")


isPar()
