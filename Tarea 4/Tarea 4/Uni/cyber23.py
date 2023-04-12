import os
nombres = [0 for i in range(4)]
notasa = [[0 for i in range(5)] for j in range(4)]
notasd = [[0 for i in range(5)] for j in range(4)]
def ingresar():
    for i in range(len(notasa)):
        os.system('clear' if os.name == 'posix' else 'cls')
        nombres[i]= input(f"Ingrese el nombre del estudiante {i+1}: ")
        for x in range(len(notasa[0])):
            grade = int(input(f"Ingrese la nota {x+1}: "))
            notasa[i][x] = grade
            if grade >= 80 and grade <= 85: notasd[i][x] = grade+2
            elif grade >= 86 and grade <= 90: notasd[i][x] = grade+4
            elif grade >= 91 and grade <= 99: notasd[i][x] = grade+5
            elif grade == 100: notasd[i][x] = grade+10
            else: notasd[i][x] = grade
def mostrar():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('-----ANTES-----')
    cont = 0
    for f in notasa:
        print(f'Estudiante: {nombres[cont]}')
        cont += 1
        for c in f:
            print(c,end = " ")
        print('\n')

    print('-----DESPUÉS-----')
    cont = 0
    for f in notasd:
        print(f'Estudiante: {nombres[cont]}')
        cont += 1
        for c in f:
            print(c,end = " ")
        print('\n')

    input('*presione enter para continuar')

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        resp = input("""
1- Ingresar Notas
2- Mostrar Notas
Opcion: """)
        match resp:
            case '1':
                ingresar()
            case '2':
                mostrar()
            case _:
                main()

main()