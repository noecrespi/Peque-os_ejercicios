#Pida al usuario un importe en euros y diga si el cajero automático le 	puede dar dicho importe utilizando el mismo billete y el más grande ∫

# import math
# from nis import match


def cambioBilletes():

    importe = int(input("Intruduce el importe en euros: "))

    billete500 = 500
    billete200 = 200
    billete100 = 100
    billete50 = 50
    billete20 = 20
    billete10 = 10
    billete5 = 5

    if(importe % 5 == 0):
        # combrueba si se le puede devolver todo el importe con billetes de 500
        if(importe % billete500 == 0):
            cambio = math.floor(importe / billete500)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete500))
        # combrueba si se le puede devolver todo el importe con billetes de 200
        elif(importe % billete200 == 0):
            cambio = math.floor(importe / billete200)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete200))
        # combrueba si se le puede devolver todo el importe con billetes de 100
        elif(importe % billete100 == 0):
            cambio = math.floor(importe / billete100)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete100))
        # combrueba si se le puede devolver todo el importe con billetes de 50
        elif(importe % billete50 == 0):
            cambio = math.floor(importe / billete50)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete50))
        # combrueba si se le puede devolver todo el importe con billetes de 20
        elif(importe % billete20 == 0):
            cambio = math.floor(importe / billete20)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete20))
        # combrueba si se le puede devolver todo el importe con billetes de 10
        elif(importe % billete10 == 0):
            cambio = math.floor(importe / billete10)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete10))
        # combrueba si se le puede devolver todo el importe con billetes de 5
        elif(importe % billete5 == 0):
            cambio = math.floor(importe / billete5)
            print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete5))
    else: 
        print("El cajero no puede devolver el dinero solicitado")

cambioBilletes()

# def cambioBilletes():

#     importe = int(input("Intruduce el importe en euros: "))

#     BILLETES = [500, 200, 100, 50, 20, 10, 5]

#     if(importe % 5 == 0):
#         for billete in BILLETES:
#             if(importe % billete == 0):
#                 cambio = math.floor(importe / billete)
#                 print("El cambio de " + str(importe) + " es de " + str(cambio) + " billetes de " + str(billete))
#     else: 
#         print("El cajero no puede devolver el dinero solicitado")

# cambioBilletes()