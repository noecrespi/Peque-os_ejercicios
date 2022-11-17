# Práctica 5 – Ejercicios while y listas

**Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.**

    Escribe una palabra: viaje
    Escribe más palabras: aventura
    Escribe más palabras: cómic
    Escribe más palabras:
    
    Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']

El archivo que contiene estafunción se llama ``` palabras ``` .

**Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir números, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.**

    Escribe un número: 14
    Escribe una otro número: 123
    Escribe una otro número: -25
    Escribe una otro número: 123
    Escribe una otro número: Salir
    
    Los números que has escrito son [14, 123, -25, 123]

El archivo que contiene estafunción se llama ``` pedirNum ``` .

**Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.**
    
    Escribe una nota: 7.5
    Escribe una nota: 0
    Escribe una nota: 10
    Escribe una nota: -1

    Las notas que has Escrito son [7.5, 0.0, 10.0]

El archivo que contiene estafunción se llama ``` notasAlum ``` .

**Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide:**

    Escribe un número: 6
    Escribe un número mayor que 6: 6
    6 no es mayor que 6. Vuelve a introducir un número: 1
    1 no es mayor que 6. Vuelve a introducir un número: 8

    Los números que has escrito son 6 y 8

El archivo que contiene estafunción se llama ``` numeros ``` .

**Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números:**

    Escribe un número: 6
    Escribe un número mayor que 6: 10
    Escribe un número mayor que 10: 12
    Escribe un número mayor que 12: 25
    Escribe un número mayor que 25: 9
    Los números que has escrito son: 6, 10, 12, 25  

##### (Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista, haced esto así a partir de ahora)

El archivo que contiene estafunción se llama ``` numLAscendentes ```.

**Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.**
    
    Escribe un número: 6
    Escribe un número mayor que 6: 4
    4 no es mayor que 6. Vuelve a probar: 50
    Escribe un número entre 6 y 50: 45
    Escribe otro número entre 6 y 50: 13
    Escribe otro número entre 6 y 50: 4

    Los números situados entre 6 y 50 que has escrito son: 45, 13 

El archivo que contiene estafunción se llama ``` numList ```.

**Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.**

    Escribe límite: 50
    Escribe un valor: 10
    Escribe otro valor: 25
    Escribe otro valor: 7
    Escribe otro valor: 14

    El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56


El archivo que contiene estafunción se llama ``` sumTotal ```.


**Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.**

    Escribe límite: 50
    Escribe un valor: 10
    Escribe otro valor: 45
    45 es demasiado grande. 
    Escribe otro valor: 1
    Escribe otro valor: 39
    El límite a alcanzar es 50. 
    
    La lista creada es: 10, 1, 39

El archivo que contiene estafunción se llama ``` sumNums ```.

**Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.**

    Dame un nombre: Pepe González
    Dame el teléfono: 971971971
    Dame un nombre: Macarena Gómez
    Dame el teléfono: 971999999
    Dame un nombre: Pascual Ribot
    Dame el teléfono: 666555444
    Dame un nombre: S
    
    Los nombres y teléfonos de la agenda son:
    Pepe González: 971971971
    Macarena Gómez: 971999999
    Pasqual Ribot: 666555444

El archivo que contiene estafunción se llama ``` agenda ```.

**Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos.**

Nota: La lista en la que se guardan los nombres y notas tiene esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

    Dame un nombre: Héctor Quiroga
    Escribe una nota: 4
    Escribe otra nota: 8.5
    Escribe otra nota: 12
    Dame otro nombre: Inés Valls
    Escribe una nota: 7.5
    Escribe otra nota: 1
    Escribe otra nota: 2
    Escribe otra nota: -5
    Dame otro nombre:
    
    Las notas de los alumnos son:
    Héctor Quiroga: 4.0 - 8.5
    Inés Valls: 7.5 - 1.0 - 2.0

El archivo que contiene estafunción se llama ``` notasAlum ```.


**Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños. pista:**

```
import random
import time



minimo = int (input ( "Valor mínimo:"))
max = int (input ( "Valor máximo:"))
secreto = random.randint (mínimo, máximo)
```

    Valor mínimo: 0
    Valor máximo: 100

    A ver si adivinas un número entero entre 0 y 100.
    
    Escribe un número: 20
    
    Demasiado pequeño! Volver a probar: 30
    Demasiado grande! Volver a probar: 27
    Correcto! Lo has intentado 3 veces.

El archivo que contiene estafunción se llama ``` numMaquina ```.

**Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata. El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.**

    Valor mínimo: 0
    Valor máximo: 100
    
    Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
    
    Es 50 ?: mayor
    Es 75 ?: menor
    Es 62 ?: menor
    Es 56 ?: mayor
    Es 59 ?: igual
    Gracias por jugar!!

Mejoras (opcionales):

- que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.

- Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" y al decir "26" le decimos "menor", el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.

El archivo que contiene estafunción se llama ``` adivinaNum ```.

**Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.**

El archivo que contiene estafunción se llama ``` isPrimo ```.


**Desarrolla un programa que tenga las siguientes características:**
- Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
    
    He creado un programa de adivinar tres adivinanzas. Al final del programa te dice los intentos que has necesitado para adivinar cada adivinanza.

- Dicho problema resuélvelo con bucles for y while. 
Justifica en el propio programa porque una opción es adecuada y la otra no.

- ¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará que efectivamente una solución es más eficiente? Investiga para comprobarlo.

    Todas las opciones son efectivas, pero el `for` es para recorrer una lista sabiendo cuando acaba (después de recorrer la lista). En cambio el `while` podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera, es decir, entrará en el bucle while cuando la condición sea verdadera y no se sabe cuando falalizará.

    Por lo que supuestamente al ejecutar el `for` es más rapido que el `while` ya que el for tiene/sabe un inicio y un fin, mientras el while tienen un inicio pero no se sabe cuando será su fin por lo que puede tardar infinito.

    O sea, los dos son eficientes simplemente tienen finalidades diferentes. 

El archivo que contiene estafunción se llama ``` adivinanza ```.

