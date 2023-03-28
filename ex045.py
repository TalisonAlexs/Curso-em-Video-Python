from random import randint

player = int(input("[0] Pedra\n"
                   "[1] Papel\n"
                   "[2] Tesoura\n"
                   "Digite sua opção: "))
cpu = randint(0, 2)
lista = ["Pedra", "Papel", "Tesoura"]
if 0 <= player <= 2:
    print(f"Jogador jogou {lista[player]}\n"
          f"Computador jogou {lista[cpu]}")
    if player == cpu:
        print("Empate")
    elif (
        player == 0 and cpu == 1 or player == 1 and cpu == 2 or player == 2 and cpu == 0
    ):
        print("Computador venceu")
    else:
        print("Jogador venceu")
else:
    print("Erro. Tente novamente.")
