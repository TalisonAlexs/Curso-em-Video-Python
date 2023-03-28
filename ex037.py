n = int(input("Digite um número inteiro: "))
escolha = int(
    input(
        "Escolha umas das bases de conversão\n"
        "[1] - Binário\n"
        "[2] - Octal\n"
        "[3] - Hexadecimal\n"
        "Digite a opção: "
    )
)
if escolha == 1:
    print(f"{n} em binário é {bin(n)}")
elif escolha == 2:
    print(f"{n} em octal é {oct(n)}")
elif escolha == 3:
    print(f"{n} em hexadecimal é {hex(n)}")
