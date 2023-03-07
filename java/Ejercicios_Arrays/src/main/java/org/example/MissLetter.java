package org.example;

import java.util.Scanner;

// Escriba un programa Java que devuelva la letra que falta de una matriz de letras crecientes (superiores o inferiores)
// . Suponga que siempre faltará una letra en la matriz.
public class MissLetter {

    static String[] abecedario = {
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    };
    public static void cearch(String letras){
        // convertir las letras en minusculas
        String minusculas = letras.toLowerCase();

        for(int i = 0; i < abecedario.length; i++){
            for(int j =0; j < minusculas.length(); j++){
                //coger la primera letra de la palabra

                // si la letra del abecedario es igual a la letra de la palabra
                if(!minusculas.contains(abecedario[i])){
                    System.out.println("La letra que falta es: " + abecedario[i]);
                    break;
                }
            }
        }



    }
}
