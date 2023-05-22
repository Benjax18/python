import statistics
a = [10,9,12,15,18]
b = [21,8,15,3,12]

result= a+b
print (f"A) {result} ")

result.insert(1,30) 
print (f"B) {result} ")

result.sort()
print (f"C) {result} ")

listan=[4,5,6]
result.append(listan)
print (f"D) {result} ")

result.remove(listan)

suma = sum(result)+sum(listan)
print (f"E)  La suma de la lista es: {suma} ")

media = (sum(result)+sum(listan))/14 
mediana= statistics.mean(result+listan)



print (f"F) la media es {media} y la mediana es {mediana}")
