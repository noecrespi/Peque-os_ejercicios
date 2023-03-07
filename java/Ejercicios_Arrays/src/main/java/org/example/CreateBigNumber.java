package org.example;

import org.w3c.dom.ls.LSOutput;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Scanner;

//Escriba un programa Java para formar el número más grande de una lista dada de enteros no negativos
public class CreateBigNumber {


    static  ArrayList<Integer> numbers = new ArrayList<>();
    public static void bigNumber(){
        System.out.println("¿Cúantos númerosquieres que haya en la lista?");
        Scanner maxNumber = new Scanner(System.in);
        String respuesta = "";

        int max = maxNumber.nextInt();

        for (int i = 0; i < max; i++){
            System.out.println("Escribe un número: ");
            Scanner num = new Scanner(System.in);
            //añadir el número a la lista
            numbers.add(num.nextInt());
        }

        // ordenar los números de mayor a menor
        numbers.sort((o1, o2) -> o2 - o1);
        // ordenar los números de menor a mayor
        //numbers.sort((o1, o2) -> o1 - o2);

        for (int i = 0; i< numbers.size(); i++){
            respuesta += numbers.get(i);
        }
        System.out.println("El número más grande es: " + respuesta);
    }
}
