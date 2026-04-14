i=0
maior=0
while i<3:
    v =int(input("Digite um valor "))
    if v > maior:
        maior = v
    i=i+1
print(f'{maior}')