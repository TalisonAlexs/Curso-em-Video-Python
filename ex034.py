salario_inicial = float(input("Digite o salário do funcionário: R$"))
if salario_inicial > 1250:
    salario_final = salario_inicial + salario_inicial * 0.10
else:
    salario_final = salario_inicial + salario_inicial * 0.15
print(f"Quem ganhava R${salario_final:.2f}, passa a ganhar R${salario_final:.2f}")
