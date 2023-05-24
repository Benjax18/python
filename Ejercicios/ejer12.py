
n=int (input("ingresa un numero"))
i=1
coci=0
while i<=n:
    if n%i ==0: 
        coci=coci+1
    i=i+1
if coci ==2:
      print ("es primo")
else:
      print ("no eri mi primo")
