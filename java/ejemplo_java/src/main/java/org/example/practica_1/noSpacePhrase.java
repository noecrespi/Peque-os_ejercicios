package org.example.practica_1;

import java.util.Scanner;
/*
ejercicio f
Reciba como parámetro un texto y lo devuelva sin espacios en blanco.
 */
public class noSpacePhrase {

    public static void noSpace(String phrase6) {
        String noSpace = phrase6.replaceAll("\\s", "");
        System.out.println(noSpace);
    }
}
