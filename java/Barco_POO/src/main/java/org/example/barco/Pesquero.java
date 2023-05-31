package org.example.barco;

import org.example.Barco;

public class Pesquero extends Barco {

    //Del barco pesquero se guardan los metros de eslora, la potencia, el número de
    //pescadores.

    double metrosEslora;
    int potencia;
    int numPescadores;

    String mensaje = "Mensaje desde barco pesquero";


    // constructor
    public Pesquero(double metrosEslora, int potencia, int numPescadores) {
        this.metrosEslora = metrosEslora;
        this.potencia = potencia;
        this.numPescadores = numPescadores;
        System.out.println("Barco pesquero creado");
    }


    public void alarma(){
        System.out.println("Alarma desde barco pesquero");
    }

    public void mensajeSocorro(String mensaje){
        alarma();
        System.out.println(mensaje);
    }
}
