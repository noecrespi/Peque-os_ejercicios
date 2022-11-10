#  Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.


def agenda():

    telf = []
    telfStr = ""
    isName = True

    while (isName == True):
        name = input("Escribe un nombre: ")
        if (name == "S" or name == "s"):
            isName = False
        else:
            telfNum = int(input("Escribe el número de teléfono de " + name + ": "))
            while (len(str(telfNum)) != 9):
                print("El número de teléfono debe tener 9 dígitos")
                telfNum = int(input("Escribe el número de teléfono de " + name + ": "))
            else:
                telf.append([name, telfNum])


    # printerr 
    for persona in telf:
        telfStr = telfStr + str(persona[0]) + ": " + str(persona[1]) + "\n"

    print("Los nombres y teléfonos de la agenda son: \n" + telfStr)

agenda()
