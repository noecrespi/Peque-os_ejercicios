# Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor de los tres números primos.

def isDivisor():

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    num4 = int(input("Introduce el cuarto número: "))

    if(num1 % num4 == 0 and num2 % num4 == 0 and num3 % num4 == 0):
        print("El numero  " + str(num4) + " es divisor de los tres numeros")
    else:
        print("El numero " + str(num4) + " no es dvisor de los tres numeros")


isDivisor()
