package org.example;

import org.example.barco.Crucero;
import org.example.barco.Pesquero;
import org.example.barco.Portaaviones;

// es abstracta porque no se puede instanciar
// se puede intanciar las clases hijas por que no son abstracta
public abstract class Barco {
    public static void main(String[] args) {


            Crucero bp = new Crucero(111,2);
            Pesquero p = new Pesquero(222,2000,3);
            Portaaviones pa = new Portaaviones(333,4);
            p.alarma();
            bp.mensajeSocorro("Ay, madre");
            p.mensajeSocorro("Qué miedo");
            pa.mensajeSocorro("¡Nos hundimos!");



        //Todos los barcos tienen un comportamiento en común: los métodos alarma() y
        //mensajeSocorro()


        /*Del barco crucero se quiere guardar los metros de eslora y un contador del
        número de camas ocupadas. El contador se utilizará para almacenar el número de
        camas que se vayan creado.
                Del barco portaaviones se desea almacenar el número de aviones y el número de
        marinos. También queremos los métodos get y set de los atributos
        correspondientes, ¿Son realmente necesarios? ¿Se utilizan en algún momento?
                Explícalo con tus propias palabras.
        Del barco pesquero se guardan los metros de eslora, la potencia, el número de
        pescadores.
                Cada vez que se cree un barco deberá mostrarse un mensaje indicándose los datos
        del barco creado.
                El método alarma muestra un mensaje indicando desde qué tipo de barco se envía
        la alarma. Este método podrá ser accedido desde fuera de la clase.
        El método mensaje de socorro invoca al método alarma, y, además, muestra un
        mensaje a partir de una cadena que recibe por parámetro. Este método podrá ser
        accedido desde fuera de la clase.
        Haz un diagrama, como el visto en clase de la estructura de clases resultante y
        completa los métodos correspondientes y crea un programa principal que utilice
        los diferentes tipos de barcos y ejecuta los mensajes de socorro y alarma de
        cada uno.*/




    }

    private static void alarma() {
    }
    public void mensajeSocorro(String mensaje){
        alarma();
        System.out.println(mensaje);
    }
    
    //crear datos para que imprima 



}