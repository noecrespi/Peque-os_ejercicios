# Escribe un programa que pida la anchura de un triángulo y dibuje un rombo


def printRombo():

    # Pedimos la anchura del rombo
    anchura = int(input("Introduce la anchura del rombo: "))

    # pintamos el rombo
    if anchura >= 1:
        # dibuja la parte superior del rombo
        for i in range(anchura):
            print("*" * (i + 1))
        # dibuja la parte inferior del rombo
        for i in range(anchura):
            # el número de asteriscos es la anchura menos el número de iteración
            print("*" * (anchura - (i+1)))
    else:
        print("Debe introducirse un número mayor que 0")


printRombo()