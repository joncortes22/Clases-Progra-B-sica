
estudiantes = 1
mayor = 0
menor = 0
aprobados = 0
reprobados = 0
seguir = True
while seguir == True:
    entrada = int(input(f"Ingrese la nota del estudiante: {estudiantes}: "))
    estudiantes += 1
    if entrada>mayor: mayor = entrada
    if estudiantes == 0: menor = entrada
    elif entrada < menor: menor = entrada
    if entrada>=70: aprobados += 1
    else: reprobados += 1
    resp = int(input("Desea seguir ingresando? 1-Si 2-No: "))
    if resp == 2: break

print(f"""
Nota mayor: {mayor}
Nota mayor: {menor}
Aprobados: {aprobados}
Reprobados: {reprobados}""")

