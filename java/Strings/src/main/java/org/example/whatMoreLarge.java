package org.example;

//Escriba un programa Java para comparar lexicográficamente dos cadenas. Dos cadenas son lexicográficamente iguales si
// tienen la misma longitud y contienen los mismos caracteres en las mismas posiciones.
public class whatMoreLarge {



    public static void moreLarge(String cadena1, String cadena2){

        if (cadena1.length() > cadena2.length()){
            System.out.println("La cadena 1 es mayor que la cadena 2");
        } else if (cadena1.length() == cadena2.length()){
            System.out.println("Las cadenas son iguales");
        } else {
            System.out.println("La cadena 1 es menor que la cadena 2");
        }
}
}
