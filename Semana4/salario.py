salario = int(input("Ingrese su salario: "))
if salario > 1000:
    salario += salario * 0.1
    print("Aumento del 15% fue emitido")
else:
    print("Salario no modificado")

print(f"Su salario es de {salario} dolares")