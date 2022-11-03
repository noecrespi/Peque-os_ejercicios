# Escribe un programa que escriba a los siguientes números (la separación entre número es para facilitar cuántos números se deben escribir en cada bucle) y en el que la función range que utilices tenga un ÚNICO argumento y que el valor de este se corresponda con el número de elementos que aparecen en la lista.


def tabla():

    fila1 = ""
    fila2 = ""
    fila3 = ""
    fila4 = ""
    fila5 = ""

    for i in range(10):
        fila1 = fila1 + "|" + str((i)+1) + "\t" 
        # print(i)
    print(fila1)

    #2
    for i in range(10):
        fila2 = fila2 + "|" + str((i*2)+2) + "\t" 
        # print((i*2)+1)
    print(fila2)

    #3
    for i in range(10):
        fila3 = fila3 + "|" + str((i*2)+20) + "\t" 
        # print((i*2)+20)
    print(fila3)

    #4
    for i in range(6):
        fila4 = fila4 + "|" + str((i*4)+10) + "\t" 
        # print((i*4)+10)
    print(fila4)

    #5
    for i in reversed(range(9)):
        fila5 = fila5 + "|" + str(i*5) + "\t" 
        # print((i)*5)
    print(fila5)

tabla()