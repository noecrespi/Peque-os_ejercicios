# Escribe un programa que pida la altura de un triángulo y lo dibuje


def printTrianguloCentral():

    # altura del triangulo introducida por el usuario
    altura = int(input("Introduce la altura del triángulo: "))

    if altura >= 1:
        # dibuja el triangulo
        for i in range(altura):
            # espacios vacios -> altura - posición i - 1
            # * -> siempre tiene que ser impares para que puedan estar centradas por eso se multiplica por 2 la posición de i y se suma 1
            print(" " * (altura - i - 1) + "*" * (2 * i + 1))
    else:
        print("Debe introducirse un número mayor que 0")

printTrianguloCentral()