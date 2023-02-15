package org.example.practica_1;

import java.util.Scanner;

/*
ejercicio e
Reciba como parámetro un texto y devuelva el texto al revés.
 */
public class reversePharse {

    public static void reverse(String phrase5) {

        for (int i = phrase5.length() - 1; i >= 0; i--) {
            System.out.print(phrase5.charAt(i));
        }
    }
}
