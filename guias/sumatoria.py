# tiene un patron que va aumentado y el otro disminuyendo que llega hasta 800
n1=[]
for i in range (500,802,10):
    n1.append(i)


n2=[]
for i in range (456,-2,-2):
    n2.append(i)


r= int (sum(n1))
r2= int (sum(n2))

final= r+r2

print (f"La sumatoria final es: {final}")


