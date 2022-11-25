# Escribe un programa que te pida una frase y una vocal (entrada por teclado), y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá:

def fraseVocales():

    frase = input("Dime algo: ")
    vocal = str(input("Dime una vocal: "))

    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


    for i in vocales:
        frase = frase.replace(i, vocal)
    
    print(frase)


fraseVocales()


