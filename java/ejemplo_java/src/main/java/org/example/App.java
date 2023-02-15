package org.example;

import org.example.practica_1.*;
import java.util.Scanner;

/**
 * Prepara un menú que seleccione la ejecución de los diferentes ejercicios que se piden a continuación. Este menú se debe realizar con un switch.
 */
public class App {
    /**
     * Prepara un menú que seleccione la ejecución de los diferentes ejercicios que se piden a continuación.
     *Este menú se debe realizar con un switch.
     */

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        boolean activo = true;

        while (activo){
            System.out.println("Elige una opción");
            // Ejericio1
            System.out.println("1. Leer 5 números (con bucle por favor, no pongáis 5 scanner consecutivos) y " +
                    "mostrarlos en el mismo orden introducido. Los 5 números se deben almacenar en un array.\n");
            // Ejericio2
            System.out.println("2. Leer 5 números y mostrarlos en orden inverso al introducido.");
            // Ejericio3
            System.out.println("3. Leer 5 números por teclado y a continuación realizar la media de los números " +
                    "positivos, la media de los negativos y contar el número de ceros que se han introducido por " +
                    "teclado.\n");
            // Ejericio4
            System.out.println("4. Reciba como parámetro un texto y devuelva la cantidad de caracteres que incorpora " +
                    "el texto.");
            // Ejericio5
            System.out.println("5. Reciba como parámetro un texto y devuelva el texto invertido.");
            // Ejericio6
            System.out.println("6. Reciba como parámetro un texto y devuelva el texto sin espacios en blanco.");
            // Ejericio7
            System.out.println("7. Reciba como parámetro dos cadenas y las devuelva concatenadas.");
            // Ejericio8
            System.out.println("8. Reciba como parámetro una cadena y una vocal, el método sustituye todas las " +
                    "vocales de la cadena por la vocal que se ha pasado como parámetro (no devuelve nada).\n");
            // Ejericio9
            System.out.println("9. Reciba como parámetro una cadena, y muestre el código ASCII de cada uno de los " +
                    "caracteres de la cadena (no devuelve nada el método).\n");

            int opcion = keyboard.nextInt();
            Scanner entrada = new Scanner(System.in);
            switch (opcion) {
                case 1:
                    System.out.println("Has elegido la opción 1");
                    // Llamar al método
                    listNumbers.numbers();
                    break;

                case 2:
                    System.out.println("Has elegido la opción 2");
                    // Llamar al método
                    listNumsReverse.NumsReverse();

                    break;
                case 3:
                    System.out.println("Has elegido la opción 3");
                    infoList.createList();
                    break;

                case 4:
                    System.out.println("Has elegido la opción 4");
                    // Pedir frase al usuario
                    String phrase4 = entrada.nextLine();
                    // Llamar al método count
                    countPhrase.count(phrase4);
                    break;

                case 5:
                    System.out.println("Has elegido la opción 5");
                    // Pedir frase al usuario
                    String phrase5 = entrada.nextLine();
                    // Llamar al método
                    reversePharse.reverse(phrase5);
                    break;

                case 6:
                    System.out.println("Has elegido la opción 6");
                    // Pedir frase al usuario
                    String phrase6 = entrada.nextLine();
                    // Llamar al método
                    noSpacePhrase.noSpace(phrase6);
                    break;

                case 7:
                    System.out.println("Has elegido la opción 7");
                    String phrase8_1 = entrada.nextLine();
                    String phrase8_2 = entrada.nextLine();
                    // Llamar al método addPhrases
                    addPhrases.add(phrase8_1, phrase8_2);
                    break;
                case 8:
                    System.out.println("Has elegido la opción 8");
                    // Pedir frase al usuario
                    String phrase8 = entrada.nextLine();
                    String vocal = entrada.nextLine();
                    changeVocal.change(phrase8, vocal);
                    break;
                case 9:
                    System.out.println("Has elegido la opción 9");
                    // Pedir frase al usuario
                    String phrase9 = entrada.nextLine();
                    // Llamar al metodo
                    ascii.changeAscii(phrase9);
                    break;
                default:
                    System.out.println("La opción NO válida");
                    break;
            }
        }
    }
}
