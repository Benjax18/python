dic= {
    "nombre":"benja",
    "apellido":"miranda"
    }

for key,valor in dic.items():

    print (key)
    print (valor)

tpl=[1,23,4,5]

print (tpl[1])

def funcion(**diccionario):
    print (diccionario)

funcion(hola="pepe") #el primero es la clave y el segundo el valor