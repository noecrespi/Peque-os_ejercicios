// Definir una función que muestre información sobre una cadena de texto que se le pasa como argumento.A partir de la cadena que se le pasa, la función determina si esa cadena está formada sólo por mayúsculas, sólo por minúsculas o por una mezcla de ambas.


function infoCadena(cadena) {

    // Comprueba que la cadena está formada sólo por mayúsculas
    if (cadena == cadena.toUpperCase()) {
        console.log ("La cadena " + cadena + " está formada sólo por mayúsculas");
    // Comprueba que la cadena está formada sólo por minúsculas
    } else if (cadena == cadena.toLowerCase()) {
        console.log ("La cadena " + cadena + " está formada sólo por minúsculas");
    // Comprueba que la cadena está formada por una mezcla de mayúsculas y minúsculas
    } else {
        console.log ("La cadena " + cadena + " está formada por una mezcla de mayúsculas y minúsculas");
    }
}

infoCadena("HOLA MUNDO");
infoCadena("hola mundo");
infoCadena("Hola Mundo");
