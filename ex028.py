from random import randint

player = int(input("Tente adivinhar o número entre 0 e 5: "))
cpu = randint(0, 5)
if player == cpu:
    print("Voce acertou")
else:
    print(f"Voce errou. Eu pensei no número {cpu}")
