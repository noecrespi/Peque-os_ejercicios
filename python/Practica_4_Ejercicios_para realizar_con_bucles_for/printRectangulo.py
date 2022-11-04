# Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera.

def printRectangulo():

    # altura y ancho del rectangulo introducidos por el usuario
    altura = int(input("Introduce la altura del rectángulo: "))
    ancho = int(input("Introduce el ancho del rectángulo: "))

    if altura >= 1 and ancho >= 1:
        # dibuja el rectangulo
        for i in range(altura):
            print("*" * ancho)
    else:
        print("Debe introducirse un número mayor que 0")

printRectangulo()
