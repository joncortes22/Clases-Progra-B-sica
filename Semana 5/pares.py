i = int(input("Ingrese el valor inicial: "))
f = int(input("Ingrese el valor final: "))
for i in range(i,f):
    if i % 2 == 0: print(f"Numero: {i}, y su cuadrado es {i**2}")


i = int(input("Ingrese el valor inicial: "))
f = int(input("Ingrese el valor inicial: "))
while i<f:
    i += 1
    if i % 2 == 0:
        print(f"{i}, su cuadrado es: {i**2}")