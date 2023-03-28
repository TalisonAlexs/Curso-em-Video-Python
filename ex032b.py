from calendar import isleap
from datetime import date

ano = int(input("Que ano quer analisar? Digite 0 para o ano atual: "))
if ano == 0:
    ano = date.today().year
if isleap(ano) is True:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")
