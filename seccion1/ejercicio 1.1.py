# Ejercicio 1.1 - Registro de usuario: solicita nombre, edad y ciudad,
# muestra un mensaje personalizado y valida que la edad sea positiva.

print("=============================================================")
print("Ejercicio 1.1 - Registro de usuario")
print("Creado por: Jostin Bedoya")
print("=============================================================")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad de residencia: ")

if edad > 0:
    print(f"Hola {nombre}, tienes {edad} anos y vives en {ciudad}.")
else:
    print("La edad ingresada no es valida. Debe ser un numero positivo.")