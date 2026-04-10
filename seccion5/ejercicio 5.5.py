# Ejercicio 5.5 - Factorial recursivo: funcion recursiva factorial(n) que calcula
# el factorial de un numero entero, con validacion para numeros negativos.

print("=============================================================")
print("Ejercicio 5.5 - Factorial recursivo")
print("Creado por: Jostin Bedoya")
print("=============================================================")

def factorial(n):
    if n < 0:
        return "No existe factorial para numeros negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un numero entero positivo: "))
print("Factorial:", factorial(numero))