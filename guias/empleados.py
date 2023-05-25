emple1={
    "lunes":"nocturno",
    "martes":"nocturno",
    "miercoles":"nocturno",
    "jueves":"diurno",
    "viernes":"diurno"
}
emple2={
    "martes":"nocturno",
    "miercoles":"nocturno",
    "jueves":"nocturno",
    "domingo":"diurno"
}
emple3={
    "miercoles":"diurno",
    "jueves":"diurno",
    "viernes":"diurno",
    "sabado":"nocturno",
    "domingo":"nocturno"
}



diurnoxhora=12000
nocturnoxhora=16000
extranocturno=nocturnoxhora+3000
extradiurno=diurnoxhora+2000

h_aldia=10

e1=[]
for i in emple1.items():
    key =i[0]
    valor = i[1]

    if valor == "nocturno":
        e1.append(i)
        n1= len (e1)

e1_2=[]
for i in emple1.items():
    valor = i[1]

    if valor == "diurno":
        e1_2.append(i)
        d1= len (e1_2)

dias_trabajados1=n1+d1



e2=[]
for i in emple2.items():
    key =i[0]
    valor = i[1]

    if valor == "nocturno":
        e2.append(i)
        n2= len (e2)

e2_2=[]
for i in emple2.items():
    valor = i[1]

    if valor == "diurno":
        e2_2.append(i)
        d2= len (e2_2)

dias_trabajados2=n2+d2



e3=[]
for i in emple3.items():
    key =i[0]
    valor = i[1]

    if valor == "nocturno":
        e3.append(i)
        n3= len (e3)

e3_2=[]
for i in emple3.items():
    valor = i[1]

    if valor == "diurno":
        e3_2.append(i)
        d3= len (e3_2)

dias_trabajados3=n3+d3







#MUESTRA LOS EMPLEADOS QUE TRABAJAN LOS DOMINGOS Y EN QUE TURNO

for i in emple1.items():
    key= i[0]
    valor= i[1]
    if key =="domingo":
        if valor == "diurno":
            print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia} y se le suma domingo de turno diurno {extradiurno*h_aldia}")
            
            total_semanadiur1=(extradiurno*h_aldia)*d1+(nocturnoxhora*h_aldia)*n1
            
            print(f"el total semanal del empleado 1 es igual a: {total_semanadiur1}")

            emple1["pago diario"]=total_semanadiur1

            print (emple1)

            break
        elif valor== "nocturno":
            print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia} y se le suma domingo de turno nocturno {extranocturno*h_aldia}")
            
            total_semananoc1=(diurnoxhora*h_aldia)*d1+(extranocturno*h_aldia)*n1
            
            print(f"el total semanal del empleado 1 es igual a: {total_semananoc1}")

            break
else:
    
    print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia}")
    
    total_semanasinnada1=(diurnoxhora*h_aldia)*d1+(nocturnoxhora*h_aldia)*n1
    
    print(f"el total semanal del empleado 1 es igual a: {total_semanasinnada1} no se suma nada porque no trabaja los domingos")
print ("")         
print ("DICCIONARIO ACTUALIZADO")         
emple1["total semanal"]= total_semanasinnada1
emple1["pago diario nocturno"]= nocturnoxhora*h_aldia
emple1["pago diario diurno"]= diurnoxhora*h_aldia

print (emple1)
print ("""
""")
for i in emple2.items():
    key= i[0]
    valor= i[1]
    if key =="domingo":
        if valor == "diurno":
            print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia} y se le suma domingo de turno diurno {extradiurno*h_aldia}")
            total_semanadiur2=(extradiurno*h_aldia)*d2+(nocturnoxhora*h_aldia)*n2
            print(f"el total semanal del empleado 2 es igual a: {total_semanadiur2}")
            break
        elif valor== "nocturno":
            print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia} y se le suma domingo de turno nocturno {extranocturno*h_aldia}")
            total_semananoc2=(diurnoxhora*h_aldia)*d2+(extranocturno*h_aldia)*n2
            print(f"el total semanal del empleado 2 es igual a: {total_semananoc2}")
            break
else:
    print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia}")
    total_semanasinnada2= (diurnoxhora*h_aldia)*d2+(nocturnoxhora*h_aldia)*n2
    print(f"el total semanal del empleado 2 es igual a: {total_semanasinnada2} no se suma nada porque no trabaja los domingos")
print ("")         
print ("DICCIONARIO ACTUALIZADO")         
emple2["total semanal"]= total_semanadiur2
emple2["pago diario nocturno"]= nocturnoxhora*h_aldia
emple2["pago diario diurno"]= diurnoxhora*h_aldia

print (emple2)
print (""" 
""")          
for i in emple3.items():
    key= i[0]
    valor= i[1]
    if key =="domingo":
        if valor == "diurno":
            print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia} y se le suma domingo de turno diurno {extradiurno*h_aldia}")
            total_semanadiur3=(extradiurno*h_aldia)*d3+(nocturnoxhora*h_aldia)*n3
            print(f"el total semanal del empleado 3 es igual a: {total_semanadiur3}")
            break
        elif valor== "nocturno":
            print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia} y se le suma domingo de turno nocturno {extranocturno*h_aldia}")
            total_semananoc3=(diurnoxhora*h_aldia)*d3+(extranocturno*h_aldia)*n3
            print(f"el total semanal del empleado 3 es igual a: {total_semananoc3}")
            break
else:
    print (f"este empleado recibe {diurnoxhora*h_aldia} por dia diurno y pago por dia nocturno {nocturnoxhora*h_aldia}")
    total_semanasinnada3=(diurnoxhora*h_aldia)*d3+(nocturnoxhora*h_aldia)*n3
    print(f"el total semanal del empleado 3 es igual a: {total_semanasinnada3} no se suma nada porque no trabaja los domingos")
 

print ("")         
print ("DICCIONARIO ACTUALIZADO")         
emple3["total semanal"]= total_semananoc3
emple3["pago diario nocturno"]= nocturnoxhora*h_aldia
emple3["pago diario diurno"]= diurnoxhora*h_aldia

print (emple3)


