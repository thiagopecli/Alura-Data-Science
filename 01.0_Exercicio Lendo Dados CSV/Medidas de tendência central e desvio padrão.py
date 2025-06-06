import pandas as pd

# Lendo os Filmes
filmes = pd.read_csv(r"e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\movies.csv", sep=",", encoding="utf-8")
print(filmes.head(2))

# Lendo as notas:
notas = pd.read_csv(r"e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\ratings.csv", sep=",", encoding="latin1")
print(notas.head(2))

# Calcular a média do filme em específico 1 - Toy Story e 2 - Jumanji:
media_por_filme_toy_story = notas.loc[notas["movieId"] == 1, "rating"]
media_por_filme_jumanji = notas.loc[notas["movieId"] == 2, "rating"]

media_por_filme_toy_story = media_por_filme_toy_story.mean()
media_por_filme_jumanji = media_por_filme_jumanji.mean()

print(media_por_filme_toy_story, media_por_filme_jumanji) 

# Criar o grafico:
import matplotlib.pyplot as plt

# Dados das avaliações
toy_story = notas.loc[notas["movieId"] == 1, "rating"]
jumanji = notas.loc[notas["movieId"] == 2, "rating"]

# Criar o boxplot com patch_artist=True
box = plt.boxplot([toy_story, jumanji], patch_artist=True)

# Definir cores para cada boxplot
cores = ['lightblue', 'lightgreen']
for patch, cor in zip(box['boxes'], cores):
    patch.set_facecolor(cor)

plt.xticks([1, 2], ["Toy Story", "Jumanji"])
plt.ylabel("Avaliação")
plt.title("Avaliação dos filmes")
plt.show()