# Questão 27

idadeNadador = int(input("Informe a idade do nadador: "))

if 5 <= idadeNadador <= 7:
    print("Categoria do nadador: Infantil A")
elif 8 <= idadeNadador <= 10:
    print("Categoria do nadador: Infantil B")
elif 11 <= idadeNadador <= 13:
    print("Categoria do nadador: Juvenil A")
elif 14 <= idadeNadador <= 17:
    print("Categoria do nadador: Juvenil B")
else:
    print("Categoria do nadador: Sênior")