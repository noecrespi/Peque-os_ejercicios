package org.edu.programacion;

public class CuentaSuperJoven extends CuentaJoven {
    public CuentaSuperJoven(String numCuenta, Double saldo) {
        super(numCuenta, saldo);
    }
    @Override
    public void pagarIntereses(){
        this.setSaldo(this.getSaldo() * 1.10);
    }
}

