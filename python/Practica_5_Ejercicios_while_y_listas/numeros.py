# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal.

def numeros():
    
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce un número mayor que " + str(num1) + ": "))
    
    while(num2 <= num1):
        num2 = int(input(str(num1) + " no es mayor que " + str(num2) + ". Introduce un número mayor que " + str(num1) + ": "))
    
    print("Los números dados por el usuario son " + str(num1) + " y " + str(num2))

numeros()