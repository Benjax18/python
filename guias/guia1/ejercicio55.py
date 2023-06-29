#ejercicio número 5 de la guia
import random

lista_de_numeros=[]

for i in range(20):
  número=random.randrange(40,350)
  lista_de_numeros.append(número)
print("numeros generados")
print(lista_de_numeros)

buscar_numero = int(input("ingrese un número que quiera buscar:"))

ocurrencias= lista_de_numeros.count(buscar_numero)

print("número de ocurrencias en el número ingresado")
print(ocurrencias)

