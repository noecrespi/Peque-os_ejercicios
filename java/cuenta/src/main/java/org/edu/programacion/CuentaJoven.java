package org.edu.programacion;

// 6
public class CuentaJoven extends Cuenta {

    public CuentaJoven(String numCuenta, Double saldo) {
        super(numCuenta, saldo);
    }

    @Override
    public void pagarIntereses(){
        this.setSaldo(this.getSaldo() * 1.05);
    }

    // 7

}
