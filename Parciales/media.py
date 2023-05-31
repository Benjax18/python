#Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
#más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
#notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1.0 ni
#mayores a 7.0

import statistics
i=1
notas= []
while i <=10:
    valornotas= float (input ("ingrese las notas de la asignatura de programacion: "))
    if valornotas>=1.0 and valornotas<=7.0:
        notas.append(valornotas)
        
    else:
        print (" <ERROR>  ¡ingrese notas entre 1.0 y 7.0!")
        continue

    i+=1

media=statistics.mean(notas)

print (f"la media es: {media}")
listamala=[]
for i in notas:
    if i < media:
        listamala.append(i)
print (f"las notas mas bajas que la media son: {listamala}")
listabuena=[]
for i in notas:
    if i>media:
        listabuena.append(i)
print (f"las notas mas altas que la media son: {listabuena}")
    