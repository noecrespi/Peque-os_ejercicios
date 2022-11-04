# Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.

from re import I


def sumaEntreNum():

    # numeros introcinidos por el usuario
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    # cambia el orden de los números, en el caso que el nummero 1 sea mayor que el numero 2
    if num1 > num2:
        num1, num2 = num2, num1

    # suma los números entre el primer y el segundo número
    suma = 0
    for i in range(num1, num2 + 1):
        suma  = suma + i

    print("La suma de los números entre " + str(num1) + " y " + str(num2) + " es " + str(suma))

sumaEntreNum()
