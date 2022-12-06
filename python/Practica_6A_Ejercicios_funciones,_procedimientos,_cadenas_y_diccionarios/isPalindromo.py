# Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla: 

#       Dime algo: Salta lenin el atlas
#       Salta lenin el atlas es palíndromo

#       Dime algo: dabale arroz a la zorra el abad
#       dabale arroz a la zorra el abad 


frase = input("Dime algo: ")

def isPalindromo(frase):
    
    # Eliminamos los espacios en blanco
    # Pasamos todo a minúsculas
    frase1 = frase.replace(" ", "").lower()

    if frase1 == frase1[::-1]:
        print(frase + " Es palindromo")
    else:
        print(frase + " No es palindromo")

isPalindromo(frase)