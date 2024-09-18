# Faca um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
# # a seguir, verifique e mostra qual a classificacao dessa pessoa.    

altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))

if altura <= 1.20 and peso <= 60:
    print("Classificação da Tabela A")

elif altura <= 1.20 and 60 <= peso <= 90:
    print("Classificação da Tabela D")

elif altura <= 1.20 and peso > 90:
    print("Classificação da Tabela G")

elif 1.20 <= altura <= 1.70 and peso <= 60:
    print("Classificação da Tabela B")

elif 1.20 <= altura <= 1.70 and 60 <= peso <= 90:
    print("Classificação da Tabela E")

elif 1.20 <= altura <= 1.70  and peso > 90:
    print("Classificação da Tabela H")

elif altura > 1.70 and peso <= 60:
    print("Classificação da Tabela C")

elif altura > 1.70 and 60 <= peso <= 90:
    print("Classificação da Tabela F ")

elif altura > 1.70 and peso > 90:
    print("Classificação da Tabela I")