import pandas as pd

# Lendo o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Exibir apenas a coluna 'original_language':
print(tmdb['original_language'])

# Exibir valores únicos da coluna 'original_language':
print(tmdb['original_language'].unique())

# Exibir qual moda da coluna 'original_language':
print(tmdb['original_language'].value_counts())

# Exibir os indices dos filmes:
print(tmdb['original_language'].value_counts().index)

# Exibir os valores da moda:
print(tmdb['original_language'].value_counts().values)

# Transformar em dataframe:
print(tmdb['original_language'].value_counts().to_frame())

# Correção de nomes e índices:
print(tmdb['original_language'].value_counts().to_frame().reset_index())

# Renomear as Colunas:
print(tmdb['original_language'].value_counts().to_frame().reset_index().rename(columns={'original_language': 'Idioma', 'count': 'Quantidade'}))

# Visualizar no gráfico:
import matplotlib.pyplot as plt
tmdb['original_language'].value_counts().to_frame().reset_index().rename(columns={'original_language': 'Idioma', 'count': 'Quantidade'}).plot(x='Idioma', y='Quantidade', kind='bar')
plt.title('Línguas Originais dos Filmes')
plt.xlabel('Idioma')
plt.ylabel('Quantidade')
plt.show()
