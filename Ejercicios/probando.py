ciu=["Santiago", "Temuco", "Osorno", "Punta Arenas","Copiapo"]
indi_cali_aire=[134,99,245,50,301]
print ("""La informacion esta en las siguientes ciudades
Santiago
Temuco
Osorno
Punta Arenas
Copiapo""")
ciu_info= indi_cali_aire[ciu.index(input ("ingrese la ciudad: "))]
cd= ciu[indi_cali_aire.index(ciu_info)]


if (ciu_info>0 and ciu_info<=50):
    print (f"el indice de calidad de aire de {cd} es de {ciu_info} Y esta en la categoria de buena")
elif (ciu_info>=51 and ciu_info<=100):
    print (f"el indice de calidad de aire de {cd} es de {ciu_info} Y esta en la categoria de moderada")
elif (ciu_info>=101 and ciu_info<=150):
    print (f"el indice de calidad de aire de {cd} es de {ciu_info} Y esta en la categoria de dañina a la salud para grupos sensibles")
elif (ciu_info>=151 and ciu_info<=200):
    print (f"el indice de calidad de aire de {cd} es de {ciu_info} Y esta en la categoria de dañina a la salud")
elif (ciu_info>=201 and ciu_info<=300):
    print (f"el indice de calidad de aire de {cd} es de {ciu_info} Y esta en la categoria de muy dañina a la salud")
elif (ciu_info>300):
    print (f"el indice de calidad de aire de {cd} es de {ciu_info} Y esta en la categoria de peligrosa")


