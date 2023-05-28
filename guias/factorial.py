def factorial(n):
   if n== 0:
      return 1
   else:
      print(n)
      return n *factorial(n-1)
      
   

n= int(input("Introduzca un numero\n"))

ress=factorial(n)
print(f"El numero {n} su factorial es {ress}")