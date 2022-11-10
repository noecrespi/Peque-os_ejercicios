# Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

def notasAlum():

    alum = []
    alumStr = ""
    
    isName = True


    while (isName == True):
        name = input("Escribe un nombre: ")
        if (name == ""):
            isName = False
        else:
            isNota = True
            notas = []
            notas.append(name)
            while (isNota == True):
                nota = int(input("Escribe una nota de " + name + ": "))
                if (nota < 0 or nota > 10):
                    isNota = False
                else:
                    notas.append(nota)
            alum.append(notas)
    print(alum)

    for i in alum:
        alumNotas = ""
        for j in i:
            alumNotas = alumNotas + str(j) + ", "
        # alumNotas = alumNotas.replace(i[0] + ", ", ": ")
        alumStr = alumStr + str(i[0]) + alumNotas[:-2].replace(i[0] + ", ", ": ") + "\n"



    # opción 2
    # while (isName == True):
    #     name = input("Escribe un nombre: ")
    #     if (name == ""):
    #         isName = False
    #     else:
    #         isNota = True
    #         notas = "" 
    #         while (isNota == True):
    #             nota = int(input("Escribe una nota de " + name + ": "))
    #             if (nota < 0 or nota > 10):
    #                 isNota = False
    #             else:
    #                 notas = notas + str(nota) + ", "
    #         alum.append([name, notas[:-2]])

    # printear 
    # for persona in alum:
    #     alumStr = alumStr + str(persona[0]) + ": " + str(persona[1]) + "\n"



    # opción 3
    # while (isName == True):
    #     name = input("Escribe un nombre: ")
    #     if (name == ""):
    #         isName = False
    #     else:
    #         isNota = True
    #         notas = []
    #         while (isNota == True):
    #             nota = int(input("Escribe una nota de " + name + ": "))
    #             if (nota < 0 or nota > 10):
    #                 isNota = False
    #             else:
    #                 notas.append(nota)
    #         alum.append([name, notas])

    # # printear 
    # for persona in alum:
    #     alumStr = alumStr + str(persona[0]) + ": " + str(persona[1]) + "\n"

    print("Los nombres y notas de los alumnos son: \n" + alumStr)

notasAlum()