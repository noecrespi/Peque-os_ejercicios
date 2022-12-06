# Is primo?

# Escribe un programa que le pida al usuario si quiere calcular si un número es primo deberéis utilizar for o con while, por tanto, habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra (con while). Ambas funciones devolverán true (si es primo) o false (si no es primo). El programa principal informará del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra. 

# Comentario: aprovecha el código que tienes ya creado


# Con for

import time



def isPrimo():
    num  = int(input("Introduce un número: "))
    

    for n in range(2,num):
        if (num % n) == 0:
            print("El numero " + str(num) + " no es primo = False")
            print("for" + time.time())
            return False
    
    print("El numero " + str(num) + " es primo = True")
    print("for" + time.time())
    return True


isPrimo()


# Con while


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
                return True
                print("El numero " + str(num) + " es primo = True")
                print("while" + time.time())
            else:
                return False
                print("El numero " + str(num) + " no es primo = False")
                print("while" + time.time())
            


isPrimo()