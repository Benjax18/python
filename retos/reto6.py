#obtener numeros del 10 al 30
list=[]
for i in range (10,31,2):
    print (i)
    list.append(i)
    
r= sum (list)

print (f"la suma total de los numeros entre 10 a 30 es igual a: {r}")