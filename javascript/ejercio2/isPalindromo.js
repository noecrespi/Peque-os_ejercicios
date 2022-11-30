// Definir una función que determine si la cadena de texto que se le pasa como parámetro es un palíndromo, es decir, si se lee de la misma forma desde la izquierda y desde la derecha.

// Entiendo que os caractesres especiales tambien cuentan ya que se considera que  


function isPalindromo(cadena){

    // tratamiento del la cadena para luego compararlo
    cadena1 = cadena.toLowerCase().split(" ").join();
    cadenaReverse = cadena1.toLowerCase().split("").reverse().join("");

    console.log(cadena)
    console.log(cadena1)
    console.log(cadenaReverse)

    // Compruena que la cadena tenga el mismo numero de letas tanto si la palabra está del derecho cómo del reves 
    // Ademaás tienen que ser totalmente iguales 
    if (cadena1.length == cadenaReverse.length && cadena1 == cadenaReverse){
        console.log("La cadena " + cadena + " es un palíndromo")
    } else{
        console.log("La cadena " + cadena + " no es un palíndromo");
    }
}

isPalindromo("abba")
isPalindromo("Hola Mundo")
isPalindromo("Amo la paloma")
