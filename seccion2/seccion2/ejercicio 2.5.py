# Ejercicio 2.5 - Simulador de descuentos por categoria: aplica descuento
# segun categoria (A=20%, B=15%, C=10%) y muestra el total a pagar y el ahorro.

print("=============================================================")
print("Ejercicio 2.5 - Simulador de descuentos por categoria")
print("Creado por: Jostin Bedoya")
print("=============================================================")

categoria = input("Ingrese su categoria (A, B, C): ").upper()
monto = float(input("Ingrese el monto de la compra: "))

descuento = 0

if categoria == "A":
    descuento = 0.20
elif categoria == "B":
    descuento = 0.15
elif categoria == "C":
    descuento = 0.10
else:
    print("Categoria no reconocida. No se aplica descuento.")

ahorro = monto * descuento
total = monto - ahorro

print(f"Descuento aplicado: ${ahorro:.2f}")
print(f"Total a pagar: ${total:.2f}")