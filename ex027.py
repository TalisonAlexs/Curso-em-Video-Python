nome = input("Digite seu nome completo: ").strip().title().split()
ultimo = list(reversed(nome))
print(f"Seu primeiro nome é {nome[0]}\n"
      f"Seu ultimo nome é {ultimo[0]}")
# print(f"Seu ultimo nome é {nome[len(nome) - 1]}")
