# Comprobar si el número es par

def isPar():
    input("Comprueba si el número es par")

    num = int(input("Introduce un número: "))
    remainder = num % 2


    if remainder == 0:
        return print("El número " + str(num) + " es par")
    else:
        #return print("El número " + str(num) + " no es par")
        return print("El número " + str(num) + " es impar")


isPar()
