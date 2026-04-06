mes = input("Digite o nome do mês: ").lower()
if mes in ["dezembro", "janeiro","fevereiro"]:
    print("verão")
elif mes in ["março", "abril", "maio"]:
    print("outono")
elif mes in ["junho", "julho","agosto"]:
    print("inverno")
elif mes in ["setembro","outubro","novembro"]:
    print("primavera")
else:
    print("Mês inválido")