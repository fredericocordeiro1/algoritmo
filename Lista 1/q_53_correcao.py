print("=================================================================")
print("Calculadora de Custo para Cercar o Terreno com Tela")
print("=================================================================")

# Leitura das dimensões do terreno e do preço por metro
c = float(input("Insira o comprimento do terreno (em metros): "))  # Comprimento
l = float(input("Insira a largura do terreno (em metros): "))     # Largura
p = float(input("Insira o preço do metro de tela (em R$): "))      # Preço por metro

# Calcula o perímetro do terreno
perimetro = 2 * (c + l)

# Calcula o custo total para cercar o terreno
custo_total = perimetro * p

# Exibe o custo total
print("=================================================================")
print(f"Custo para cercar o terreno com tela: R$ {custo_total:.2f}")
