package org.example.practica_1;
import java.util.ArrayList;
import java.util.Scanner;
/*
ejercicio a
Pedir 5 numeros, meterlos en un array y mosntrar en orden inverso
 */

public class listNumbers {
    static ArrayList<Integer> nums = new ArrayList<Integer>();
    public static void numbers() {

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
    }

}
