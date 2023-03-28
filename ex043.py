peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura**2
print(f"Seu IMC é de {imc:.1f}")
if imc < 18.5:
    MSG = "abaixo do peso"
elif 18.5 <= imc < 25:
    MSG = "com peso ideal"
elif 25 <= imc < 30:
    MSG = "com sobrepeso"
elif 30 <= imc < 40:
    MSG = " com obesidade"
else:
    MSG = "com obesidade mórbida"
print(f"Você esta {MSG}")
