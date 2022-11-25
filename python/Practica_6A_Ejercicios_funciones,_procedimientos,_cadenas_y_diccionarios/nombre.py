# Escribe un programa que lea (entrada por teclado) el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final será imprimida por el programa por pantalla

# nombre
print("¿Cómo te llamas?")
nombre = str(input())

# apellido 1
print("¿Cúal es tu primer apellido?")
apellido1 = str(input())

# apellido 2
print("¿Cúal es tu segundo apellido?")
apellido2 = str(input())

# controla que si el usuario no tiene un segundo apellido no lo pone
def nombreCompleto(nombre, apelllido1, apellido2 = ""):
    print(nombre + " " +  apellido1 + " " + apellido2)

nombreCompleto(nombre, apellido1, apellido2)