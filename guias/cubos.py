n = int(input("Introduzca un numero\n"))

impar = (n*(n-1)) + 1
acum = 0
print(impar)
for i in range(n):
    acum = acum + impar
    if i == (n-1):
        break
    impar = impar + 2
    print(impar)

print(f"el numero {n} su cubo es {acum}")