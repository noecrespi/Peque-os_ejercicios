package org.example.practica_1;

import java.util.ArrayList;
import java.util.Scanner;

/* ejercicio c
Leer 5 números por teclado y a continuación realizar:
    -la media de los números positivos,
    - la media de los negativos
    - contar el número de ceros que se han introducido por teclado.
 */
public class infoList {
    static ArrayList<Integer> nums = new ArrayList<Integer>();

    public static void createList() {

       Scanner sc = new Scanner(System.in);

        // Pide 5 números al usuario
        for (int i = 0; i < 5; i++) {
            System.out.println("Introduce un número");
            // nextInt() lee el número introducido por el usuario
            nums.add(sc.nextInt());
        }

        // Muestra los números introducidos
        for (int i = 0; i < nums.size(); i++) {
            System.out.println(nums.get(i));
        }

        mediaPositivos();
        mediaNegativos();
        contarCeros();
    }

    // hacer la media de los numeros positivos de nums
    public static void mediaPositivos() {
        int suma = 0;
        int contador = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) > 0) {
                suma += nums.get(i);
                contador++;
            }
        }
        System.out.println("La media de los numeros positivos es: " + suma / contador);
    }

    // hacer la media de los numeros negativos de nums
    public static void mediaNegativos() {
        int suma = 0;
        int contador = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) < 0) {
                suma += nums.get(i);
                contador++;
            }
        }
        System.out.println("La media de los numeros negativos es: " + suma / contador);
    }

    // contar el numero de ceros introducidos
    public static void contarCeros() {
        int contador = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) == 0) {
                contador++;
            }
        }
        System.out.println("El numero de ceros introducidos es: " + contador);
    }


}
