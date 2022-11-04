# Escribe un programa que pida un número e imprima todos sus divisores.


def isDivisor():

    print("Programa que dice todos los divisores del numero añadido")
    print("¿Qué numero quieres saber sus divisores?")
    
    num = int(input())
    divisores = ""

    if num >= 1:
        for i in range(1,num +1):
            if num % i == 0:
                divisores =  divisores + str(i) + " "
            else:
                None 
        print("Los divisores del número " + str(num) + " son: " + divisores )
    else:
        print("El número tiene que ser mayor a 0")
    

isDivisor()
