#Ejercicio 6 Semana 2
distancia = int(input("Ingrese la distancia de casa a la universidad: "))
costo = int(input("Ingrese el costo por kilómetro: "))
cantDias = int(input("Ingrese cantidad de días que va a la universidad: "))
costoTotal = distancia * 2 * costo * cantDias * 15
#la distancia se multiplica por 2, al ser ida y vuelta
#lo anterior se multiplca por el costo de cada km
#después se multiplica por la cantidad de días semanales
#y por último la cantidad de semanas del cuatrimestre
print("El costo del uber cuatrimestral es de: ", costoTotal)