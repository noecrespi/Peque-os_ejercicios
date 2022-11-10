# Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
# El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56


def sumTotal():

    nums = []
    numsStr = ""
    numlimit = int(input("Escribe el número máximo: "))
    num1 = int(input("Escribe un número: "))
    
    nums.append(num1)
    
    total = num1
    isnumLimitGig = True
    
    while (isnumLimitGig == True):
        if (total < numlimit):
            num2 = int(input("Escribe otro número: "))
            nums.append(num2)
            total = total + num2
        else:
            isnumLimitGig = False

    for i in nums:
        numsStr = numsStr + str(i) + ", "

    print("El límite a superar es " + str(numlimit) + ". Los números que has escrito son: " + numsStr[:-2] + " y la suma de estos números es: " + str(total))


sumTotal()