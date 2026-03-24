import os
os.system("cls")

# 7. Escribe un programa que recorra una cadena de 
# texto y cuente cuántas veces aparece la letra 'a' en la cadena.

ph = input("Escribe una frase motivacional: ")
print("")
a = 0

for letras in ph:
    if letras == "a":
        a += 1

print(f"Hay {a} letras 'a' en la frase: {ph}")