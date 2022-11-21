#  hacer una función de una ecuacion de segundo grado

import math


def equacion2():

    print("Ecuación de segundo grado")

    # variables
    a = float(input("¿Cuál es el valor de la letra 'a'? "))
    b = float(input("¿Cuál es el valor de la letra 'b'? "))
    c = float(input("¿Cuál es el valor de la letra 'c'? "))


    # dividendo 
    dividendo1 = - ( b )
    dividendoRaiz = math.sqrt(((b)*(b)) + (-4 * (a) * (c)))

    # Denominador
    denominador = 2 *a

    # x = (num ± num) / denominador 
    # x = num / denominador
    xParte1 = dividendo1 / denominador 
    # x = num / denominador
    xParte2 = dividendoRaiz / denominador 
    
    # resultados de x 
    x1 = xParte1 + xParte2
    x2 = xParte1 - xParte2

    print("     -(" + str(b) + ") ± √ ( (" + str(b) + ")² (-4 (" + str(a) + ") ("+ str(c)+ ")) )" + "\nx = -------------------------------------------\n                    2(" + str(a) + ")")
    # respuestas de la ecuación de segundo grado
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


equacion2()
