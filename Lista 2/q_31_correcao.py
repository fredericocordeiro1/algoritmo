# Recebe a altura e o peso da pessoa
altura = float(input("Digite a altura da pessoa (em metros): "))
peso = float(input("Digite o peso da pessoa (em kg): "))

# Classificação baseada na altura e peso
if altura < 1.20:
    if peso <= 60:
        classificacao = 'A'
    elif peso <= 90:
        classificacao = 'D'
    else:
        classificacao = 'G'
elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        classificacao = 'B'
    elif peso <= 90:
        classificacao = 'E'
    else:
        classificacao = 'H'
else:  # altura > 1.70
    if peso <= 60:
        classificacao = 'C'
    elif peso <= 90:
        classificacao = 'F'
    else:
        classificacao = 'I'

# Mostra a classificação
print(f"A classificação da pessoa é: {classificacao}")
