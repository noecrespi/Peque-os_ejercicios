package org.example;
// importar la clase Producto

public class Main {
    public static void main(String[] args) {

        Producto producto1 = new Producto("Camiseta", 9.79, 1);
        Producto producto2 = new Producto("Jeans", 15.99, 2);
        Producto producto3 = new Producto("Blusa", 25.90, 3);

        // Añadir productos a la lista con la función addProducto de la clase Producto
        Producto.addProducto(producto1);
        Producto.addProducto(producto2);
        Producto.addProducto(producto3);

        // Imprimir los productos agregados
        System.out.println("Lista de productos:");
        for (Producto producto : Producto.getProductos()) {
            System.out.println(producto);
        }

        // ordenar productos por precio
        //System.out.println("Lista de productos ordenados por precio descendiente:");
        //Producto.ordenarDescendiente();

        // ordenar productos por precio
        //System.out.println("Lista de productos ordenados por precio ascendiente:");
        //Producto.ordenarAscendiente();

        System.out.println("Lista de productos ordenados por precio descendiente:");
        Producto.getProductos().sort(Comparable::compareTo);
        for (Producto producto : Producto.getProductos()) {
            System.out.println(producto);
        }

        // Ordenar la lista de productos por nombre (usando Comparator)
        System.out.println("Lista de productos ordenados por nombre ascendente:");
        ProducComparator productoComparator = new ProducComparator();
        Producto.getProductos().sort(productoComparator);
        for (Producto producto : Producto.getProductos()) {
            System.out.println(producto);
        }

    }

}