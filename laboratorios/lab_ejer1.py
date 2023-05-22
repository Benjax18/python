info_region1={
    "id":8,
    "nombre":"biobio",
    "superficie": 23890,
    "habitantes": 1556805,

}
info_region2= {
    "id":10,
    "nombre":"los lagos",
    "superficie":48583,
    "habitantes": 828708
}

print (""" 
COMIENZO
""")
print (info_region1)# SE IMPRIME DICCIONARIO
print ("")
print (info_region2)

h = int (info_region1["habitantes"])
s = int (info_region1["superficie"])

re=h/s
info_region1["densidad"]=round (re,1) #CREA LA NUEVA CLAVE "DENSIDAD"




h = int (info_region2["habitantes"])
s = int (info_region2["superficie"])

re=h/s
info_region2["densidad"]=round (re,1)




info_region1["capital"]= "concepcion" # CREA LA OTRA CLAVE LLAMADA "CAPITAL"
info_region2["capital"]= "puerto montt"

info_region1["comunas"]= ["lota","lebu","los angeles"] #CREA NUEVA CLAVE LLAMADA "COMUNAS"
info_region2["comunas"]= ["castro","puerto varas","purranque"]

info_region1["provincia"]= ("biobio","arauco","concepcion") #CREA NUEVA CLAVE LLAMADA "PROVINCIAS"
info_region2["provincia"]= ("osorno","llanquihue","palena")

print (""" 
ACTUALIZACION
""")
print (info_region1)
print ("")
print (info_region2) # POR ULTIMO IMPRIME DICCIONARIO ACTUALIZADO