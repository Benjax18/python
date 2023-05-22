n1=int (input ( "ingrese el primer numero: ..."))
n2=int (input ( "ingrese el segundo numero: ..."))
n3=int (input ( "ingrese el tercer numero: ..."))

while (n1>0 and n2>0 and n3>0):
    if (n1>n2):
        if (n3<n1):
            print (f"el numero mayor es: {n1}")
    if (n2>n1):
         if (n3<n2):
            print(f"el numero mayor es {n2}")
    if (n3>n2):
         if (n1<n3):
            print(f"el numero mayor es {n3}")
    if (n3==n2 and n1==n2 and n3==n1):
        print ("iguales")

    break







