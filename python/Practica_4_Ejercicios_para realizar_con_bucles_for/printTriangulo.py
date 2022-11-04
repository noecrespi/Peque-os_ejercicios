# Escribe un programa que pida la altura de un triángulo y lo dibuje


def printTriangulo():

    # altura del triangulo introducido por el usuario
    altura = int(input("Introduce la altura del triángulo: "))

    if altura >= 1:
        # dibuja el triangulo
        for i in range(altura):
            print("*" * (i + 1))
    else:
        print("Debe introducirse un número mayor que 0")


printTriangulo()
