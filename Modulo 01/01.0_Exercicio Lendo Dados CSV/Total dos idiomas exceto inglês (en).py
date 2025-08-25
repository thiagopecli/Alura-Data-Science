import pandas as pd

# Carrega o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv')

# Total dos idiomas exceto inglês:
total_por_lingua = tmdb['original_language'].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
print(f'Total de idiomas exceto inglês: {total_do_resto}')

# Criando um dicionário para armazenar os totais
dados = {
    "lingua": ["ingles", "outros"],
    "total": [total_de_ingles, total_do_resto]
}

dados = pd.DataFrame(dados)
print(dados)

# Criando o gráfico de barras
import matplotlib.pyplot as plt
plt.bar(dados["lingua"], dados["total"], color=["blue", "orange"])
plt.title("Total de Filmes por Idioma")
plt.xlabel("Idioma")
plt.ylabel("Total de Filmes")
plt.show()

# Criando o gráfico de pizza
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    dados["total"],
    labels=dados["lingua"],
    autopct='%1.2f%%',
    startangle=140,
    colors=["green", "orange"]
)

plt.legend(dados["lingua"], title="Idioma")  # Adiciona a legenda
plt.title("Distribuição de Filmes por Idioma")
plt.axis('equal')  # Garante que o gráfico seja um círculo
plt.show()

