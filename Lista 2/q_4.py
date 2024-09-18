# Questão 4
# Faca um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
# O numero digitado ao quadrado
# A raiz quadrada do numero digitado

n = int(input("Insira um número positivo :"))
nAoquadrado = n ** 2
nRaizquadrada = n ** 0.5
if n > 0:
    print(f"Numero ao quadrado :", nAoquadrado,"Raiz quadrada :", nRaizquadrada)
else :
    print("Numero inválido!!")