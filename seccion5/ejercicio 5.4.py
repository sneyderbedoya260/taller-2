# Ejercicio 5.4 - Detector de palindromos: funcion es_palindromo(texto) que
# ignora espacios, mayusculas/minusculas y signos de puntuacion al verificar.

print("=============================================================")
print("Ejercicio 5.4 - Detector de palindromos")
print("Creado por: Jostin Bedoya")
print("=============================================================")

import string

def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    texto = texto.replace(" ", "")
    return texto == texto[::-1]

frase = input("Ingrese un texto: ")

if es_palindromo(frase):
    print("Es un palindromo.")
else:
    print("No es un palindromo.")