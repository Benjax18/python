
def algt_nombre(nume):
    i=0
    lis=[]
    while i < nume:

        personas =input ("ingrese el nombre de la persona")

        
        lis.append(personas)
        
        i=i+1
    print (lis)
    for i in lis:
        print (f"buenos dias crack {i}")

n=int (input ("ingrese el numero de personas que ahi: "))



algt_nombre(n)