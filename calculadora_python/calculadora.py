

import math

print("\n******************* Calculadora em Python *******************")

def add(x, y) : 
    return x + y

def subtract(x, y) : 
    return x - y

def multiply(x, y) : 
    return x * y

def divide(x, y) : 
    return x / y


print("\nSelecione o número da operação desejada:  \n")
print(" 1 - Soma")
print(" 2 - Subtracao")
print(" 3 - Multiplicacao")
print(" 4 - Divisao")

operation = input("\nDigite sua operacao (1/2/3/4): \n")
num1 = int(input("\nDigite o primeiro numero: "))
num2 = int(input("\nDigite o segundo numero: "))

if operation == "1":
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif operation == "2":
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")
    
elif operation == "3":
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")
elif operation == "4":
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")
else :
    print("\nOpcao inválida")