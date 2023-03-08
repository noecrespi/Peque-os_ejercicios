package org.example;

public class Countcurrents {

    public static void count(String ocurrencia, String cadena){

        int contador = 0;

        for (int i = 0; i < cadena.length() -1; i++) {
            if (cadena.charAt(i) == ocurrencia.charAt(0) && cadena.charAt(i+1) == ocurrencia.charAt(1)){
                contador++;
            }
        }
        System.out.println("La ocurrencia de la cadena es: " + contador);
    }
}
