km = float(input("Digite a distancia da viagem(km): "))
if km > 200:
    preço = km * 0.45
else:
    preço = km * 0.50
print(f"O preço da passagem é de R${preço:.2f}")
