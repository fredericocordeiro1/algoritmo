#Questão 20
# Dados tres valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo
# e, se forem, se e um triangulo escaleno, equilatero ou isosceles, considerando os seguintes conceitos:
# 
# • O comprimento de cada lado de um triangulo e menor do que a soma dos outros dois lados.
# • Chama-se equilatero o triangulo que tem tres lados iguais. 
# • Denominam-se isosceles o triangulo que tem o comprimento de dois lados iguais. 
# • Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.


a = int(input("Insira um valor para o lado a :"))
b = int(input("Insira um valor para o lado b :"))
c = int(input("Insira um valor para o lado c :"))

# T_equilatero = a == b == c
# T_isosceles = a == b != c
# T_escaleno = a != b != c

if a == b == c:
    print("Triangulo Equilatero")

elif a != b != c:
    print("Triangulo Escaleno")
else:
    print("Triangulo Isosceles")