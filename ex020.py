from random import shuffle
n = int(input("Número de alunos: "))
lista = []
for i in range(0, n):
    nome = input(("Nome do aluno: "))
    lista.append(nome)
shuffle(lista)
print(f"A ordem de apresentação será {lista}")
