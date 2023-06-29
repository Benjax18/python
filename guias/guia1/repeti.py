# obtener cuantas veces se repite universidad en el siguiente parrafo

parr= """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica."""
r=parr.lower()
result= r.count("universidad")

print (f"Universidad en el texto se repite: {result} veces.")

