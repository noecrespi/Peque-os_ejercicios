# Escribe un programa que lea (entrada por teclado) una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea

frase = str(input("Introduce una frase: "))

def textos(frase):
    for i in frase:
        print(i)

textos(frase)