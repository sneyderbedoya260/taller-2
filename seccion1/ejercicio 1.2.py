# Ejercicio 1.2 - Calculadora basica: solicita dos numeros y una operacion
# (+, -, *, /), muestra el resultado y valida division por cero.

print("=============================================================")
print("Ejercicio 1.2 - Calculadora basica")
print("Creado por: Jostin Bedoya")
print("=============================================================")

print("Operaciones disponibles: +, -, *, /")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion matematica: ")

if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Operacion no valida.")