# Ejercicio 5.1 - Generador de saludos personalizados: funcion saludar(nombre, hora)
# que retorna un saludo segun la hora del dia (dias 5-12, tardes 13-19, noches 20-4).

print("=============================================================")
print("Ejercicio 5.1 - Generador de saludos personalizados")
print("Creado por: Jostin Bedoya")
print("=============================================================")

def saludar(nombre, hora):
    if 5 <= hora <= 12:
        return f"Buenos dias {nombre}"
    elif 13 <= hora <= 19:
        return f"Buenas tardes {nombre}"
    else:
        return f"Buenas noches {nombre}"

nombre = input("Ingrese su nombre: ")
hora = int(input("Ingrese la hora (0-23): "))
print(saludar(nombre, hora))