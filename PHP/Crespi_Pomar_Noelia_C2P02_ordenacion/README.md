# Algoritmo de ordenación

## Introduccion
Implementar en PHP 2 algoritmos de entre los numerados. La descripción de estos algoritmos están presentados en el pdf "Algoritmos de ordenación" de esta unidad.

1. Burbuja
1. Inserción directa.
1. Selección directa.
1. Intercambio.

Los valores a ordenar serán números enteros.

Despliegue:  nom_corporativo.dwes.randion.es

DocumentRoot: /var/www/ifc33{letra_del_grupo}/{nom_corporativo}/dwes

Repositorio en classroom.github.com:  dwes-{nom_corporativo}

## Intrucciones de envio
Se enviará un único fichero zip que contendrá el código fuente de todos los algoritmos programados. El código estará debidamente documentado y se valorará si estos comentarios siguen el estándar de PHPDoc, similar a JavaDoc.

Este fichero se nombrará de acuerdo con el siguiente convenio de denominación:

    apel1_apel2_nom_C2P02_ordenacion.zip

### CRITERIOS DE EVALUACIÓN
**Criterio 1 (Máxima puntuación: 1 puntos; Ponderación: 1)**

Sobre la fecha de entrega del envío:
- 0 ⇾ Entregada fuera de plazo.
- 1 ⇾ Entregada en plazo.

Observación: la ponderación de este aspecto, representa aproximadamente un 5,5% de la nota. Es decir, una calificación de 10/10 se transformaría en un 9,4/10 si se entrega fuera de plazo.

 

**Criterio 2 (Máxima puntuación: 3 puntos; Ponderación: 1)**
Sobre el seguimiento de los convenios de denominación del fichero entregado

Orientaciones:
- No:  0  puntos.
- No en todos los apartados, de una manera desigual: de 1 a 2 puntos.
- Totalmente: 3 puntos

**Criterio 3 (Máxima puntuación: 8 puntos; Ponderación: 2)**

Sobre la estructuración:
- El código está perfectamente estructurado y en el orden descrito en el enunciado: de 0 a 3 puntos.

Sobre la documentación del código fuente:
- El código está documentado de modo que es fácil de comprender: de 0 a 2 puntos.
- Sigue las directrices del documentador PHPDoc. de 0 a 3 puntos

**Criterio 4 (Máxima puntuación: 6 puntos; Ponderación: 10)**

Por la realización de los siguientes algoritmos:
- Algoritmo de ordenación 1 ⇾ 0 a 3 puntos
- Algoritmo de ordenación 2 ⇾ 0 a 3 puntos.

**Criterio 5 (Máxima puntuación: 8 puntos; Ponderación: 4)**
Formulario web, método de entrada de datos (solo 1 método es obligatorio, los demás son opcionales pero puntúan):

1) Matriz predeterminada, incorporada en el código, 0 a 1 punto.
2) Generación aleatoria de enteros. Seleccionará desde el formulario la cantidad de números a generar. 0 a 2 puntos.
3) Entrada por teclado. 0 a 2 puntos.
4) Entrada por fichero (txt, json, xml, etc a elegir). 0 a 3 puntos.


**¡Observaciones!**, he tenido que ampliar mi memria limite de php ya que al intentar generar una lista random con una longitud indeterminada y que podria ser bastante grande he tenido que ir: 
1. Ir a la terminal, buscar donde esta el archivo de configuración:
    ```
    php --ini
    ```
2. Buscar `memory_limit`, cambiar: 
    
    memory_limit = ~~128M~~  256M

3. Guardar los cambios 

