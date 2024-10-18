idades = []

while True:
    idade = int(input("Insira a idade de uma pessoa: "))
    if idade == 0:
        # Verifica se pelo menos uma idade foi inserida antes de calcular a média
        if len(idades) > 0:
            media = sum(idades) / len(idades)
            print(f"A média das idades é: {media:.2f}")
        else:
            print("Nenhuma idade válida foi inserida.")
        break  # Encerra o loop ao digitar 0
    
    if idade > 0:
        idades.append(idade)  # Só adiciona idades válidas (maiores que 0)