from datetime import date

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano
if idade <= 9:
    CATEGORIA = "Mirim"
elif idade <= 14:
    CATEGORIA = "Infantil"
elif idade <= 19:
    CATEGORIA = "Junior"
elif idade <= 25:
    CATEGORIA = "Sênior"
else:
    CATEGORIA = "Master"
print(f"O atleta tem {idade} anos\n"
      f"Classificação: {CATEGORIA}")
