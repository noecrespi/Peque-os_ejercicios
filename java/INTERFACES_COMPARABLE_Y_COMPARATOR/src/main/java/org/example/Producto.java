package org.example;

import java.awt.*;
import java.util.ArrayList;

public class Producto implements Comparable<Producto>  {
    // Implementar una clase producto teniendo en cuenta que, cada producto tiene un nombre, un precio y un código.
    // Debemos tener en cuenta que trabajaremos con listas de productos.

    private String nombre;
    private double precio;
    private int codigo;

    // lista de productos
    static ArrayList<Producto> productos = new ArrayList<Producto>();

    public Producto() {
    }

    public Producto(String nombre, double precio, int codigo) {
        this.nombre = nombre;
        this.precio = precio;
        this.codigo = codigo;
    }


    // getters y setters

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public static ArrayList<Producto> getProductos() {
        return productos;
    }

    public void setProductos(ArrayList<Producto> productos) {
        Producto.productos = productos;
    }

    // agregar producto
    public static void addProducto(Producto producto) {
        productos.add(producto);
    }

    //Ordenar la lista de productos por precio de forma descendente.
    public static void ordenarDescendiente() {
        productos.sort((o1, o2) -> (int) (o2.getPrecio() - o1.getPrecio()));
        for (Producto producto : productos) {
            System.out.println(producto);
        }
    }

    public static void ordenarAscendiente() {
        productos.sort((o2, o1) -> (int) (o2.getPrecio() - o1.getPrecio()));
        for (Producto producto : productos) {
            System.out.println(producto);
        }
    }

    @Override
    public int compareTo(Producto otroProducto) {
        return Double.compare(this.precio, otroProducto.precio);
    }


    // toString
    @Override
    public String toString() {
        return "Producto{" +
                "nombre='" + nombre + '\'' +
                ", precio=" + precio +
                ", codigo=" + codigo +
                '}';
    }
}
