# Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir números, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.


def pedirNum():

    lista = []
    num = input("Introduce un número: ")
    isNum = True
    
    # me no me deja poner varios argumentos
    # while(num != "salir" or num != "Salir" or num != "SALIR"):
    while(num != "Salir"):
            lista.append(int(num))
            num = input("Introduce un número: ")

    
    print("Los números dados por el usuario son " + str(lista))




pedirNum()
