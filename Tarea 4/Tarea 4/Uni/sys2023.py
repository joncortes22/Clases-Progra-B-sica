import os
def ingresar():
    os.system('clear' if os.name == 'posix' else 'cls')
    info = []
    info.append(input('Nombre del estudiante: '))
    nota = int(input('Nota: '))
    info.append(str(nota))
    if nota >= 80 and nota <= 90: info.append('Categoria C')
    elif nota >= 91 and nota <= 95: info.append('Categoria B')
    elif nota >= 96 and nota <= 100: info.append('Categoria A')
    else: info.append('Sin Categoria')
    return info
def escribir():
    estudiantes = ingresar()
    if not os.path.isfile('estudiantes.txt'): open('estudiantes.txt', 'w+').close()
    with open('estudiantes.txt', 'a') as f:
        for i in range(len(estudiantes)):
            f.write(f'{estudiantes[i]}\n')

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        resp = input("1-Ingresar estudiante de honor")
        match resp:
            case '1': 
                escribir()
            case _: main()

main()