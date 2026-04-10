# Ejercicio 3.2 - Acumulador numerico: suma numeros ingresados por el usuario
# hasta que ingrese 0, luego muestra la suma total.

print("=============================================================")
print("Ejercicio 3.2 - Acumulador numerico")
print("Creado por: Jostin Bedoya")
print("=============================================================")

suma = 0

while True:
    numero = float(input("Ingrese un numero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("Suma total:", suma)