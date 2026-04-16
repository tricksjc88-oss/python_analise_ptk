#Crie uma função que receba dois números e retorne o maior deles. 
def encontrar_maior(a, b):
    if a > b:
        return a
    else:

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Chamando a função e exibindo o resultado
resultado = encontrar_maior(num1, num2)
print(f"O maior número é: {resultado}")