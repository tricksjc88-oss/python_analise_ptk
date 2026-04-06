# Desenvolva um código que leia 3 valores, e ao final mostre qual é o valor maior entre os 3.

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
if n1 > n2 and n1 > n3:
    print(f"{n1} é maior que {n2} e {n3}")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é maior que {n1} e {n3}")
else 
    print(f"{n3} é maior que {n2} e {n1}")