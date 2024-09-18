# Questão 22

idade = int(input("Insira sua idade :"))
tempoTrab = int(input("Insira quanto tempo você trabalhou :"))

if idade >= 65:
    print(f"Você pode se aposentar, por idade!")

elif tempoTrab >= 30:
    print(f"Voce pode se aposentar, por tempo de trabalho!")

elif idade >= 60 and tempoTrab >= 25:
     print(f"Voce pode se aposentar por idade e por tempo de trabalho!")

else:
    print("Você não pode se aposentar de nenhuma das duas formas.")