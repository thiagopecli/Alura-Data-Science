import pandas as pd

# Lendo os dados CSV
movies = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\movies.csv')
print(movies.head(10))