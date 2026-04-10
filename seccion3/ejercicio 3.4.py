# Ejercicio 3.4 - Tabla de multiplicar interactiva: genera la tabla del 1 al 10
# de un numero y pregunta si desea generar otra, repitiendo hasta que el usuario salga.

print("=============================================================")
print("Ejercicio 3.4 - Tabla de multiplicar interactiva")
print("Creado por: Jostin Bedoya")
print("=============================================================")

while True:
    numero = int(input("Ingrese un numero para ver su tabla: "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    opcion = input("Desea generar otra tabla? (s/n): ").lower()
    if opcion != "s":
        break