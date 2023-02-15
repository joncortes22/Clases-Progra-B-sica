
"""resultado = 1
valor = int(input("Ingrese un valor:"))
while valor > 0:
    resultado *= valor
    valor -= 1
print(resultado)"""
i = 1
while i<=12:
    j = 1
    while j<=12:
        print(i,"x",j,"=",i*j)
        j+=1
    i+=1
