# Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.


def palabras():

    palabras = []
    palabra = input("Escribe una palabra: ")

    while(palabra != ""):
        palabras.append(palabra)
        palabra = input("Escribe una palabra: ")
    
    print("Las palabras que el usuario ha metido son: " + str(palabras))

palabras()
