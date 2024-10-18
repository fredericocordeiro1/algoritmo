while True:
    r1 = float(input("Insira o valor da resistência do RESISTOR 1 (ou 0 para sair): "))
    if r1 == 0:
        print("Programa encerrado.")
        break

    r2 = float(input("Insira o valor da resistência do RESISTOR 2 (ou 0 para sair): "))
    if r2 == 0:
        print("Programa encerrado.")
        break

    # Calcular a resistência equivalente
    resistencia = (r1 * r2) / (r1 + r2)
    print(f"A resistência equivalente dos dois resistores é: {resistencia}")
