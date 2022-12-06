# Actividades avanzadas en JavaScript

**Escribir el código de una función a la que se pasa como parámetro un número entero y devuelve como resultado una cadena de texto que indica si el número es par o impar. Mostrar por pantalla el resultado devuelto por la función.**

El archivo que contiene esta función se llama ``` parImpar ``` .



**Definir una función que muestre información sobre una cadena de texto que se le pasa como argumento.A partir de la cadena que se le pasa, la función determina si esa cadena está formada sólo por mayúsculas, sólo por minúsculas o por una mezcla de ambas.**

El archivo que contiene esta función se llama ``` infoCadena ``` .



**Definir una función que determine si la cadena de texto que se le pasa como parámetro es un palíndromo, es decir, si se lee de la misma forma desde la izquierda y desde la derecha.**

    Ejemplo de palíndromo complejo: "La ruta nos aportó otro paso natural".

El archivo que contiene esta función se llama ``` isPalindromo ``` .

**Con la función [`getMonth()`](https://www.w3schools.com/jsref/jsref_getmonth.asp) realiza un script para escriba el nombre del mes en el que estamos. La variable a usar seria:**
    
    var letras = ['Enero', 'Febrero', ...];

El archivo que contiene esta función se llama ``` mes ``` .


**Realiza un programa que en función de la nota que introduzcamos, nos muestre por pantalla la nota equivalente en letras del estilo Notable, Insuficiente, ... A su vez, este programa debe almacenar hasta 5 notas y luego mostrar la media tanto con numero como con letras.**

El archivo que contiene esta función se llama ``` notas.html ``` .


**El signo zodiacal de una persona está determinado por su día de nacimiento. Realiza un programa que determine tu sigo del zodiaco en función de tu fecha de nacimiento. Deberás usar un diccionario, array o lista que asocia a cada signo el período del año que le corresponde.**

El archivo que contiene esta función se llama ``` signosZodiaco.html ``` .



**Escribe un programa que muestre una tabla de multiplicar como la siguiente:**

    1   2   3   4   5   6   7   8   9   10
    2   4   6   8   10  12  14  16  18  20
    3	6	9	12	15	18	21	24	27	30	
    4	8	12	16	20	24	28	32	36	40	
    5	10	15	20	25	30	35	40	45	50	
    6	12	18	24	30	36	42	48	54	60	
    7	14	21	28	35	42	49	56	63	70	
    8	16	24	32	40	48	56	64	72	80	
    9	18	27	36	45	54	63	72	81	90	
    10	20	30	40	50	60	70	80	90	100	

El archivo que contiene esta función se llama ``` tabla ``` .



**Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.**

**Desarrolla un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos**

**El programa deja de pedir tiempos de viaje cuando se ingresa un 0.**

    Duración tramo: 15
    Duración tramo: 30
    Duración tramo: 87  
    Duración tramo: 0
    Tiempo total de viaje: 2:12horas

El archivo que contiene esta función se llama ``` tiempoViaje ``` .



**Escribe un programa que «piense» un número entre 0 y 100, y entregue pistas al usuario para que lo adivine. El usuario debe ingresar su intento, y el programa debe decir si el número pensado es mayor, menor, o el correcto:**

    Adivine el numero.
    Intento 1: 32
    Es mayor que 32
    Intento 2: 80
    Es menor que 80
    Intento 3: 70
    Es mayor que 70
    Intento 4: 72
    Correcto. Adivinaste en 4 intentos.

El archivo que contiene esta función se llama ``` adivinaNum ``` .

**Una vez que completes este ejercicio, es hora de invertir los roles: ahora tú pensarás un número y el computador lo adivinará.**

El archivo que contiene esta función se llama ``` WhatNumberIs ``` .


**Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen respectivamente 1.20€, 2.70€ y 4.80€. La máquina acepta y da cambio con monedas de 10cent, 50cent y 1€. Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio del producto, el programa debe entregar las monedas de vuelto, una por una.**

    Elija producto: B
    Ingrese monedas:
    1
    50
    50
    1
    Su vuelta:
    10
    10

El archivo que contiene esta función se llama ``` maquinaAlimentos ``` .


**El supermercado Pryca ha lanzado una promoción para todos sus clientes que posean su tarjeta de fidelización. La promoción consiste en aplicar un descuento por cada n productos que pasan por caja.**

**El primer descuento es de 20%, y se aplica sobre los primeros n productos ingresados. Luego,cada descuento es la mitad del anterior, y es aplicado sobre los siguientes n productos.**

**Por ejemplo, si n = 3 y la compra es de 11 productos, entonces los tres primeros tienen 20% de descuento, los tres siguientes 10%, los tres siguientes 5%, y los dos últimos no tienen descuento.**

**Escriba un programa que pida al usuario ingresar n y la cantidad de productos, y luego los precios de cada producto. Al final, el programa debe entregar el precio total, el descuento total y el precio final después de aplicar el descuento.**

**Si al aplicar el descuento el precio queda con decimales, redondee el valor hacia abajo.**

    n: 3
    Cantidad productos: 8
    Precio producto 1: 400
    Precio producto 2: 800
    Precio producto 3: 500
    Precio producto 4: 100
    Precio producto 5: 400
    Precio producto 6: 300
    Precio producto 7: 200
    Precio producto 8: 500
    Total: 3200
    Descuento: 455
    Por pagar: 2780

El archivo que contiene esta función se llama ``` descuentoPryca ``` .
