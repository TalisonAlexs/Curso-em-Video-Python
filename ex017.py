from math import hypot

CatetoO = float(input("Comprimento do cateto oposto: "))
CatetoA = float(input("Comprimento do cateto adjacente: "))
Hipotenusa = hypot(CatetoO, CatetoA)
print(f"A hipotenusa mede {Hipotenusa:.2f}")
