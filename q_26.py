#Questão 26
metro = 1

kilometro = float(input("Insira quantos QUILOMETROS voce percorreu :"))
litro = float(input("Insira quantos LITROS você colocou de gasolina :"))

consumo = kilometro / litro
print(f"Seu carro faz {consumo:.2f} quilometros Por litro.")

if consumo < 8:
    print("Venda seu carro!")
elif 8 <= consumo <= 14:
    print("Econômico!")
elif consumo > 12:
    print("Super Econômico!")

