n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
valor_media = float(7.0)

print(f"Resultado da média:", media)
if media >= valor_media:
    print("Aprovado")
else:
    print("Reprovado")