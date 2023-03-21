from random import choice

n = int(input("Número de alunos: "))
lista = []
CONT = 0
# for i in range(0, n):
while CONT < n:
    CONT += 1
    nome = input(f"{CONT}° Aluno: ")
    lista.append(nome)
print(choice(lista))
