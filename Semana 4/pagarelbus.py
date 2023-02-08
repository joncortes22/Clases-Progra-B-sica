edad = int(input("Ingrese su edad: "))
pagar = 1500
if edad < 3 or edad > 65:
    pagar = 0

print(f"Debe pagar {pagar} colones")