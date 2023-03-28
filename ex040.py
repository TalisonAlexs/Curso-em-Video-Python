n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
if media >= 7:
    MSG = "aprovado"
elif 7 > media >= 5:
    MSG = "em recuperação"
else:
    MSG = "reprovado"
print(f"Média: {media}\n"
      f"Aluno {MSG}")
