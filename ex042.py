r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        TIPO = "equilátero"
    elif r1 != r2 != r3 != r1:
        TIPO = "escaleno"
    else:
        TIPO = "isósceles"
    print(f"Os segmentos podem formar um triângulo {TIPO}")
else:
    print("Os segmentos não podem formar um triângulo")
