import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Explorar o gráfico pizza:

contagem_de_lingua = tmdb ['original_language'].value_counts().to_frame().reset_index().rename(columns={'original_language': 'Idioma', 'count': 'Quantidade'})
contagem_de_lingua.plot.pie(y='Quantidade', labels=contagem_de_lingua['Idioma'], autopct='%1.2f%%', figsize=(10, 10))
plt.title('Distribuição das Línguas Originais dos Filmes')
plt.ylabel('')
plt.show()