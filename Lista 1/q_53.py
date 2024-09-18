#Questão 53
print("=================================================================")
print("O preço por metro é equivalente a COMPRIMENTO * LARGURA")
print("=================================================================")
c = int(input("Insira o comprimento do terreno(METRO) :"))#COMPRIMENTO
print("=================================================================")
l = int(input("Insira a largura do terreno(METRO) :"))#LARGURA

p = c * l #PREÇO POR METRO
print("=================================================================")
print(f"Custo para cercar o terreno com tela: R$ {p}")