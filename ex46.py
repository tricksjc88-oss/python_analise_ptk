def verificar_par_ou_impar(numero):
    """
    Função que recebe um número e verifica se é par ou ímpar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# --- Fluxo principal ---
try:
    # Solicita um número ao usuário
    entrada = int(input("Digite um número inteiro: "))
    
    # Chama a função e armazena o resultado
    resultado = verificar_par_ou_impar(entrada)
    
    # Exibe o resultado
    print(f"O número {entrada} é {resultado}.")

except ValueError:
    print("Por favor, digite um número inteiro válido.")