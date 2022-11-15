// Escribir el código de una función a la que se pasa como parámetro un número entero y devuelve como resultado una cadena de texto que indica si el número es par o impar. Mostrar por pantalla el resultado devuelto por la función.


function parImpar(numero) {
    
    if (numero % 2 == 0) {
        console.log ("El número " + numero +  " es par");
    } else {
        console.log ("El número " + numero +  " es impar");
    }
}

parImpar(2);
parImpar(3);
parImpar(33);
parImpar(22);
