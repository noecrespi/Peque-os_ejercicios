# calcular y mostrar el area de un triangulo


def areaTriangulo():
    input("Calcula el area de un triangulo")

    b = int(input("Introduce la base del trinagolo: "))
    h = int(input("introduce la altura del trinagulo: "))
    a = (b * h) / 2
    
    return print("El area del triangulo es: " + str(a))


areaTriangulo() 
