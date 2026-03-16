print("------- Sistema de Tienda -------")

# Metodo que calcula el total de la compra
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


while True:

    print("Menu Principal")
    print("1. Calcular total de compra")
    print("2. Salir")

    opcion = int(input("Ingrese el numero de la opcion: "))

    if opcion == 1:

        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos: "))

        resultado = calcular_total(precio, cantidad)

        print("El total de la compra es:", resultado)

    elif opcion == 2:
        print("Gracias por usar el sistema.")
        break

    else:
        print("El numero ingresado no es correcto. Intente nuevamente.")