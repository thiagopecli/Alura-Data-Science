import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

#Contagem dos valores e indices:
tmdb['original_language'].value_counts().index
print(tmdb['original_language'].value_counts().index)

tmdb['original_language'].value_counts().values
print(tmdb['original_language'].value_counts().values)

# Transformando em um dataframe: 
contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_language', 'total']
print(contagem_de_lingua)

# Plotar grafico com seaborn:
import seaborn as sns
plt.figure(figsize=(12, 6))
sns.barplot(
    data=contagem_de_lingua,
    x='original_language',
    y='total',
    hue='original_language',    # Adiciona o hue
    palette='viridis',
    legend=False                # Remove a legenda duplicada
)
plt.title('Total de Filmes por Idioma')
plt.xlabel('Idioma Original')
plt.ylabel('Total de Filmes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()