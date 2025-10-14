#20. Inventario con diccionario

def mostrarMenu():
    print("--------Menu----------")
    print("1.Agregar producto")
    print("2.Modificar cantidad")
    print("3.Mostrar inventario")
    print("4.salir")

inventario = {}

while True:
    mostrarMenu()
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        producto = input("Nombre del producto: ").strip().lower()
        if producto in inventario:
            print("El producto ya existe")
        else:
            
            cantidad = int(input("Dame la cantidad: "))
            inventario[producto] = cantidad
            print("El producto" , producto , "has agregado con cantidad: " , cantidad)
    elif opcion == "2":
        producto = input("Dime el nombre del producto que quieres modificarlo: ")
        if producto in inventario:
            new_cantidad = int(input("Dame un nueva cantidad: "))
            inventario[producto] = new_cantidad
        else:
            print("El producto " , producto , "no existe")
    elif opcion == "3":
        print("Inventario actual: ")
        for clave, valor in inventario.items():
            print(producto , "-->" , valor)
    elif opcion == "4":
        print("Adios")
        break
    else:
        print("opcion no válida")

            