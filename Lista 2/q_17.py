#Questão 17
# Faca um programa que calcule e mostre a area de um trapezio. Sabe-se que:
# A = (basemaior + basemenor) ∗ altura / 2

bMa = int(input("Insira o valor da base maior: "))
bMe = int(input("Insira o valor da base menor: "))
altura = int(input("Insira o valor da altura : "))

areaTrapezio = (((bMa + bMe) * altura)/2)
print(areaTrapezio)