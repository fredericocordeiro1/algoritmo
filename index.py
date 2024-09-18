#Teste

salario = float(input("Insira o valor do seu sálario: "))
emprestimo = float(input("Insira o valor da prestação do seu empréstimo: "))

if emprestimo * 0.2 > salario:
    print("Emprestimo concedido!")
else:
    print("Emprestimo nao concedido!")
