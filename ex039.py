from datetime import date

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano
print(f"Quem nasceu em {ano} tem {idade} em {date.today().year}")
if idade < 18:
    print(
        f"Ainda faltam {18 - idade} anos para o alistamento\n"
        f"Seu alistamento sera em {ano + 18}"
    )
elif idade > 18:
    print(
        f"Você já deveria ter se alistado há {idade - 18} anos\n"
        f"Seu alistamento foi em {ano + 18}"
    )
else:
    print("Você deve se alistar este ano")
