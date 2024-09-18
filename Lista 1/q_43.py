#Questão 43
total = float(input("Insira o valor total EM REAIS :"))

desconto = total * 0.9
valorParcela = total / 3
comissaoAvista = 0.05 * desconto
comissaoParcelado = 0.05 * total

print(f"Desconto de 10%: R$ {desconto}")
print(f"Valor da parcela em até 3x sem juros: R$ {valorParcela:.2f}")
print(f"Valor da comissão do VENDEDOR quando a venda for AVISTA: R$ {comissaoAvista:.2f}")
print(f"Valor da comissão do VENDEDOR quando a venda for PARCELADA: R$ {comissaoParcelado:.2f}")