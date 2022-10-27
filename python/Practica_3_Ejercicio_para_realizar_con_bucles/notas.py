# Escribe un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas,  la nota media, la nota más alta que ha sacado así como también la menor nota que ha sacado

def notas():

    # 1r forma menos eficiente 
    # notas = []

    # print("Introduce la notas del alumno para sacar la media, la nota máxima y la nota mínima.")
    # nombre = input("Pon el nombre del alumno: ")

    # num1 = int(input("introduce la primera nota: "))
    # num2 = int(input("introduce la segunda nota: "))
    # num3 = int(input("introduce la tercera nota: "))
    # num4 = int(input("introduce la cuarta nota: "))
    # num5 = int(input("introduce la quinta nota: "))
    
    # notas.append(num1)
    # notas.append(num2)
    # notas.append(num3)
    # notas.append(num4)
    # notas.append(num5)

    # notas.sort()
    

    # contar = 0
    # suma = 0
    
    # for nota in notas:
    #     if nota >= 0 and nota <= 10:
    #         contar = contar +1
    #         suma = suma + nota
    #     else:
    #         print("La nota " + str(nota) +  " no es valida, debe estar comprendida entre 0 y 10 ")

    # print("El alumno " + nombre)
    # print("Su nota media es: " + str(suma / contar))
    # print("La nota nimima es: " + str(notas[0]))
    # print("La nota máxima es: " + str(notas[-1]))

    
    #2n forma

    notas = []

    print("Introduce la notas del alumno para sacar la media, la nota máxima y la nota mínima.")
    nombre = input("Pon el nombre del alumno: ")
    continuar = True

    #Comprueba que los numeros introducidos tengan las características necesarias para meterse en la lista de notas
    while continuar == True and len(notas) <= 4:
        num = int(input("Introduce la nota: "))
        if (num >= 0 and num <= 10) and len(notas) <= 4:
            notas.append(num)
            continuar = True

            print(notas)    
        else:
            continuar = False
    else:
        continuar = False


    # controla que si la lista está vacia o no está completa
    if len(notas) == 0:
        print("Lo siento pero la nota debe estar comprendida entre 0 y 10")
    elif len(notas) == 5:
        notas.sort()
        contar = len(notas)
        sumNums = sum(notas)

        print("El alumno " + nombre)
        print("Su nota media es: " + str(sumNums / contar))
        print("Su nota nimima es: " + str(notas[0]))
        print("su nota máxima es: " + str(notas[-1]))
    else:
        print("Lo siento pero la nota debe estar comprendida entre 0 y 10")
        print("La lista de notas son: " + str(notas))


notas()
