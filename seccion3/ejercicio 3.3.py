# Ejercicio 3.3 - Busqueda en lista de nombres: busca un nombre ingresado
# por el usuario en una lista predefinida y muestra su posicion si existe.

print("=============================================================")
print("Ejercicio 3.3 - Busqueda en lista de nombres")
print("Creado por: Jostin Bedoya")
print("=============================================================")

nombres = ["sofia", "felipe", "diego", "isabela", "valentina"]

buscar = input("Ingrese el nombre a buscar: ")

encontrado = False

for i in range(len(nombres)):
    if nombres[i].lower() == buscar.lower():
        print(f"Nombre encontrado en la posicion {i}.")
        encontrado = True
        break

if not encontrado:
    print("Nombre no encontrado.")