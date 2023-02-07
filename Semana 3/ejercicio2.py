#Ejercicio 2 Semana 3
n1 = int(input("Ingrese el primer valor != 0: "))
n2 = int(input("Ingrese el segundo valor != 0: "))
print("La suma de estos valores es: ", n1+n2)
print("La resto de estos valores es: ", n1-n2)
try:
    div = n1 / n2
    print("La división de estos valores es: ", div)
except ZeroDivisionError:
    print("Se intentó dividir ente 0 :(")
print("La multiplicación de estos valores es: ", n1*n2) 