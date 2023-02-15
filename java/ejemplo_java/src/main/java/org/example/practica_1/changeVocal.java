package org.example.practica_1;

import java.awt.*;

import java.util.Arrays;
import java.util.Scanner;

/*
ejercicio h
Reciba como parámetro una cadena y una vocal, el método sustituye todas las vocales de la cadena por la vocal que se ha pasado como parámetro (no devuelve nada).

 */
public class changeVocal {
    public static void change(String phrase8, String vocal) {

        String[] vocales = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"};

        for (String v : vocales) {
            phrase8 = phrase8.replace(v, vocal);
        }

        System.out.println(phrase8);
    }
}
