package org.example.barco;

import org.example.Barco;

public class Crucero extends Barco {
    //Del barco crucero se quiere guardar los metros de eslora y un contador del
    //número de camas ocupadas. El contador se utilizará para almacenar el número de
    //camas que se vayan creado.

    int metrosEslora;
    int numCamasOcupadas;

    String mensaje = "Mensaje desde barco crucero";

    // constructor
    public Crucero(int metrosEslora, int numCamasOcupadas) {
        this.metrosEslora = metrosEslora;
        this.numCamasOcupadas = numCamasOcupadas;
        System.out.println("Barco crucero creado");
    }


    //crear contador de camas
    public void contadorCamas(){
        numCamasOcupadas++;
    }

    public void alarma(){
        System.out.println("Alarma desde barco crucero");
    }

    public void mensajeSocorro(String mensaje){
        alarma();
        System.out.println(mensaje);
    }



}
