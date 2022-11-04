# Escribe un programa que pida la anchura y la altura de un rectángulo


def printRectanHueco():

    # Pide la anchura y la altura del rectángulo
    ancho = int(input("Introduce la anchura del rectángulo: "))
    altura = int(input("Introduce la altura del rectángulo: "))

    if altura >= 3 and ancho >= 3:
        # Dibuja el rectángulo
        for i in range(altura):
            # Dibuja la primera línea
            if i == 0:
                print("*" * ancho)
            # Dibuja la última línea
            elif i == altura - 1:
                print("*" * ancho)
            # Dibuja las líneas intermedias
            else:
                print("*" + ((ancho -2) * " ") + "*")
    else:
        print("Debe introducirse un número mayor que 3 para poder dibujar el rectángulo hueco")



printRectanHueco()
