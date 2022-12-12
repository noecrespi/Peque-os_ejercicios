# Objetos y métodos


**Realizaremos las actividades a partir del siguiente objeto:**

```
   var equip_ciclita = {
    team: "alfa-lum-1983",
    ciclistes: [
        {
            nom: "Juan Alonso",
            born: "08/01/1958",
            height: 1.92,
            tours: 0,
            wins: 12,
        }, {
            nom: "Josh Pantono",
            born: "25/10/2000",
            height: 1.84,
            tours: 3,
            wins: 12,
        }, {
            nom: "Bid Seville",
            born: "12/07/1993",
            height: 1.88,
            tours: 3,
            wins: 3,
        }, {
            nom: "Zolz Brucker",
            born: "08/09/1984",
            height: 1.72,
            tours: 0,
            wins: 1,
        }, {
            nom: "Otto Verdes",
            born: "19/02/1979",
            height: 1.92,
            tours: 0,
            wins: 12,
        }, {
            nom: "Bert Poel",
            born: "03/06/1995",
            height: 1.99,
            tours: 1,
            wins: 2,
        }, 
    ]
}
```


1. **Imprime nombres:** Imprime los nombres de los ciclistas, según el orden natural del array. Resultado:
    
    Juan Alonso,Josh Pantano,Bid Seville,Zolz Brucker,Otto Verdes,Bert Poel

La función que lo hace es ```names```.

2. **Imprime nombres ordenados alfabéticamente:** Imprime los nombres de los ciclistas ordenados alfabéticamente. Resultado:

    Bert Poel,Bid Seville,Josh Pantano,Juan Alonso,Otto Verdes,Zolz Brucker

La función que lo hace es ```namesAlphabetically```.

3. **Imprime nombres ordenados por altura** y luego saca la lista de los nombres ordenada por altura, de los más altos a los más bajos. Resultado:

    Bert Poel,Juan Alonso,Otto Verdes,Bid Seville,Josh Pantano,Zolz Brucker

La función que lo hace es ```orderHeight```

4. **Imprime nombres de ciclistas de mejor a peor:** Ordena de peor a mejor, teniendo en cuenta que el mejor ciclista es el que tiene más tours, y si empatan a tours, es mejor el que tiene más wins. Imprime los nombres ordenados y también el número de tours y de wins.

La función que lo hace es ```betterCiclistas```

5. Utiliza `map()` para **añadir un tour** a todos los ciclistas.

La función que lo hace es ```moreTour```.


6. Utiliza `filter()` para **eliminar todos los ciclistas** menores de 30 años

La función que lo hace es ```deleteCiclistas```.


7. Utiliza `find()` para **encontrar el primer ciclista** que tiene más de 30 años.

La función que lo hace es ```findBigCycling```.


8. **Añade un ciclista** a la posición 2 con los siguientes datos:
    
    ```
    nom: "Josh Pantano",
    born: "30/11/1995",
    height: 1.88,
    tours: 2,
    wins: 9
    ```

La función que lo hace es ```addCycling```.

09. **Imprime nombres ordenados por edad:** de más jóvenes a más viejos.

La función que lo hace es ```orderAge```.