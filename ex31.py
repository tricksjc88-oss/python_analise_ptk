for i in range (0,5):
    x=int(input("Digite um valor "))
    r = x % 2
    if r % 2 == 0:
        input(f'O valor {x} é par')
    else:
        input(f'O valor {x} é impar')