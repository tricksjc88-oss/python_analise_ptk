#Desenvolva um código que o usuário digite 5 valores
# e após digitar, informe se o valor é par ou ímpar.

# Lista para armazenar os números digitados
numeros = []

# Loop para solicitar 5 valores
for i in range(5):
    try:
        # Recebe o valor e converte para inteiro
        valor = int(input(f"Digite o {i+1}º valor inteiro: "))
        numeros.append(valor)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        # Opcional: repetir a iteração se a entrada for inválida
        
print("\n--- Verificação Par ou Ímpar ---")

# Verifica se é par ou ímpar após todos os valores serem inseridos
for valor in numeros:
    if valor % 2 == 0:
        print(f"O valor {valor} é PAR.")
    else:
        print(f"O valor {valor} é ÍMPAR.")