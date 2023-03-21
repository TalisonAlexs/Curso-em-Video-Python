inp = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(inp)}\n"
      f"Só tem espaços? {inp.isspace()}\n"
      f"É um número? {inp.isnumeric()}\n"
      f"É alfabético? {inp.isalpha()}\n"
      f"É alfanumérico? {inp.isalnum()}\n"
      f"Esta em maiúsculas? {inp.isupper()}\n"
      f"Esta em minusculas? {inp.islower()}\n"
      f"Esta capitalizada? {inp.istitle()}")
