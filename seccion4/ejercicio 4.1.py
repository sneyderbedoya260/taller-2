# Ejercicio 4.1 - Lista de compras: permite agregar, eliminar y mostrar
# productos en una lista usando un menu interactivo.

print("=============================================================")
print("Ejercicio 4.1 - Lista de compras")
print("Creado por: Jostin Bedoya")
print("=============================================================")

lista_compras = []

while True:
    print("\n--- MENU ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        producto = input("Ingrese el producto: ")
        lista_compras.append(producto)
        print("Producto agregado.")
    elif opcion == "2":
        producto = input("Ingrese el producto a eliminar: ")
        if producto in lista_compras:
            lista_compras.remove(producto)
            print("Producto eliminado.")
        else:
            print("El producto no esta en la lista.")
    elif opcion == "3":
        if lista_compras:
            print("Lista actual:")
            for item in lista_compras:
                print("-", item)
        else:
            print("La lista esta vacia.")
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion invalida.")