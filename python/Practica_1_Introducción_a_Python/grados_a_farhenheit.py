# Conversión de grados centígrados a grados Fahrenheit


def gradosAFar():
    print("Convierte grados centígrados a grados Farhenheit")

    c = int(print("Introduce los grados centigrados: "))
    far = (c * 9/5) + 32

    return print(str(c)+ " grados centírados son: " + str(far) + " grados Farhenheit ")

gradosAFar()
