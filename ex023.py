n = int(input("Digite um número inteiro de 0 a 9999: "))
unidade = n % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print(
    f"Unidade = {unidade}\n"
    f"Dezena = {dezena}\n"
    f"Centena = {centena}\n"
    f"Milhar = {milhar}"
)
