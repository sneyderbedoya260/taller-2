# Ejercicio 3.5 - Eliminador de duplicados: solicita 10 numeros y muestra
# la lista original y una nueva lista sin duplicados, usando ciclos y lista auxiliar.

print("=============================================================")
print("Ejercicio 3.5 - Eliminador de duplicados en lista")
print("Creado por: Jostin Bedoya")
print("=============================================================")

numeros = []
sin_duplicados = []

for i in range(10):
    num = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(num)

for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)