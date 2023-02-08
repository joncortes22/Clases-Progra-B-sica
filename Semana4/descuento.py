cantidad = int(input("Ingrese la cantidad de producto que lleva: "))
valor = int(input("Ingrese el valor de producto que lleva: "))
factura = cantidad * valor

if cantidad >= 12:
    factura -= factura * 0.2
    print("Descuento de 20% aplicado")

print(f"El total de su factura es de {factura}")

