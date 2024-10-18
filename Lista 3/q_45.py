print("""-------------------------------
1- Converte de KM/s para M/s
2- Converte de M/s para KM/s
3- Finaliza o programa
-------------------------------""")
km = 0
m = 0
while True:
        
        opcao = int(input("Insira uma das opções: "))
        
        if opcao == 1:
            km = float(input("Insira sua velocidade em Quilometro: "))
            ms = km * 1000
            print(f"Sua velocidade em Metro/s é de: {ms} M/s")
        elif opcao == 2:
            m = float(input("Insira sua velocidade em Metro: "))
            kms = m / 1000
            print(f"Sua velocidade em Kilometro/s é de: {kms} KM/s")
        elif opcao == 3:
            print("Programa finalizado!")
            break
        else:
            print("Erro: Opção inválida. Tente novamente.")
        