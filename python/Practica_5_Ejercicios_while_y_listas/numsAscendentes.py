# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números:


def numAscendentes():

    nums = []
    numsStr = ""
    numsPrint = True

    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce un número mayor que " + str(num1) + ": "))

    nums.append(num1)

    while(numsPrint == True):
        if (nums[-1] < num2):
            nums.append(num2)
            num2 = int(input("Introduce un número mayor que " + str(nums[-1])+": "))
        else:
            numsPrint = False

    for i in nums:
        numsStr = numsStr + str(i) + ", "

    print("Los números introducidos son: " + numsStr[:-2])


numAscendentes()
