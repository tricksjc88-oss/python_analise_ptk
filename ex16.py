# Desenvolva um código que leia 3 valores, e ao final mostre qual é o valor maior entre os 3.

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f"O maior valor é: {maior}")