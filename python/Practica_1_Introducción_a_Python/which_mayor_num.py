# Di cual de los los dos números es mayor 

def whichMayorNum():

    # Codigo respecto al diagrama de flujo
    # input("Programa que dice cual es el numero más alto de los dos intrducidos por el usuario")
    
    # # variable A
    # num1 = int(input("Introduce el primer número: "))
    # # variable B
    # num2 = int(input("Introduce el segundo número: "))

    # if num1 > num2:
    #     return print("El número " + str(num1) + "es mayor que el número " + str(num2))
    # else:
    #     return print("El número " + str(num2) + "es mayor que el número " + str(num1))



    # Codigo más eficiente y facil de mantener
    input("Programa que dice cual es el numero más alto de los dos intrducidos por el usuario\n Cuando escribas '0' te mostrará el resultado")
    
    nums = []
    isVerResultado = False

    while isVerResultado == False:
        
        num = int(input("Introduce un número: "))

        if num == 0:
            nums.sort()
            n = nums[-1]
            isVerResultado = True

            return print("El número más alto es: " + str(n))
        else:
            nums.append(num)

whichMayorNum()
