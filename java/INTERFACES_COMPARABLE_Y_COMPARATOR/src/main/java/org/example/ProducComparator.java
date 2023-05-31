package org.example;

import java.util.Comparator;

public class ProducComparator implements Comparator<Producto> {
    @Override
    public int compare(Producto producto1, Producto producto2) {
        return producto1.getNombre().compareTo(producto2.getNombre());
    }
}
