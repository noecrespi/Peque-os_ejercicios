package org.example.practica_1;

import java.util.ArrayList;
import java.util.Scanner;
/*
ejercicio b
 */
public class listNumsReverse {
    static ArrayList<Integer> nums = new ArrayList<Integer>();
    public static void NumsReverse() {

        Scanner sc = new Scanner(System.in);

        // Pide 5 números al usuario
        for (int i = 0; i < 5; i++) {
            System.out.println("Introduce un número");
            // nextInt() lee el número introducido por el usuario
            nums.add(sc.nextInt());
        }

        // Muestra los números introducidos en al reves
        for (int i = nums.size() - 1; i >= 0; i--) {
            System.out.println(nums.get(i));
        }
    }

}
