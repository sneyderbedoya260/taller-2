# Ejercicio 2.3 - Calculadora con menu mejorado: permite realizar multiples
# operaciones (suma, resta, multiplicacion, division) sin salir del programa.

print("=============================================================")
print("Ejercicio 2.3 - Calculadora con menu mejorado")
print("Creado por: Jostin Bedoya")
print("=============================================================")

while True:
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 5:
        print("Saliendo de la calculadora...")
        break

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if opcion == 1:
        print("Resultado:", num1 + num2)
    elif opcion == 2:
        print("Resultado:", num1 - num2)
    elif opcion == 3:
        print("Resultado:", num1 * num2)
    elif opcion == 4:
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("No se puede dividir por cero.")
    else:
        print("Opcion no valida.")