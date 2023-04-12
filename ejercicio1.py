import os
dialogo = []
def leer():
    list = open("dialogo.txt").readlines()
    for i in range(len(list)):  
        dialogo.append(list[i].replace('\n', '').replace(',','').replace('.',''))

    if os.path.isfile("resultado.txt") == False: open("resultado.txt", "w+").close()

def write(word):
    info = [[0 for i in range(2)] for j in range(8)]
    for i in range(len(dialogo)):
        linea = dialogo[i].split()
        c = 0
        for x in range(len(linea)): 
            if linea[x].lower() == word: c+=1
        if c > 0: info[i] = [i+1,c]
        else: info[i] = [i+1,0]

    print(f'Palabra a buscar: {word}')
    for i in range(len(info)): print(f"Linea {i+1} - {info[i][1]}")

    with open("resultado.txt", 'a') as f: 
        f.write(f'Palabra a buscar: {word}\n')
        for i in range(len(dialogo)): f.write(f"Linea {i+1} - {info[i][1]}\n")
    
    input('*presione enter para continuar')
    main()

def main():
    leer()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        word = input('Ingrese una palabra: ')
        write(word)

if __name__ == '__main__':
    main()