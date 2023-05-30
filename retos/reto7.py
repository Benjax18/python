# escribir una funcion que reciba una frase por teclado
# devuelva un diccionario con las palabras que contiene y su longitud 

def generador(fra):
    fra=list(fra)

    longitud = len(fra)

    dic={

    }
    dic["frase"]=fra
    dic ["Longitud"]=longitud
    return dic


fra=input ("ingrese ")
print (generador(fra))