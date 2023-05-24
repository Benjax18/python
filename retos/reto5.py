#Hacer un algoritmo que detecte si un número es
#par o impar, además si es un número primo y si es
#mayor o menor a 50. Para este ejercicio se solicita
#utilizar condicionales y bucles.
n=int (input ("ingrese un numero "))
while n %2 == 0:
    print (f"el {n} es un numero par")
    if n <50 and n >0:
        print ("esta entre 0 y 50")
    else:
        print (" no esta entre 0 y 50")
    break
else: 
    print (f"el {n} es un numero impar")

    if n <=50 and n >=0:
        print ("esta entre 0 y 50")
    else:
        print ("no esta entre 0 y 50")

i=1
coci=0
while i<=n:
    if n%i ==0: 
        coci=coci+1
    i=i+1
if coci == 2:
    print ("y es primo")
else:
    print ("y no es primo")
