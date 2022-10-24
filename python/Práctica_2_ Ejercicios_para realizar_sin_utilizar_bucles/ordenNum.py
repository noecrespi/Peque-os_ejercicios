# Pida al usuario 5 números y diga si estos estaban en orden decreciente, 	creciente o desordenados. Sin usar bucles

# 1. Crear una lista  donde meteremos todos los numeros que meta el usuario
# 2. Pedir al usuario que introduzca 5 números
# 3. Guardar los numeros en la lista 
# 4. Crear una lista nueva que ordene (menor a mayor) los numeros de la lista dada del usuario
# 5. Crear una lista nueva que ordene (mayor a menor) los numeros de la lista dada del usuario
# 6. Si la lista ordenada  es igual a la lista que el usuario nos ha dado 
#   6.1 imprimir en pantalla "Los numeros están en orden creciente"
# 7. Si la lista del reves es igual a la lista que el usuario nos ha dado 
#   7.1 imprimir en pantalla "Los numeros están en orden descendiente"
# 8. Si la lista del usuario 
#   8.1 imprimir en pantalla "Los numeros están en orden descendiente"

def ordenNum():
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

    # ordena los números de menor a mayor
    ordenNums = sorted(nums)
    # ordena los números de mayor a menor 
    ordenRevesNums = sorted(nums, reverse=True)

    if(ordenNums == nums):
        print("Los numeros están en orden creciente")
    elif(ordenRevesNums == nums):
        print("Los numeros estan de forma descendiente")
    else:
        print("Los numeros estan desordenados")


ordenNum()
