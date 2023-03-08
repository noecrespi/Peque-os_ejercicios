package org.edu.programacion;
git
// 4 abstract: no se puede instanciar
public abstract class Cuenta {

    // atributos
    //1
    public String numCuenta;
    public double saldo;
    // static: se comparte entre todas las instancias de la clase
    private static int contador = 0 ; // almacena el número de cuentas que se han creado

    // constructor por defecto
    //2
    public Cuenta (){
        this.numCuenta = "";
        this.saldo = 0;
    }
    // constructor con parámetros
    public Cuenta (String numCuenta, Double saldo){
        this.numCuenta = numCuenta;
        this.saldo = saldo;
    }

    // método abatrscto 3
    public abstract void pagarIntereses();

    // métodos getter y setter

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }
}
