# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.


def notas():
    
        notas = []
        nota = float(input("Escribe una palabra: "))
    
        while(nota > 0 and nota <= 10):
            notas.append(nota)
            nota = float(input("Escribe una palabra: "))
        
        print("Las palabras que el usuario ha metido son: " + str(notas))
        print(notas)

notas()
