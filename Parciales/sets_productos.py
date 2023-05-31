#Se cuenta con dos sets, los cuales contienen precios de productos: (40 Puntos)
set1 = {100, 250, 300, 1000}
set2 = {150, 250, 500, 1000}


for i in set1:
    if i ==100:
        print ("en el set 1 si esta el 100")  #A) Verificar si el valor 100 está en ambos sets
        break
    elif i == 500 or i == 700:
        print("en el set 1 no esta el 100 pero si se encuentra el 500 u/o 700") #B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets
        break
for i in set1:
    r= i**3
    print (f"el numero {i} del set 1 elevado a la 3 es igual a: {r}") #C) Elevar a 3 todos los valores dentro de los sets



for i in set2:
    if i ==100:
        print ("en el set 2 si esta el 100")
        break
    elif i == 500 or i == 700:
        print("en el set 2 no esta el 100 pero si se encuentra el 500 u/o 700")
        break


for i in set2:
    r= i**3
    print (f"el numero {i} del set 2 elevado a la 3 es igual a: {r}")


list1= list(set1)
list2= list(set2)

result= set(list1+list2)

print ( f"ACTUALIZACION DEL SET: {result}")  #D) Unir ambos sets en uno solo

