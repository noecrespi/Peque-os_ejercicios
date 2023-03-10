package org.example;

public class ValidarDNI {
// validar el dni
    public boolean isCorrecto(String dni){

        Character[] letras = {
                'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C',
                'K', 'E'};

        String dniNumeros = dni.substring(0, dni.length()-1);
        int nums = Integer.parseInt(dniNumeros);

        Character letra = dni.charAt(dni.length()-1);

        int resto = nums % 23;

        Character isLetra = letras[resto];

        String dniOgininal = dniNumeros + isLetra;

        if(dni.equals(dniOgininal)){
            return true;
        } else {
            return false;
        }
    }

}
