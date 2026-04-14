while True:
    # Solicita a entrada do usuário
    nome = input("Digite um nome (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário quer parar
    if nome.lower() == 'sair':
        print("Programa encerrado.")
        break  # Sai do loop while
    
    # Imprime o nome digitado
    print(f"Nome digitado: {nome}")