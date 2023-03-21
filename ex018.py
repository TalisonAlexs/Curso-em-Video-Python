from math import sin, cos, tan, radians
angulo = float(input("Digite um ângulo: "))
print(f"Seno de {angulo} = {sin(radians(angulo)):.2f}\n"
      f"Cosseno de {angulo} = {cos(radians(angulo)):.2f}\n"
      f"Tangente de {angulo} = {tan(radians(angulo)):.2f}")
