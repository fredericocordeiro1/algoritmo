import random

# Inicializa o contador de acertos
acertos = 0

# Gera e apresenta 5 perguntas
for i in range(5):
    # Gera dois números aleatórios entre 1 e 99
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    
    # Calcula a resposta correta
    resposta_certa = a + b
    
    # Mostra a pergunta ao usuário e pede a resposta
    print(f"Pergunta {i + 1}: Qual é a soma de {a} + {b}?")
    resposta_usuario = int(input("Sua resposta: "))
    
    # Verifica se a resposta do usuário está correta
    if resposta_usuario == resposta_certa:
        print("Resposta correta!")
        acertos += 1
    else:
        print(f"Resposta incorreta. A resposta correta é {resposta_certa}.")

# Mostra o resumo das acertos
print(f"\nVocê acertou {acertos} de 5 perguntas.")