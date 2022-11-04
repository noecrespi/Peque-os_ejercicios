# Escribe un programa que pida un número y escriba si primo o no


def isPrimo():
    num  = int(input("Introduce un número: "))
    

    for n in range(2,num):
        if (num % n) == 0:
            print("El numero " + str(num) + " no es primo")
            return False
    
    print("El numero " + str(num) + " es primo")
    return True

isPrimo()