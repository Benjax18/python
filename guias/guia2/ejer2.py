# Funcion que perimta ingresar tantos nombres como el usuario quiera.
# se deben almacenar en una lista
# crear otra funcion que permita contar las letras
# la cual debe recorrer la lista de nombres y cuente la cantidad total de letras de todos los nombres ingresados
# crear una funcion para que imprima los resultados y muestre en pantalla los nombres ingresados y el total de
# letras contadas.
lista=[]
def nombresus(n_denombres):
    i=1
    while i <=n_denombres:
        nombres=input ("ingrese su nombre:")
        lista.append(nombres)
        i+=1
    return lista
numero=int (input ("ingrese cantidad de nombres a ingresar: "))
nombresus(numero)

def cuentaletras(lis):
    cantidad=[]
    for i in lis:
        cant=len(i)
        cantidad.append(cant)
    r=sum(cantidad)
    return r
suma=cuentaletras(lista)


def mostrar():
    
    print ("Estos son los nombres ingresados ")
    for i in lista:

        print (f"- {i}")
    
    print (f"La suma total de las letras de cada numero es {suma}")

if numero >=0:
    mostrar()
else:
    print ("nada de numeros negativos!")