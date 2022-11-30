# Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes. Comentario: no es necesario validar si la es correcta, damos por hecho que lo será. 


dia = input("Introduce una fecha en formato dd/mm/aaaa: ")

def fecha(dia):

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto", 
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre", 
        12: "Diciembre",
    }

    dia = dia.split("/")
    numDia = []

    # comprueba que los parametros son números 
    for i in dia:
        if isinstance( int(i), int) == True:
            numDia.append(int(i))
        else:
            print( i + " no es correcto con el formato dia/mes/año, debe introducir numeros")

    # comprobamos que el dia este entre 1 y 31
    # comprobamos que el mes esté entre 1 y 12
    # Comprovamos que el año tiene 4 digitos 
    if (numDia[0] >= 1 and numDia[0] <= 31) and (numDia[1] >= 1 and numDia[1] <= 12) and (len(dia[2]) == 4):
        print( str(numDia[0]) + " de " + str(meses.get(numDia[1])+ " de " + str(numDia[2])) )
    else:
        print("El dia tiene que ser enrte 1 y 31. \nEl mes tiene que ser entre  1 y 12.\nEl año tiene que tener 4 digitos")


fecha(dia)