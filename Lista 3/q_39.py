print("""--------------------------------
Calculo de area de Triângulo
--------------------------------""")
while True:
    altura = float(input("Insira a altura do Triângulo: "))
    base = float(input("Insira a base do Triângulo: "))

    if altura <= 0:
        print("Erro: A altura deve ser um valor maior que 0. Tente novamente.")
    elif base <= 0:
        print("Erro: A base deve ser um valor maior que 0. Tente novamente.")
    else:
        area = (base * altura) / 2
        print(f"A area do Triangulo é: {area}")
        break