casa = float(input("Valor da casa: R$"))
salario = float(input("Salario do comprador: R$"))
anos = int(input("Anos de financiamento: "))
prestação = casa / (anos * 12)
print(f"Prestação de R${prestação:.2f}")
if prestação > salario * 0.3:
    print("Empréstimo negado")
else:
    print("Empréstimo concedido")
