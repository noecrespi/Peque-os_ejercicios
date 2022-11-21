# Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.

# En enste caso es mejor usar el for ya que es más sencillo y más rápido de ejecutar.
# En cambio el while es más complicado y más lento de ejecutar.

def isPrimo():
    listaPrimos = True


    while listaPrimos == True:
        primo = True
        num  = int(input("Introduce un número: "))
        
        if num == 0:
            return False
        else: 
            for n in range(2,num):
                if (num % n) == 0:
                    primo = False
            
            if primo == True:
                print("El numero " + str(num) + " es primo")
            else:
                print("El numero " + str(num) + " no es primo")
            


isPrimo()


