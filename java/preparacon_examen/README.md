# Preparación del examen

## 1 indica el valor de la variable X de cada iteración 
    
```java
    public class Main {

        public static void main(String[] args) {
            int x = 4;
            int z = x;
            
            while (x < 11) {
                if (x % 2 == 0) {
                    System.out.println(x + "es par ");
                    x=z;
                } else {
                    System.out.println(x + " es impar ");
                    z=10;
                }
                x++;
            }
        }
    }
```

Respuesta:

    4 es par
    5 es impar
    6 es par

## 2. Escribe un progama en java que en el main :
- Pida un numero entero 
```java
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // primer apartado
        System.out.println("Escribe un número entero: ");
        boolean entero = true;

        while (entero) {
            String isnum = scanner.nextLine();
            // comprobar si el numero es entero
            try {
                int num = Integer.parseInt(isnum);
                System.out.println("Es un número entero");
                entero = false;
            } catch (NumberFormatException e) {
                System.out.println("No es un número entero");
            }
        }
    }
}
```


- Genere un aleatorio entre 0 y el número pedido y lo muestre por pantalla
```java
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Escribe un número entero: ");
        boolean entero = true;

        while (entero){
            String isnum = scanner.nextLine();
            try {
                int num = Integer.parseInt(isnum);
                System.out.println("Es un número entero");

                // segundo apartado
                double ramdom = Math.random()*num+0;
                System.out.println("El número aleatorio es: " + ramdom);
                entero = false;
            } catch (NumberFormatException e) {
                System.out.println("No es un número entero");
            }
        }
    }
}
```

- Muestra los numeros impares en orden descendiente entre 0 y el número aleatorio.

```java
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escribe un número entero: ");
        boolean entero = true;

        while (entero){
            String isnum = scanner.nextLine();
            try {
                int num = Integer.parseInt(isnum);
                System.out.println("Es un número entero");

                double ramdom = Math.random()*num+0;
                System.out.println("El número aleatorio es: " + ramdom);

                // tercer apartado
                ArrayList<Integer> lista = new ArrayList<>();

                // redondear el numero aleatorio
                int redondeo = (int) Math.round(ramdom);
                //lista descendente
                for (int i = redondeo; i >= 0; i--) {
                    // si el numero es par
                    if (i % 2 != 0) {
                        lista.add(i);
                    }
                }
                System.out.println("Lista descendente: " + lista);

                entero = false;
            } catch (NumberFormatException e) {
                System.out.println("No es un número entero");
            }
        }
    }
}

```

##  3. Escribe un probrama en java que pida un identificador  de factura por 
teclado. El programa tiene que decir si este identificador es correcto o no 
usando el método de la excepción ene le caso de no ser válido.

Un identificador de facturas es considerado tiene el siguienete formato:
- Un    a mayúscula
- 4 números
- guión
- 2 números

Ejemplo: A1234-56

```java
public class Main {
    public static void main(String[] args) {
        Scanner scaner = new Scanner(System.in);

        System.out.println("Escribe el número de identificación: ");
        String id = scaner.nextLine();

        String[] abecedario = {
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        };

        // Comprobar que despues de la primera letra hay 4 digitos
        try {
            // comprobar la longitud del string
            if (id.length() > 8) {
                System.out.println("El número de identificación no es válido, debe tener 8 caracteres");
            }
            int num4 = Integer.parseInt(id.substring(1, 5));
            // comprobar los dos ultimos digitos
            int num2 = Integer.parseInt(id.substring(6, 8));

            // Comprobar que despues de los 4 digitos hay un guion
            if (id.charAt(5) != '-') {
                System.out.println("El número de identificación no es válido, despues de los 4 dígitos debe ir un guión");
            }
            // comprobar si hay una letra mayuscula
            for (int i = 0; i < abecedario.length; i++) {
                if (i == abecedario.length - 1) {
                    System.out.println("El número de identificación no es válido, la primera letra debe ser una letra mayúscula");
                }
            }

        } catch (NumberFormatException e) {
            System.out.println("El número de identificación no es válido, despues de la priemra letra debe ir un número de 4 dígitos");
        }
    }
}
```

## 4. Implementa en el código los métodos estaticos `RetonaCadenaAmbMésVocals()`
para saber cual es la cadena de caracteres con más vocales de una matriz de 
cadenas y que utiliza el método `calculaVocals()` escrito a continuación. 
- El método `retornarCadenaAmbMesVocals()` recibe por parámetro una matriz de cadenas
de caracteres y devuele la cadena con más vocales. 

## 5. 
### A
- Da la la clase `Computer` un:
  - identifiador `(id)`
  - número de aula donde está ubicada `(aula)`
  - Cantidad de memoria RAM `(ram)`
  - Capacidad de HD `(hd)`
  - Velocidad del procesador `(speed)`

    - Implementa los métodos `getRam()` y `setRam()`
    - Implementa el método `clasifica()` que devuelv una cadena de caracteres con clasificación del Computer segun las siguientes caracteristicas:
      - "ultimate" sie le valor spell es mayor que 3 y el valor de ram es mayor que 16
      - "normal" en caso contrario.

### B
- Completa la clase ArrayComputers para trabajar con un array con un máximo de 100 Compute, escribiendo el código del método:
  - `calculaMitjanaRamAula()` que recibe como parametro el aula y devuelve la media de la memoria RAM de los ordenadores que hay en el aula.

### C
- Escribe el código del método `main()` de la clase Principal (se tiene que utilizar 
los métodos creats en las clases correspondientes ) en el que tienes que: 
  - crear un objeto ``computerl`` de la clase Computer con los datos que quieras.(directamente literal, no se tiene que pedir por teclado)
  - Mostrar por pantalla el id y la clasificación de la calse computerl.
  - Crear un objeto ``arrayComputers`` de la clase ArrayComputers.
  - Añadir el objeto ``computerl`` al Objeto computers.
  - Mostrar por pantalla la media de Ram de el aula "info1" de objeto computers.