package org.example.barco;
import org.example.Barco;

public class Portaaviones extends Barco {

    //Del barco portaaviones se desea almacenar el número de aviones y el número de
    //marinos. También queremos los métodos get y set de los atributos



    int numAviones;
    int numMarinos;

    String mensaje = "Mensaje desde barco portaaviones";

    // constructor
    public Portaaviones(int numAviones, int numMarinos) {
        this.numAviones = numAviones;
        this.numMarinos = numMarinos;
        System.out.println("Barco portaaviones creado");
    }

    public int getNumAviones() {
        return numAviones;
    }

    public void setNumAviones(int numAviones) {
        this.numAviones = numAviones;
    }

    public int getNumMarinos() {
        return numMarinos;
    }

    public void setNumMarinos(int numMarinos) {
        this.numMarinos = numMarinos;
    }

    public void alarma(){
        System.out.println("Alarma desde barco portaaviones");
    }

    public void mensajeSocorro(String mensaje){
        alarma();
        System.out.println(mensaje);
    }
}
