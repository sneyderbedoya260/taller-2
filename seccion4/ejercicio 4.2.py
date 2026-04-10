# Ejercicio 4.2 - Directorio de contactos: gestiona un diccionario nombre->telefono,
# permitiendo agregar, buscar y eliminar contactos.

print("=============================================================")
print("Ejercicio 4.2 - Directorio de contactos")
print("Creado por: Jostin Bedoya")
print("=============================================================")

directorio = {}

while True:
    print("\n--- DIRECTORIO DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        directorio[nombre] = telefono
        print("Contacto agregado.")
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in directorio:
            print("Telefono:", directorio[nombre])
        else:
            print("Contacto no encontrado.")
    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        if nombre in directorio:
            del directorio[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")
    elif opcion == "4":
        print("Saliendo del directorio...")
        break
    else:
        print("Opcion invalida.")