dias = int(input("Dias alugados: "))
km = float(input("Kms rodados: "))
pagamento = 60 * dias + km * 0.15
print(f"Total a pagar: R${pagamento:.2f}")
