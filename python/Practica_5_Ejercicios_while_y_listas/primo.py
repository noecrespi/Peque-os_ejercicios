# decir si el numero es primo o no

def isPrimo():
    x = True


    while x == True:
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