numeroArmz = []

while True:
    nInt = int(input("Insira um número inteiro (ou um número negativo para encerrar): "))
    
    if nInt < 0:
        print("Número negativo digitado, Programa finalizado!")
        break  
    
    numeroArmz.append(nInt)

if numeroArmz:
    maiorNumero = max(numeroArmz)
    menorNumero = min(numeroArmz)
    print(f"Menor número digitado: {menorNumero}\nMaior número digitado: {maiorNumero}")
else:
    print("Não foi possivel mostrar o maior ou o menor número digitado.")
