# Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.


def adivinaNum():

    numMin = int(input("Introduce el número mínimo: "))
    numMax = int(input("Introduce el número máximo: "))

    
    isNumMax = True

    while isNumMax == True:
        if numMax < numMin or numMax == numMin:
            numMax = int(input("Introduce un número mayor a " + str(numMin) + str(": ")))
        else:
            isNumMax = False

    print("Piensa un número entre " + str(numMin) + " y " + str(numMax) + str(". "))
    
    num = int((numMax + numMin) / 2)    
    isNum = input("El número es " + str(num) + " ? (mayor, menor o igual): ") 
    numMax = numMax + 1
    isMayor = True
    isNumMax = True

    

    while isMayor == True:
        if num == numMin or num == (numMax-1):
            print("Tramposo!!! Ya no puedo adivinar más. Por que no hay números")
            isMayor = False
        else:
            if isNum == "mayor" or isNum == "MAYOR" or isNum == "Mayor":
                numMin = num
                num = int((numMax + numMin) / 2)
                isNum = input("El número es " + str(num) + " ? (mayor, menor o igual): ")
            elif isNum == "menor" or isNum == "MENOR" or isNum == "Menor":
                numMax = num
                num = int((numMax + numMin) / 2)
                isNum = input("El número es " + str(num) + " ? (mayor, menor o igual): ")
            elif isNum == "igual" or isNum == "IGUAL" or isNum == "Igual":
                print("Gracias por jugar!!")
                isMayor = False
            else:
                print("No has introducido una opción válida, las opciones son: mayor, menor o igual")
                isNum = input("El número es " + str(num) + " ? (mayor, menor o igual): ")
    
adivinaNum()