import statistics
n_enteros=[4,3,8,12,6,10,14,3,6]

n_enteros.pop(-1)
n_enteros.insert(0,2)
sete=set(n_enteros) #pasamos a set la lista porque en un set no puede haber nada repetido
lista=list(sete)# luego lo volvemos a transformar en lista

promedio = statistics.mean(lista) #sacamos promedio con funcion mean de la libreria statistics
medio = statistics.median(n_enteros) #sacamos promedio con funcion mean de la libreria statistics
print (f" asi quedaria la lista:  {lista}")
print (f" el promedio es igual a {promedio}")
print (f" el medio de la lista es igual a {medio}")
