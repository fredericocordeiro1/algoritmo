#Questao 47 Lista 3
import sys
print("""----------------------
Menu de Opções:
adicao(opcao 1)
subtracao(opcao 2)
multiplicacao(opcao 3)
divisao(opcao 4)
saida(opcao 5)
----------------------""")

n1 = int(input("Insira um numero :"))
n2 = int(input("Insira mais um numero :"))
opcao = int(input("Digite a opção:"))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
if opcao == 1 :
    result = adicao 
elif opcao == 2:
    result = subtracao
elif opcao == 3:
    result = multiplicacao
elif opcao == 4:
    result = divisao
elif opcao == 5:
    print("Finalizando........")
    sys.exit
else:
    print("""Opção inválida!
Insira uma opção entre 1 e 5:""")
    opcao = int(input("Digite a opção:"))
    
print(f"Resultado do calculo: {result}")