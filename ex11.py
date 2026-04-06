# Desenvolva um codigo que leia 3 notas e calcule a média entre elas

nota1=float(input("Informe a primeira nota "))
nota2=float(input("Informe a segunda nota "))
nota3=float(input("Informe a terceira nota "))
media=(nota1+nota2+nota3)/3
print(f"A média entre {nota1}, {nota2} e {nota3} é igual a {media}")
if media >= 6:
    print("Aprovado")
else:
    print("Recuperação")