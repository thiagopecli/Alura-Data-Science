import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Separando dados de filmes en ingles:
total_por_lingua = tmdb['original_language'].value_counts()
total_de_ingles = total_por_lingua.loc["en"]
print(total_de_ingles)

# Exibir o tal geral:
total_por_linguas = tmdb["original_language"].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_geral, total_de_ingles, total_do_resto)

# Preparar os dados para o grafico em barras: 
dados = {
    "lingua": ["Inglês", "Outras"],
    "total": [total_de_ingles, total_do_resto]
}   

dados = pd.DataFrame(dados)
print(dados)

# Criar o gráfico de barras:
plt.bar(dados["lingua"], dados["total"], color=["blue", "orange"])
plt.title("Total de Filmes por Idioma")
plt.xlabel("Idioma")
plt.ylabel("Total de Filmes")

# Exibir o gráfico pizza:
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    dados["total"],
    labels=dados["lingua"],
    autopct='%1.2f%%',
    startangle=140,
    colors=["blue", "orange"]
)
# Altera a cor apenas das porcentagens (autotexts)
for autotext in autotexts:
    autotext.set_color('white')

plt.legend(dados["lingua"], title="Idioma")  # Adiciona a legenda

plt.title("Distribuição de Filmes por Idioma")
plt.axis('equal')

plt.show()