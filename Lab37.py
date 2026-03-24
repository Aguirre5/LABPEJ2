import os
os.system("cls")

# Integrador:
# Escribe un programa que permita a un usuario crear
# una lista de nombres. El programa continuará pidiendo
# nombres hasta que el usuario ingrese "fin". Luego, 
# el programa mostrará la lista de nombres en orden alfabético,
# indicará cuántos nombres empiezan con la letra 'A' o 'E', 
# y mostrará si un nombre específico está en la lista.

nombres = []

print("Aquí puedes poner los nombres que quieras.")
print("Para cocncluir, escribe 'Fin.'.")

while True:
    nombre = input("Nombre: ")
    if nombre == "Fin.":
        break
    nombres.append(nombre)
    
print(f"{nombres}" )

print(f"Los nombres en orden alfabético son: {nombres}")

for nombre in nombres:
    
    letrainicial = nombre[0].lower()

    if letrainicial == "a":
        print(f"El nombre '{nombre}' empieza con 'A'.")
    elif letrainicial == "e":
        print(f"El nombre '{nombre}' empieza con 'E'.")
    else:
        print(f"El nombre '{nombre}' no empieza con 'A' ni con 'E'.")