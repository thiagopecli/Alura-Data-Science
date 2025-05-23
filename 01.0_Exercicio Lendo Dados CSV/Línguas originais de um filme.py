import pandas as pd

# Lendo o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Exibir apenas a coluna 'original_language':
print(tmdb['original_language'])

# Exibir valores únicos da coluna 'original_language':
print(tmdb['original_language'].unique())

# Exibir qual moda da coluna 'original_language':
print(tmdb['original_language'].value_counts())

