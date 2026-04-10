# Ejercicio 1.3 - Validacion de correo electronico: verifica que el correo
# contenga "@" y "." en posiciones validas.

print("=============================================================")
print("Ejercicio 1.3 - Validacion de correo electronico")
print("Creado por: Jostin Bedoya")
print("=============================================================")

correo = input("Ingrese su direccion de correo electronico: ")

if "@" in correo and "." in correo and correo.index("@") < correo.rindex("."):
    print("Direccion de correo electronico valida.")
else:
    print("Direccion de correo electronico no valida.")