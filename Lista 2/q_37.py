# Questão 37

print("As tarifas do parque são as seguintes: \n1 e 2 hora - R$ 1,00 cada\n3 e 4 hora - R$ 1,40 cada\n5 hora e seguintes - R$ 2,00 cada")

horaEntrada = int(input("Insira o horario da entrada (HORA): "))
minutoEntrada = int(input("Insira o horario da entrada (MINUTO) :"))

horaSaida = int(input("Insira o horario da saida(HORA) :"))
minutoSaida = int(input("Insira o horario da saida(MINUTO) :"))

totalEntrada = horaEntrada * 60 + minutoEntrada
totalSaida = horaSaida * 60 + minutoSaida
totalHora = totalSaida - totalEntrada

if totalHora <= 120:
    print("Valor da Tarifa : R$ 1,00 ")

if totalHora >= 121 or 240:
    print("Valor da Tarifa : R$ 1,40 ")

else:
    print("Valor da tarifa: R$ 2,00 ")
