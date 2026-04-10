# Ejercicio 5.3 - Refactorizacion de calculadora con funciones: cada operacion
# matematica se define en una funcion separada invocada desde el menu principal.

print("=============================================================")
print("Ejercicio 5.3 - Calculadora con funciones")
print("Creado por: Jostin Bedoya")
print("=============================================================")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    return a / b

while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "5":
        print("Saliendo de la calculadora...")
        break

    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opcion invalida.")