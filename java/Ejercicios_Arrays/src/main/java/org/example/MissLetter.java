package org.example;

import java.util.Scanner;

// Escriba un programa Java que devuelva la letra que falta de una matriz de letras crecientes (superiores o inferiores)
// . Suponga que siempre faltará una letra en la matriz.
public class MissLetter {

    public static void cearch(String letras){
        // convertir las letras en minusculas
        String minusculas = letras.toLowerCase();
        String respuesta = "";

        for (int i = 0; i < minusculas.length() - 1; i++){
            // si la letra es diferente a la siguiente letra
            // porque se añade menos uno
            if (minusculas.charAt(i) != minusculas.charAt(i + 1) - 1){
                // la letra que falta es la siguiente letra
                respuesta = String.valueOf((char) (minusculas.charAt(i) + 1));
                break;
            }
        }
        System.out.println("La letra que falta es: " + respuesta);


    }
}
