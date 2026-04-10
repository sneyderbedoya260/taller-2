# Ejercicio 3.1 - Generador de numeros pares: solicita un numero N y muestra
# todos los numeros pares desde 1 hasta N usando un ciclo for.

print("=============================================================")
print("Ejercicio 3.1 - Generador de numeros pares")
print("Creado por: Jostin Bedoya")
print("=============================================================")

N = int(input("Ingrese un numero entero positivo: "))

print(f"Numeros pares del 1 al {N}:")
for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)