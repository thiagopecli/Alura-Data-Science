import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV:
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv', sep=',', encoding='utf-8')
print(tmdb.head())  # Exibe as primeiras linhas do DataFrame
print(tmdb.info())  # Exibe informações gerais do DataFrame
print(tmdb.describe())  # Exibe estatísticas descritivas do DataFrame
print(tmdb['original_language'].unique())  # Exibe os idiomas únicos
print(tmdb['original_language'].value_counts())  # Exibe a contagem de idiomas originais

# Verificar dados da receita (revenue), valor acima de 0:
tmdb_receita = tmdb[tmdb['revenue'] > 0]
plt.figure()  # Cria uma nova janela de figura
plt.hist(tmdb_receita['revenue'], bins=50, color='blue', edgecolor='black')
plt.title('Distribuição da Receita dos Filmes')

# Verificar a distribuição do orçamento (budget), valor acima de 0:
tmdb_orcamento = tmdb[tmdb['budget'] > 0]
plt.figure()  # Cria outra janela de figura
plt.hist(tmdb_orcamento['budget'], bins=50, color='green', edgecolor='black')
plt.title('Distribuição do Orçamento dos Filmes')

# Verificar a distribuição da média das notas tmdb (vote_average) em que o numero de votos (vote_count) é maior que 10:
tmdb_media_notas = tmdb[(tmdb['vote_average'] > 0) & (tmdb['vote_count'] > 10)]
plt.figure()  # Cria mais uma janela de figura
plt.hist(tmdb_media_notas['vote_average'], bins=50, color='red', edgecolor='black')
plt.title('Distribuição da Média das Notas dos Filmes')

# Exibir todas as figuras abertas
plt.show()
