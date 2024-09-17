print("""\
Especificação      |Código|  Preço|
-----------------------------------
Cachorro Quente    |100   |  1.20 |
Bauru Simples      |101   |  1.30 |
Bauru com Ovo      |102   |  1.50 |
Hamburguer         |103   |  1.20 |
Cheeseburguer      |104   |  1.70 |
Suco               |105   |  2.20 |
Refrigerante       |106   |  1.00 |
-----------------------------------
""")

codigo = int(input("Insira o código :"))
resultCodigo = codigo
quantidade = int(input("Insira a quantidade que você deseja :"))

if resultCodigo == 100 :
    preco = float(1.20) * quantidade
    especificacao = "Cachorro Quente "
elif resultCodigo == 101:
    preco = float(1.30) * quantidade
    especificacao = "Bauru Simples"
elif resultCodigo == 102:
    preco = float(1.50) * quantidade
    especificacao = "Bauru com Ovo"
elif resultCodigo == 103:
    preco = float(1.20) * quantidade
    especificacao = "Hamburguer"
elif resultCodigo == 104:
    preco = float(1.70) * quantidade
    especificacao = "Cheeseburguer"
elif resultCodigo == 105:
    preco = float(2.20) * quantidade
    especificacao = "Suco"
elif resultCodigo == 106:
    preco = float(1.00) * quantidade 
    especificacao = "Refrigerante"
else:
    print("Código do produto inválido!")
print(f"Produto Comprado :{especificacao}\nValor a ser pago :R$ {preco}")