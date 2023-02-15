package org.example.practica_1;

import java.util.Scanner;

/*
ejercicio i
Reciba como parámetro una cadena, y muestre el código ASCII de cada uno de los caracteres de la cadena (no devuelve nada el método).

 */
public class ascii {
    public static void changeAscii(String phrase9) {
        String pharaseAscii;

        String[] abecedario = {
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        };

        // recorrer la frase
        for (int i = 0; i < phrase9.length(); i++) {
            // para cada letra de la frase poner la posicion en el abecedario y almacenarla en pharseAscii
            char letra = phrase9.charAt(i);
            // para cada letra de la frase poner la posicion en el abecedario y almacenarla en pharseAscii
            for (int j = 0; j < abecedario.length; j++) {
                if (letra == abecedario[j].charAt(0)) {
                    pharaseAscii = j + ", ";
                }
            }

        }
    }
}
