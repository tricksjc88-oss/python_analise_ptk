sl_bruto = float(input("Qual o seu salário?: R$ "))
if sl_bruto >= 5000 and sl_bruto <= 8000: 
    porcentagem = 7,5
    desconto = sl_bruto * 0.075
elif sl_bruto <= 5000:
    porcentagem = 0
    desconto = sl_bruto * 0.00
else:
    porcentagem = 27,5
    desconto = sl_bruto * 0.275
valor_final = sl_bruto - desconto
print(f"Salário bruto: R$ {sl_bruto:.2f}")
print(f"IRRF: {porcentagem}% (R$ {desconto:.2f})")
print(f"Salário líquido: R$ {valor_final:.2f}")



