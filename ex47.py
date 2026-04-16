def calcular_area_quadrado(lado):
    return lado ** 2

# Correção 1: Adicionado aspas na string do input
valor = int(input("Digite o tamanho do lado: "))

# Correção 2: Passar o argumento 'valor' para a função
resultado = calcular_area_quadrado(valor)

# Correção 3: Adicionado aspas na string do print
print(f"O resultado é {resultado}")

