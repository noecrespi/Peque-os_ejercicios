package org.edu.programacion;

//8
public class CuentaSuperCorriente extends CuentaCorriente{
    public CuentaSuperCorriente(String numCuenta, Double saldo) {
        super(numCuenta, saldo);
    }
    @Override
    public void pagarIntereses(){
        //throw new UnsupportedOperationException("No se puede pagar intereses en una cuenta super corriente");
    }
    }
