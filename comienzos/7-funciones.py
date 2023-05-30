#Comenzando a generar funciones 
# el fin de las funciones es reutilizar un codigo sin repetir varias veces el mismo 


def primer_func():                 # primer def luego el nombre de la funcion los parentesis y doble punto
    print ("esta es mi primera funcion")
primer_func() #asi se llama a la funcion 

# Funcion + Listas

def concatenar (lista1,lista2): # el objetivo de esta funcion es concatenar
    return lista1+lista2     # return (retornar) devolvera el valor de concatenar dos listas
lista1=[1,2,3]
lista2=[4,5,6]

# concatenar() esto devolvera error ya que no llamamos los parametros

print (concatenar(lista1,lista2)) # mostramos el valor de la funcion con print 

# declarando un funcion de multiplicacion

def multi (n1,n2):
    return n1*n2

print (multi(4,5)) #ingresa dos numeros que se multiplicaran

# declarando una funcion de suma y resta

def suma(a,b):
    return a+b
def resta (a,b):
    return a-b

a= int (input ("ingrese un numero "))
b= int (input ("ingrese otro numero "))

rsum= suma(a,b)
rresta= resta(a,b)

print (f"la suma de estos numero es: {rsum}")
print (f"la resta de estos numero es: {rresta}")

#funcion simple
def saludar ():
    print ("hola benyi que tal?")

saludar()

#funcion con parametros (variables que se crean para ser usadas dentro de solo la funcion)

def saludo (nombre, sexo):
    sexo=sexo.lower() #convierte todo en minuscula para que en los if no tenga errores

    if sexo =="mujer":
        adjetivo='reyna'
    elif sexo =="hombre":
        adjetivo='rey'
    else:
        adjetivo='amor'
    
    print (f"hola {nombre} como esta mi {adjetivo}")

saludo("compadre","hombre") #llama a la funcion dandole valores a cada parametro


#crear una funcion que retorne valores 
