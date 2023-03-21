frase = input("Digite uma frase: ").strip().upper()
frase = frase.replace("á", "a")
frase = frase.replace("à", "a")
quantidade = frase.count("A")
primeira = frase.find("A") + 1
ultima = frase.rfind("A") + 1
print(
    f"A Letra 'A' aparece {quantidade} vezes na frase\n"
    f"A primeira letra 'A' aparece na posição {primeira}\n"
    f"A ultima letra 'A' aparece na posição {ultima}"
)
