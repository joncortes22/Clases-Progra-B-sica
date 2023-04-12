import os
nums = []

def analize():
    print("Numeros mayores a 5 e impares:")
    for i in range(len(nums)):
        if nums[i] > 5 and nums[i]%2 == 1: print(nums[i])

def ingreso():
    for i in range(10): nums.append(int(input(f"Ingrese el numero {i+1}: ")))
    analize()

def main():
    ingreso()

main()