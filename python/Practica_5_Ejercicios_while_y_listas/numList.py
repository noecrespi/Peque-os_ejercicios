# Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.

# Escribe un número: 6
# Escribe un número mayor que 6: 4

# 4 no es mayor que 6. Vuelve a probar: 50

# Escribe un número entre 6 y 50: 45
# Escribe otro número entre 6 y 50: 13
# Escribe otro número entre 6 y 50: 4

# Los números situados entre 6 y 50 que has escrito son: 45, 13 



def numList():

    nums = []
    numsStr = ""
    num1 = int(input("Escribe un número: "))
    num2 = int(input("Introduce un número mayor que " + str(num1) + ": "))

    numInList = True
    numsPrint = True
    nums.append(num1)

    # comprueba que el segundo número es mayor que que el priemero 
    while(numInList == True):
        if num1 < num2:
            nums.append(num2)
            numInList = False
        else:
            num2 = int(input("Introduce un número mayor que " + str(num1) + ": "))

    # comprueba que el numero estre entre el numero 1 y el numero 2
    while(numsPrint == True):
        num3 = int(input("Introduce un número entre " + str(num1) + " y "
            + str(num2) + ": "))
        if (num1 < num3 and num2 > num3):
            nums.append(num3)
        else:
            numsPrint = False

    # ordena los números
    set(nums)
    # elinina los números repetidos de la lista
    uniqueNum = list(set(nums))
    
    # convierte la lista de numeros en un string
    for i in uniqueNum:
        numsStr = numsStr + str(i) + ", "

    print("Los números entre " + str(num1) + " y " + str(num2) + " son: " + numsStr[:-2])

numList()