package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isRunning = true;

        while (isRunning) {
            // Menu
            System.out.println("Elige una opción:");
            System.out.println("1. Escriba un programa Java para formar el número más grande de una lista dada de " +
                    "enteros no negativos");

            System.out.println("9. Escriba un programa Java que devuelva la letra que falta de una matriz de letras " +
                    "crecientes (superiores o inferiores). Suponga que siempre faltará una letra en la matriz.");

            // input
            int option = scanner.nextInt();
            // entradas
            Scanner entrada = new Scanner(System.in);

            // Procesos
            switch (option) {
                case 1:
                    System.out.println("Has elegido la opción 1");
                    CreateBigNumber.bigNumber();
                    break;
                case 9:
                    System.out.println("Has elegido la opción 9");
                    System.out.println("Escribe letras del abecedario: ");
                    String letras = entrada.nextLine();
                    MissLetter.cearch(letras);
                    break;



                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }
    }
}