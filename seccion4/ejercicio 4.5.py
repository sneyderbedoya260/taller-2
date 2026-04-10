# Ejercicio 4.5 - Comparador avanzado de listas: recibe dos listas y muestra
# los elementos comunes, unicos de la primera y unicos de la segunda (sin conjuntos).

print("=============================================================")
print("Ejercicio 4.5 - Comparador avanzado de listas")
print("Creado por: Jostin Bedoya")
print("=============================================================")

lista1 = input("Ingrese la primera lista separada por comas: ").split(",")
lista2 = input("Ingrese la segunda lista separada por comas: ").split(",")

comunes = []
unicos1 = []
unicos2 = []

for elemento in lista1:
    if elemento in lista2:
        comunes.append(elemento)
    else:
        unicos1.append(elemento)

for elemento in lista2:
    if elemento not in lista1:
        unicos2.append(elemento)

print("Elementos comunes:", comunes)
print("Unicos en lista 1:", unicos1)
print("Unicos en lista 2:", unicos2)