#Questão 21

n1 = (input("Insira um numero :"))
n2 = (input("Insira outro número :"))
print("1- Soma de 2 números.\n2- Diferença entre 2números (maior pelo menor).\n3- Produto entre 2 números.\n4- Divisão entre 2 números (o denominador não pode ser zero)")

opcao = int(input(f"Insira a opção que voce escolheu :"))


if opcao == 1:
    soma = n1 + n2
    print(f"Resultado da (SOMA) :",soma)

elif opcao == 2:
    subtracao = n1 - n2
    print(f"Resultado da (DIFERENÇA) :",subtracao)

elif opcao == 3:
    multiplicacao = n1 * n2
    print(f"Resultado do (PRODUTO) :",multiplicacao)

elif opcao == 4:
    divisao = n1 / n2
    print("Resultado da (DIVISÃO) :",divisao)

else:
    print("Opção inválida!!",)
