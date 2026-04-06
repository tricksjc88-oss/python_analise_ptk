#Desenvolva um código que leia um valor e dê um desconto de acordo com a tabela de valores abaixo = >500, desc 20% / 100 a 499 - 15% / <100 - 5%
# Solicita o valor original do produto
valor_original = float(input("Digite o valor do produto: R$ "))
if valor_original >= 500:
    porcentagem = 20
    desconto = valor_original * 0.20
elif valor_original >= 100:
    porcentagem = 15
    desconto = valor_original * 0.15
else:
    porcentagem = 5
    desconto = valor_original * 0.05
valor_final = valor_original - desconto
print(f"Valor original: R$ {valor_original:.2f}")
print(f"Desconto aplicado: {porcentagem}% (R$ {desconto:.2f})")
print(f"Valor final: R$ {valor_final:.2f}")



