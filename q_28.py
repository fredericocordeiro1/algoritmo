# Questao 28
print("Cálculo de média.")
numero1 = int(input("Insira um valor para X: "))
numero2 = int(input("Insira um valor para Y: "))
numero3 = int(input("Insira um valor para Z: "))

mediaGeometrica = (numero1 * numero2 * numero3) ** (1/3)
print(f"Média Geométrica: {mediaGeometrica:.2f}")

mediaPonderada = ((numero1 * 1) + (numero2 * 2) + (numero3 * 3)) / 6 # 6 é igual a soma do peso de cada numero (1+2+3=6)
print(f"Média Ponderada: {mediaPonderada:.2f}")

mediaHarmonica =(3)/((1/numero1)+(1/numero2)+(1/numero3))
print(f"Média Harmônica: {mediaHarmonica:.2f}")

mediaAritmetica = (numero1+numero2+numero3)/(3)
print(f"Média Aritmética: {mediaAritmetica:.2f}")
