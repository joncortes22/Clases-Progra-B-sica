#Ejercicio 8 Semana 2
horasSemanales = int(input("Ingrese la cantidad de horas que trabaja semanalmente: "))
precioHora = int(input("Ingrese lo que cobra por hora: "))
salarioBruto = (horasSemanales * precioHora) * 4.2
cargasSociales = salarioBruto * 0.105
asociacion = salarioBruto *0.05
print("El salario mensual es de: ", salarioBruto - cargasSociales - asociacion) 