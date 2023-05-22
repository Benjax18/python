# Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de Programaci´on. Luego obtener el promedio ponderado de la
#siguiente manera:
#Promedio Ponderado = Lab1 * 0,3 + Lab2 * 0,4 + Lab3 * 0,3
#Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprob´o
#la asignatura. Si el promedio es superior a 4,0, indicar que el estudiante aprobo
#la asignatura. Si la nota es superior 6,0, debe mostrar el mensaje: el estudiante
#aprobo con distinci´on

ramo_prg={
    1: input ("ingrese nota de laboratorio 1: "),
    2: input ("ingrese nota de laboratorio 2: "),
    3: input ("ingrese nota de laboratorio 3: ")
}

lab1= int(ramo_prg[1])* 0.3
lab2= int (ramo_prg[2])*0.4
lab3= int (ramo_prg[3])* 0.3

pm_final= lab1+lab2+lab3

print (round (pm_final,0))
if pm_final>0.0 and pm_final <=3.0:
    print ("fuera")
elif pm_final>=4.0 and pm_final<=5.9 :
    print ("el estudiante aprobo de pura suerte")
elif pm_final>=6.0 and pm_final<=7.0 :
    print ("el estudiante aprobo con distincion")
else:
    print (f"tu nota es : {pm_final} en que pais estamos? esto es chile las notas van del 0 al 7")