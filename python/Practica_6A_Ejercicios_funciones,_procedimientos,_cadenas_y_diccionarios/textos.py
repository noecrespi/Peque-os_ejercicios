# Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

texto = str(input("Introduce un texto: "))

def textos(texto = "Hello world"):

    # texto en minusculas 
    print("Texto en minusculas:")
    print(texto.lower())

    # texto en mayusculas 
    print("Texto en mayusculas:")
    print(texto.upper())

textos(texto)
