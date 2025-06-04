import pandas as pd

# Importando o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Criando novo visual:
total_de_outros_filmes_por_lingua = tmdb[tmdb["original_language"] != "en"]["original_language"].value_counts()
print(total_de_outros_filmes_por_lingua.head(5))

# Construir um countplot:
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 8))
sns.countplot(data=tmdb.query("original_language != 'en'"), 
              order=total_de_outros_filmes_por_lingua.index, 
              palette="cubehelix",
              hue="original_language",
              hue_order=total_de_outros_filmes_por_lingua.index, 
              x="original_language")

plt.title("Total de filmes por língua (excluindo inglês)")
plt.xlabel("Língua Original")
plt.ylabel("Total de Filmes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()