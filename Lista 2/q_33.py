
produto = float(input("Insira o valor antigo do produto em (R$) :"))
precoAntigo = produto

if produto <= 50:
    percentual_aumento = 5
    aumento = precoAntigo * (percentual_aumento / 100)
elif produto <= 100:
    percentual_aumento = 10
    aumento = precoAntigo * (percentual_aumento / 100)
else:
    percentual_aumento = 15
    aumento = precoAntigo * (percentual_aumento / 100)
precoNovo = precoAntigo + aumento

print(f"Valor novo:R${precoNovo:.2f}\nPercentual de aumento aplicado {percentual_aumento}%: R$ {aumento:.2f}") 
