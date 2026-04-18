import pandas as pd

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salários': [1000,2000,3000,4000]
}

dados_bi = pd.DataFrame(dados)
#print (dados_bi)
print (dados_bi.head(2))

dados_bi. to_csv('meus_dados.csv', index=False, sep=';', encoding ='utf-8')

print("Arquivo exportado com sucesso!")