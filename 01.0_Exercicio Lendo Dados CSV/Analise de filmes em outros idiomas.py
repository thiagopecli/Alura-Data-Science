import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados:
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Analise de filmes em outros idiomas:
tmdb.query('original_language != "en"')
print(tmdb.query('original_language != "en"'))

# Contagem dos filmes por lingua:
total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en'")['original_language'].value_counts()
print(total_de_outros_filmes_por_lingua)

# Plotagem do grafico:
sns = total_de_outros_filmes_por_lingua.plot(kind='bar', figsize=(10, 5), color='blue')
plt.title('Total de Filmes por Língua (Excluindo Inglês)')
plt.xlabel('Língua')
plt.ylabel('Total de Filmes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
