import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Separando dados de filmes en ingles:
total_por_linguas = tmdb['original_language'].value_counts()
total_por_linguas = total_por_linguas.loc["en"]
print("Total de filmes em inglês: ", total_por_linguas)