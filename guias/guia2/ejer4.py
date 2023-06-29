# hacer un programa que funcione como un cajero
# funcion que le ingrese el dinero con el que pagara el cliente 
# funcion que diga cuanto le sobra 


precio_t= int (input ("ingrese precio total: "))
monto_para_pagar= int (input ("ingrese monto con el que pagara: "))

def calculevuelto(total,monto):
    resultado = monto - total
    return  resultado

def mostrar():
    print (f"precio a pagar: {precio_t} CLP")
    print (f"usted pago con: {monto_para_pagar} CLP")
    print (f"su vuelto es igual a: {calculevuelto(precio_t,monto_para_pagar)} CLP")
i=1

while i>0:

    if precio_t < 0 or monto_para_pagar<0:
        print ("no se puede ingresar monto menor a 0")
    else:
        if monto_para_pagar >=precio_t:
            mostrar()        
        else:
            print ("f saldo insuficiente")
    
    op=input ("""desea hacer otra operacion? 
    exit= salir       enter para continuar...""")
    op=op.lower()
    if op == "exit":
        print ("\n")
        print ("MUCHAS GRACIAS POR SU COMPRA!")

        break
    else:
        precio_t= int (input ("ingrese precio total: "))
        monto_para_pagar= int (input ("ingrese monto con el que pagara: "))
    i+=1




