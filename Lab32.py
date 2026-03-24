import os
os.system("cls")

# Escribe un programa que muestre
# los números del 0 al 4 usando un ciclo while.
"""
n = 0
while n < 5:
    print(n)
    n += 1
"""
# Escribe un programa que solicita al usuario
# que ingrese números enteros positivos y muestre
# la suma de esos números. La entrada de números
# continuarà hasta que el usuario ingrese un 
# número negativo, momento en el que el programa 
# mostrarà la suma total.

number = 0
acum = 0

while number >= 0:
    number = int(input("Ingrese un número entero positivo (o un número negativo para terminar): "))
    if number >= 0:
        acum += number

print(f"La suma total es: {acum}")