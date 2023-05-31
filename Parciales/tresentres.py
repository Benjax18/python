#Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
#valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
#divisibles por 5, y la suma de los enteros generados que sean impares.
lista= []
for i in range(2,30,3):
    
    
    lista.append(i)

print (f"estos son todos los numeros desde 2 y menores que 30 {lista}")
listcinco=[]
for i in lista:
    
    if i %5 ==0:
        listcinco.append(i)
r_divicinco=sum(listcinco)
print (f"la suma de los numeros divisibles de 5: {r_divicinco}")

listaimpa=[]
for i in lista:
    if i%2==1:
        listaimpa.append(i)
r_impa=sum(listaimpa)
print (f"la suma de los valores impares: {r_impa}")