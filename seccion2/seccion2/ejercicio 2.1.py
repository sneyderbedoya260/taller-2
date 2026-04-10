# Ejercicio 2.1 - Clasificacion de edades: determina si una persona es
# nino (0-12), adolescente (13-17), adulto (18-64) o adulto mayor (65+).

print("=============================================================")
print("Ejercicio 2.1 - Clasificacion de edades")
print("Creado por: Jostin Bedoya")
print("=============================================================")

edad = int(input("Ingrese la edad: "))

if 0 <= edad <= 12:
    print("Es un nino.")
elif 13 <= edad <= 17:
    print("Es un adolescente.")
elif 18 <= edad <= 64:
    print("Es un adulto.")
elif edad >= 65:
    print("Es un adulto mayor.")
else:
    print("Edad no valida.")