import pandas as pd

# Lendo os Filmes
filmes = pd.read_csv(r"e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\movies.csv", sep=",", encoding="utf-8")

# Alterando os nomes das colunas para português:
filmes.columns = ["filmeId", "filme", "gênero"]
print(filmes.head())

# Exibir os dados notas:
notas = pd.read_csv(r"e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\ratings.csv", sep=",", encoding="latin1")
notas.columns = ["usuárioId", "filmeId", "nota", "momento"]
notas.head()
print(notas.head())

# Calcular a média do filme em especifico 1 - Toy Story:
media_por_filme = notas.loc[notas["filmeId"] == 1, "nota"].mean()
print("A média do filme é: ", media_por_filme)

# Calcular a média de notas dos filmes:
media_nota = notas.groupby("filmeId")["nota"].mean().reset_index()
media_nota.columns = ["filmeId", "media_nota"]
print(media_nota.head())

# Produzindo Graficos:
import matplotlib.pyplot as plt
import seaborn as sns

media_nota["media_nota"].plot(kind="hist", bins=10, color="blue", alpha=0.7)
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.title("Histograma das Notas")
plt.show()

# Exibir boxplot das notas:
notas.boxplot(column="nota", color="blue", vert=False)
plt.xlabel("Nota")
plt.title("Boxplot das Notas")
plt.show()

print(notas)