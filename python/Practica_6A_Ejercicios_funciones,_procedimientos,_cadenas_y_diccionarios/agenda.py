# Desarrolla un programa, que nos sirva para gestionar nuestros contactos (la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. El programa tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto a partir de la clave, consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento (diccionarios, funciones, procedimientos…).
# MAPEO DE LA UNA BBDD 
# contactos = {
#         0: {
#             'nombre': 'nombre', 
#             'apellido1': '1', 
#             'apellido2': '2', 
#             'telefono': '98', 
#             'correo': 'jsbdnjs'
#             }, 
#         1: {
#             'nombre': 'noe',
#             'apellido1': '1',
#             'apellido2': '2',
#             'telefono': '98', 
#             'correo': 'jsbdnjs'
#             }, 
#         2: {
#             'nombre': 'noe', 
#             'apellido1': 'casa', 
#             'apellido2': '2', 
#             'telefono': '98', 
#             'correo': 'jsbdnjs'
#         }}


contactos = {}
contar = 1

def agenda():
    print(" ------------------------------------------------")
    print("|            Agenda de contactos                 |")
    print(" ------------------------------------------------")
    print("|    Opcciones:                                  |\n ------------------------------------------------")

    print("     - Añadir contacto")
    print("     - Consultar contacto")
    print("     - Eliminar contacto")
    print("     - Consultar todos los contactos\n")
    print(" ------------------------------------------------")
    print("|    - Para salir del programa escriba 'salir'  |")

    add = True 

    while add:
        opcion = input("Opcion: ")
        if opcion == "Añadir contacto":
            print( addContacto())
        elif opcion == "Consultar todos los contactos":
            print( consultarContactos())
        elif opcion == "eliminar":
            print( eliminarContacto())
        elif opcion == "consultar":
            print( consultarContacto())
        elif opcion == "salir":
            add = False
        else:
            print("Opcion no valida")



# Añadir contacto
def addContacto():
    contacto = {}
    nombre = input("Nombre: ")
    apellido1 = input("Apellido 1: ")
    apellido2 = input("Apellido 2: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    
    contacto["nombre"] = nombre
    contacto["apellido1"] = apellido1
    contacto["apellido2"] = apellido2
    contacto["telefono"] = telefono
    contacto["correo"] = correo
    contar = len(contactos)
    
    contactos[contar] = contacto
    contar += 1
    # print(contactos)
    return contactos
    
    

# Consultar todos los contactos
def consultarContactos():
    for i in contactos:
        print(contactos[i])
        # return contactos[i]



# Eliminar contacto por el primer apellido
def eliminarContacto():
    eliminar = input("Escriba el apellido del contacto que quieres eliminar: ")
    
    for i in contactos:
        if contactos[i]["apellido1"] == eliminar:
            contactos.pop(i)
            # print("Contacto eliminado")
            print(contactos)
            return "¡Contacto eliminado correctamente!"
        # else:
        #     print("Contacto no encontrado")



# Consultar contacto
def consultarContacto():
    consultar = int(input("Escriba la clave del contacto que quieresconsultar: "))
    for i in contactos:
        if i == consultar: 
            print(contactos[i])
            break
        else:
            print("Contacto no encontrado")



agenda()
