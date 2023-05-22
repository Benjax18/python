# crear dos listas ciudades y indice de calidad de aire
ciu=["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indi_cali_aire=[134,99,245,50]

#buscar indice mas bajo y alto
bajo=min(indi_cali_aire)
alto=max(indi_cali_aire)
ciumenor=ciu[indi_cali_aire.index(bajo)] #llamado a ciudad para que nos diga en que posicion se encuentra el indice de aire mas bajo
ciumayor=ciu[indi_cali_aire.index(alto)] 

print (f" el indice de calidad de aire mas bajo es de {ciumenor} con el indice de calidad de aire {bajo}")


if (bajo>0 and bajo<=50):
    print ("Y esta en la categoria de buena")
elif (bajo>=51 and bajo<=100):
    print ("Y esta en la categoria de moderado")
elif (bajo>=101 and bajo<=150):
    print ("Y esta en la categoria de Dañina a la salud para grupos sensibles")
elif (bajo>=151 and bajo<=200):
    print ("Y esta en la categoria de Dañina a la salud")
elif (bajo>=201 and bajo<=300):
    print ("Y esta en la categoria de Muy dañina a la salud")
elif (bajo>300):
    print ("Y esta en la categoria de Peligrosa")
else:
    print("no se encuentra")

print (f" el indice de calidad de aire mas bajo es de {ciumayor} con el indice de calidad de aire {alto}")

if (alto>0 and alto<=50):
    print ("Y esta en la categoria de buena")
elif (alto>=51 and alto<=100):
    print ("Y esta en la categoria de moderado")
elif (alto>=101 and alto<=150):
    print ("Y esta en la categoria de Dañina a la salud para grupos sensibles")
elif (alto>=151 and alto<=200):
    print ("Y esta en la categoria de Dañina a la salud")
elif (alto>=201 and alto<=300):
    print ("Y esta en la categoria de Muy dañina a la salud")
elif (alto>300):
    print ("Y esta en la categoria de Peligrosa")
else: 
    print ("no se encuentra")

