import os

matriz = [[32,24,15],[12,31,54],[9,23,71]]

def mostrar():
    for i in range(len(matriz)): print(matriz[i])
    print('\n')

def acomodar():
    for i in range(len(matriz)): matriz[i].sort()

def main():
    mostrar()
    acomodar()
    mostrar()

main()