
import csv
import random

# Criando uma lista vazia para armazenar os dados
dados_imoveis = []

# Gerando 36 linhas de dados fictícios
for _ in range(36):
    # Gerando preços de imóveis aleatórios entre R$200.000 e R$1.000.000
    preco_imovel = round(random.uniform(200000, 1000000), 0)
    
    # Gerando valores do metro quadrado aleatórios entre R$4.000 e R$8.000
    valor_metro_quadrado = round(random.uniform(4000, 8000), 0)
    
    # Gerando valores do tamanho do metro quadrado aleatorios entre 0 e 400
    tamanho_metro_quadrado = round(random.uniform(50, 400), 0)
    
    
    # Adicionando os dados à lista
    dados_imoveis.append([preco_imovel, valor_metro_quadrado, tamanho_metro_quadrado])

# Nome do arquivo CSV
nome_arquivo = "dados_imoveis.csv"

# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # Escrevendo o cabeçalho
    writer.writerow(["Preço do Imóvel (R$)", "Valor do Metro Quadrado (R$)", "Tamanho do m2"])
    
    # Escrevendo os dados da lista no arquivo CSV
    for dados in dados_imoveis:
        writer.writerow(dados)

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
