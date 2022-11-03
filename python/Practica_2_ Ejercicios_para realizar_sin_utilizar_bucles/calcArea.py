# Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.

# 1. Pide al usuaria qe area quiere calcular si la del cuadrado o la del triangulo
# 2. si el usuario elige que quiere calcular un cuadrado 
#   2.1 pedir al usuario el lado 
#   2.2 calcular el area del cuadrado (lado x lado)
#   2.3 monstrar el area del cuadrado
# 3. si el usuario elige que quiere calcular un triangulo 
#   3.1 pedir al usuario la base
#   3.2 pedir al usuario la altura
#   3.3 calcular el area del triangulo ((b * h) / 2 )
#   3.4 monstrar el area del triangulo
# 4. si el usuario a escrito algo diferente a cuadrado o a trinagulo 
#   4.1 decir que el programa solo calcula el area del cuadrado o de un triangulo  


def calcArea():
    areaCal = input("¿Que area quieres calcular la de un trinagulo o un cuadrado? ")

    #Calcula el area de un cuadrado
    if( areaCal == "cuadrado" or  areaCal == "Cuadrado" or  areaCal == "CUADRADO"):
        lado = int(input("Dame un lado del cuadrado en cm "))
        areaCuadrado = pow(lado, 2)

        print("El area del cuadrado es de " + str(areaCuadrado) + " centímetros cuadrados")

    # Calcula el area de un triangulo
    elif(areaCal == "triangulo" or areaCal == "Triangulo" or areaCal == "TRIANGULO"):
        b = int(input("Dame la base del triangulos en cm "))
        h = int(input("Dame la altuta del triangulos en cm "))
        areaTriangulo = (b * h) / 2 

        print("El area del triangulo es de " + str(areaTriangulo) + " centímetros cuadrados")
    
    # avisa que solo se puede calcular el area de un cuadrado o de un triangulo
    else:
        print("Actualmete el programa solo calcula el area de un cuadrado y el area de un triangulo")


calcArea()
