#Ejercicio 4 Semana 3
edadLuis = int(input("Ingrese la edad de Luis: "))
edadPedro = int(input("Ingrese la edad de Pedro: "))
print("La edad de Luis es: ", edadLuis)
print("La edad de Pedro es: ", edadPedro)
aux = edadPedro
print("CAMBIO DE EDADES")
edadPedro = edadLuis
edadLuis = aux
print("La edad de Luis es: ", edadLuis)
print("La edad de Pedro es: ", edadPedro)