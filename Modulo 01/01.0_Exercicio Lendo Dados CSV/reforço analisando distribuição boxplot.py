import pandas as pd

# Carregando os dados e exibindo ass primeiras 3 linhas:
filmes = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\movies.csv')
print(filmes.head(3))

notas = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\ratings.csv')
print(notas.head(3))

# Extraindo as notas dos dois filmes em variáveis distintas:
notas_do_toy_story = notas.query('movieId == 1')
notas_do_jumanji = notas.query('movieId == 2')

media_do_toy_story = notas_do_toy_story["rating"].mean()
media_do_jumanji = notas_do_jumanji["rating"].mean()
print(media_do_toy_story, media_do_jumanji)

# Exibindo a mediana: 

notas_do_toy_story = notas.query('movieId == 1')
notas_do_jumanji = notas.query('movieId == 2')

mediana_do_toy_story = notas_do_toy_story['rating'].median()
mediana_do_jumanji = notas_do_jumanji['rating'].median()
print(mediana_do_toy_story, mediana_do_jumanji)
