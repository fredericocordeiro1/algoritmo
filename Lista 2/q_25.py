# Questão 25
import sys

a = int(input("Insira o valor de 'a':"))
if a == 0:
    print("Não é equação do segundo grau!")
    sys.exit()
b = int(input("Insira o valor de 'b':")) 
c = int(input("Insira o valor de 'c':"))

delta = (b**2) - (4*a*c)
print(delta)
raizPositiva = (-(b) + delta ** 0.5)/(2*a)
raizNegativa = (-(b) - delta ** 0.5)/(2*a)


eq2GrauP =(a*raizPositiva**2) + (b*raizPositiva) + c
eq2GrauN =(a*raizNegativa**2) + (b*raizNegativa) + c

if delta < 0:
    print("Não existe raiz.")

elif delta >= 0:
    print(f"Imprima as duas raizes reais :","Raiz Positiva:",raizPositiva,"Raiz Negativa:",raizNegativa)

else:
    print("Raiz única.")