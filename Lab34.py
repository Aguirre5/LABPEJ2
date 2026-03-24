import os
os.system("cls")

# Crear una lista de frutas y mostrar en consola
# algunas frutas de la lista, también por rebanadas.

# 5. Escribe un programa que recorra una lista de 
# frutas y muestre cada fruta.

# 5.1 Agregar otras frutas a la lista.

# 5.2 Escribe un programa verifique si una fruta 
# específica está en una lista de frutas y muestra
# un mensaje correspondiente.

listadelsuper = ["Ciruela", "Toronja", "Frutilla", "Manzana verde top 1", "Mandarin4", "Limón", "Capital de Perú", "Manzana y Cebollín"]
print(listadelsuper[0])
print(listadelsuper[1])
print(listadelsuper[2])
print(listadelsuper[0:2])

print("") # Sep otra act: Todas las frutas.
print("Lista del super-man asdjkjdasasdjjkda: ")
for fruta in listadelsuper:
    print(fruta)

print("") # Buscar una fruta mediante otro inpur...
fruta_buscada = input("Ingrese el nombre de la fruta que desea buscar: ")
if fruta_buscada in listadelsuper:
    print(f"La fruta {fruta_buscada} está en la lista.")
else:
    print(f"La fruta {fruta_buscada} no está en la lista.")
