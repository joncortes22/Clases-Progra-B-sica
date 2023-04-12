import os
campers = []
limpieza = [[],[]]
def leer():
    if os.path.isfile("campers.txt") == False: open("campers.txt", "w+").close()
    lista = open("campers.txt").readlines()
    for i in range(len(lista)):  
        campers.append(lista[i].replace('\n', '').split('|'))
    
    if os.path.isfile("limpieza.txt") == False: open("limpieza.txt", "w+").close()
    lista = open("habitaciones.txt").readlines()
    for i in range(len(lista)): 
        limpieza.append(lista[i].replace('\n', '').split('|'))

    
def acamper():
    os.system('clear' if os.name == 'posix' else 'cls')
    


def ccamper():
    pass

def rhoras():
    pass

def choras():
    pass

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    resp = input("""
1- Agregar Camper
2- Consultar Camper
3- Registrar Horas
4- Consultar Horas

Opcion: """)
    match resp:
        case '1':
            acamper()
        case '2':
            acamper()
        case '3':
            acamper()
        case '4':
            acamper()
        case _:
            main()
            
if __name__ == "__main__":
    main()