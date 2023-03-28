preco_inicial = float(input("Preço das compras: R$"))
pagamento = int(
    input(
        "FORMAS DE PAGAMENTO\n"
        "[1] à vista em dinheiro\n"
        "[2] à vista no cartão\n"
        "[3] 2x no cartão\n"
        "[4] 3x ou mais no cartão\n"
        "Digite a opção: "
    )
)
if pagamento == 1:
    preco_final = preco_inicial - preco_inicial * 0.1
elif pagamento == 2:
    preco_final = preco_inicial - preco_inicial * 0.05
elif pagamento == 3:
    preco_final = preco_inicial
    print(f"Sua compra sera parcelada em 2x de R${preco_final/2:.2f} sem juros")
elif pagamento == 4:
    preco_final = preco_inicial + preco_inicial * 0.2
    parcelas = int(input("Quantidade de parcelas: "))
    print(
        f"Sua compra sera parcelada em {parcelas}x de R${preco_final/parcelas:.2f} com juros"
    )
else:
    preco_final = preco_inicial
    print("Opção invalida. Tente novamente.")
print(f"Sua compra de R${preco_inicial:.2f} vai custar R${preco_final:.2f}")
