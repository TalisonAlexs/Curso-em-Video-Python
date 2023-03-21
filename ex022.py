nome = input("Digite seu nome completo: ").strip()
letras = len(nome) - nome.count(" ")
primeiro_nome = nome.find(" ")
print(
    f"Seu nome em maiúsculas é {nome.upper()}\n"
    f"Seu nome em minusculas é {nome.lower()}\n"
    f"Seu nome tem {letras} letras"
    f"Seu primeiro nome tem {primeiro_nome}"
)
