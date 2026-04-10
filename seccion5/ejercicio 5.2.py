# Ejercicio 5.2 - Calculadora de promedios: funcion calcular_promedio(lista)
# que retorna el promedio de una lista de numeros, validando que no este vacia.

print("=============================================================")
print("Ejercicio 5.2 - Calculadora de promedios")
print("Creado por: Jostin Bedoya")
print("=============================================================")

def calcular_promedio(lista):
    if len(lista) == 0:
        return "La lista esta vacia."
    return sum(lista) / len(lista)

numeros = input("Ingrese numeros separados por comas: ")
lista = [float(num) for num in numeros.split(",")] if numeros else []

print("Promedio:", calcular_promedio(lista))