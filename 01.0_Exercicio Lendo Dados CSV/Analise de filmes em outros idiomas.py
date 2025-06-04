import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados:
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Contagem dos filmes por lingua (exceto inglês):
total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en'")['original_language'].value_counts().reset_index()
total_de_outros_filmes_por_lingua.columns = ['lingua', 'total']

# Calcular a porcentagem de filmes por idioma
total = total_de_outros_filmes_por_lingua['total'].sum()
total_de_outros_filmes_por_lingua['porcentagem'] = (total_de_outros_filmes_por_lingua['total'] / total) * 100

plt.figure(figsize=(16, 8))
sns.barplot(
    data=total_de_outros_filmes_por_lingua,
    x='lingua',
    y='porcentagem',
    hue='lingua',
    palette='mako',
    legend=False
)
plt.title('Porcentagem de Filmes por Língua (Excluindo Inglês)')
plt.xlabel('Língua')
plt.ylabel('Porcentagem de Filmes (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
