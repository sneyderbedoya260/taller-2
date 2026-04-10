# Ejercicio 1.4 - Validador de contrasena segura: verifica minimo 8 caracteres,
# una mayuscula, un numero y un caracter especial (!@#$%^&*).

print("=============================================================")
print("Ejercicio 1.4 - Validador de contrasena segura")
print("Creado por: Jostin Bedoya")
print("=============================================================")

contrasena = input("Ingrese una contrasena: ")

errores = []

if len(contrasena) < 8:
    errores.append("Debe tener al menos 8 caracteres.")
if not any(c.isupper() for c in contrasena):
    errores.append("Debe contener al menos una letra mayuscula.")
if not any(c.isdigit() for c in contrasena):
    errores.append("Debe contener al menos un numero.")

caracteres_especiales = "!@#$%^&*"
if not any(c in caracteres_especiales for c in contrasena):
    errores.append("Debe contener al menos un caracter especial (!@#$%^&*).")

if len(errores) == 0:
    print("Contrasena segura.")
else:
    print("La contrasena no cumple con los siguientes criterios:")
    for error in errores:
        print("-", error)