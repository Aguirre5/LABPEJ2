import os
os.system("cls")


# 6. Escribe un programa que recorra una lista
# de números y muestre si cada número es par o impar.

listaaesthethic = [5, 3/4, 2, 9, 1/8, 9, 0]

for n in listaaesthethic:
    if n % 2 == 0:
        print(f"El número {n} obvi que es par.")
    else:
        print(f"El número {n} es impares.")