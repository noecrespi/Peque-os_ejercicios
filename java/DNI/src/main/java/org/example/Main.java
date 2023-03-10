package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Validador de DNI");
        System.out.println("Introduce tu DNI: ");
        String dni = sc.nextLine();

        ValidarDNI validarDNI = new ValidarDNI();
        // pasar el dni a la clase ValidarDNI;

        if(validarDNI.isCorrecto(dni)){
            System.out.println("El DNI es correcto");
        } else {
            System.out.println("El DNI es incorrecto");
        }
    }
}