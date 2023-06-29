num= int(input("ingrese la cantidad de numeros a escojer: "))



def suma_par(lista): 
    suma_par=0
    for i in lista: 
        if i % 2 ==0: 
            suma_par= suma_par + i
    return suma_par

def suma_inpar(lista): 
    suma_inpar=0
    for i in lista: 
        if i % 2 !=0: 
            suma_inpar= suma_inpar + i
    return suma_inpar


l=[]
if num <0:
    print ("ingrese solo numero positivos")  
else:
    
    for i in range(num):
        numero=int (input ("ingrese la camtidad e numero: "))
        if numero >=0:
            l.append(numero)
            print(l)
        else:
            break
    
    print("la suma de los numeros es: " ,sum(l))
    print("la suma de los numeros pares es:", suma_par(l))
    print("la suma de los numeros inpares es:", suma_inpar(l))



    

