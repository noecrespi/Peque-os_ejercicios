# Pida al usuario 5 números y diga cuál es el mayor y cuál el menor sin usar bucles.

# 1. Crear una lista  donde meteremos todos los numeros que meta el usuario
# 2. Pedir al usuario que introduzca 5 números
# 3. Guardar los numeros en la lista 
# 4. Ordenar la lista de menor a mayor
# 5. Mostrar el numero más pequeño y el más grande

def whichIsMayorNum():
    nums = []

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))
    num4 = int(input("Introduce el cuarto número: "))
    num5 = int(input("Introduce el quinto número: "))

    nums.append(num1)
    nums.append(num2)
    nums.append(num3)
    nums.append(num4)
    nums.append(num5)

    nums.sort()

    print("El numero más pequeño que has puesto es " + str(nums[0]))
    print("El numero más grande que has puest es " + str(nums[-1]))


whichIsMayorNum()
