num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))
if num2 != 0:
    resultado = num1 / num2
    print(f"El resultado de su división es {resultado}")
else:
    print("ERROR, divisor no puede ser 0")