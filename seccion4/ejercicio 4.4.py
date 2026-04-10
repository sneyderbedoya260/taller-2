# Ejercicio 4.4 - Analizador estadistico: recibe numeros separados por comas
# y calcula el maximo, minimo, suma total y promedio.

print("=============================================================")
print("Ejercicio 4.4 - Analizador estadistico")
print("Creado por: Jostin Bedoya")
print("=============================================================")

numeros = input("Ingrese numeros separados por comas: ")
lista = [float(num) for num in numeros.split(",")]

maximo = max(lista)
minimo = min(lista)
suma = sum(lista)
promedio = suma / len(lista)

print("Maximo:", maximo)
print("Minimo:", minimo)
print("Suma total:", suma)
print("Promedio:", promedio)