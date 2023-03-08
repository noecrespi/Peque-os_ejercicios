package org.example;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner escaner = new Scanner(System.in);
        int opcion = escaner.nextInt();

        switch (opcion) {
            case 1:
                System.out.println("Opción 1. Escriba un programa Java para comparar lexicográficamente dos cadenas. " +
                        "Dos cadenas son lexicográficamente iguales si tienen la misma longitud y contienen los mismos " +
                        "caracteres en las mismas posiciones.");
                String cadena1 = "Este es el ejercicio 1";
                String cadena2 = "Este es el ejercicio 22";
                whatMoreLarge.moreLarge(cadena1, cadena2);
                break;
            case 2:
                System.out.println("opción 2: Escriba un programa Java para contar las ocurrencias de una cadena dada en otra cadena dada.");
                String ocurrencia = "aa";
                String cadena = "abcd abc aabc baa abcaa";
                Countcurrents.count(ocurrencia, cadena);
        }
    }
}