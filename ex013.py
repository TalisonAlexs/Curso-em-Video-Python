salario_i = round(float(input("Digite o salário: R$")), 2)
salario_f = round((salario_i * 0.15) + salario_i, 2)
print(
    f"Um funcionário que ganhava R${salario_i}, com 15% de aumento, passa a ganhar R${salario_f}"
)
