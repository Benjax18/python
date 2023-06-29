# Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros ´
#positivos (N numeros) hasta que ingrese -1 (S ´ olo positivos ignorando los n ´ umeros ne- ´
#gativos). Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero ´
#mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los n ´ umeros ´
#pares, la sumatoria de los numeros impares y el promedio total. Adem ´ as, se debe impri- ´
#mir si el numero mayor obtenido es mayor, menor o igual que el promedio calculado. ´
#Asegurate de resolver este problema utilizando las funciones que consideres adecua- ´
#das

i=1
n= []
hastaque=int (input("Ingrese cuantas notas quiere ingresar"))
while i <=hastaque:
    numeros= int (input ("ingrese las notas de la asignatura de programacion: "))
    if numeros>=0:
        n.append(numeros)
    elif (numeros<=-1):
        print ("Gracias por todo")
        break
    else:
        print (" <ERROR>  ¡ingrese notas entre 1.0 y 7.0!")
        continue

    i+=1
print (n)

def numeromayor(lista):
    return max(lista)

def sumatotal(lista):
    return sum(lista)

