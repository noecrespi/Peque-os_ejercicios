# Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 45
# 45 es demasiado grande. Escribe otro valor: 1
# Escribe otro valor: 39
# El límite a alcanzar es 50. La lista creada es: 10, 1, 39


def sumNums():
    nums = []
    numsStr = ""
    numlimit = int(input("Escribe el número límite: "))
    num1 = int(input("Escribe un número: "))
    total = 0
    isnumLimitGig = True

    # controla que el numero introducido no sea mayor que el numero límite
    while (isnumLimitGig == True):
        if num1 > numlimit:
            print( str(num1) + " es demasiado grande ya que hace un total de " + str(num1) + " y el límite es " + str(numlimit) + ".")
            num1 = int(input(" Vuelve a probar: "))
        else:
            nums.append(num1)
            total = total + num1
            isnumLimitGig = False

    # Modo largo
    #  controla que la suma de los numeros introducidos no sea mayor que el numero límite
    while (isnumLimitGig == False):
        if (total < numlimit):
            num2 = int(input("Escribe otro número: "))
            if (total + num2 > numlimit):
                print( str(num2) + " es demasiado grande ya que hace un total de " + str(total + num2))
            else:
                nums.append(num2)
                total = total + num2
        else:
            isnumLimitGig = True

        
    for i in nums:
        numsStr = numsStr + str(i) + ", "

    print("El límite a alcanzar es " + str(numlimit) + ". La lista creada es: " + numsStr[:-2] + " y la suma de estos números es: " + str(total))

sumNums()