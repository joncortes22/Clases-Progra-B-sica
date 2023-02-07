#Ejercicio 9 Semana 2
ingresos = int(input("Ingresesos mensuales: "))
gastosAlimentacion = int(input("Ingresese los gastos por alimentación: "))
restante = ingresos - gastosAlimentacion
print("Usted gasta el ", (gastosAlimentacion*100)/ingresos, " porciento en alimentación")
print("Y le queda el ", (restante*100)/ingresos, " porciento")
