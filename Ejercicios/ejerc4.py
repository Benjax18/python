# isoceles 2 lados iguales 
# equilatero 3 lado iguales 
# escaleno ningun lado igual 


lado1=int (input ("ingresa el primer lado "))
lado2=int (input ("ingresa el segundo lado "))
lado3=int (input ("ingresa el tercer lado "))
p=(lado1+lado2+lado3)/2
area= p*(p-lado1)*(p-lado2)*(p-lado3)
area=area**0.5
area=round (area,2) #sacar solo dos decimales


if ((lado1>0) and (lado2>0) and (lado3>0) ):
    if (lado1==lado2!=lado3):
        print ("es un triagulo isoceles")
        print (f"el perimetro de este triangulo es de {p} y el area es de {area}")
        

    elif (lado2==lado3!=lado1):
        print ("es un triangulo isoceles")
    elif (lado3==lado1!=lado2):
        print ("es un triagulo isoceles")

    if (lado1==lado2 and lado2==lado3 and lado3==lado1):
        print(" Triangulo equilatero")
        print (f"el perimetro de este triangulo es de {p} y el area es de {area}")
    if (lado1!=lado2 and lado2!=lado3 and lado3!=lado1):
        print ("es un triangulo escaleno")
        print (f"el perimetro de este triangulo es de {p} y el area es de {area}")

