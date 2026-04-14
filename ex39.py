# Solicita o número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

contador = 1

# Loop while para gerar a tabuada de 1 a 10
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1 # Incrementa o contador

