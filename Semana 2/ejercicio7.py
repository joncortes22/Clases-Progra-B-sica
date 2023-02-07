#Ejercicio 7 Semana 2
edades = []
for i in range(5):
    edades.append(int(input(f"Ingrese la edad {i+1}: ")))
Suma = 0
for i in range(5):
    Suma += edades[i]
print("El promedio de edades es de: ", Suma / 5)

