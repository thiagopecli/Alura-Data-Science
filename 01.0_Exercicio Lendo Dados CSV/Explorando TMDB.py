import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv', sep=',', encoding='utf-8')
tmdb.info()
print(tmdb.describe())
print(tmdb.head())

# Gerar Histograma Distribuição de Orçamento:
sns.displot(tmdb['budget'], bins=10, kde=True, color='blue', alpha=0.7)
plt.title('Distribuição de Orçamento')
plt.show()

# Gerar Histograma Distribuição de Receita:
sns.displot(tmdb['revenue'], bins=10, kde=True, color='blue', alpha=0.7)
plt.title('Distribuição de Receita')
plt.show()

# Gerar Histograma de Faturamento acima de 0:
com_faturamento = tmdb[tmdb['revenue'] > 0]
sns.displot(com_faturamento['revenue'], bins=10, kde=True, color='green', alpha=0.7)
plt.title('Distribuição de Receita')
plt.show()