import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importando dados:
tmdb = pd.read_csv(r'e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\tmdb_5000_movies.csv') 

# Filtrando os dados para as colunas desejadas:
dados = tmdb[['title', 'original_language', 'budget', 'revenue']]
linguas = ["fr", "es", "de"]

# Mantendo dados com valores de receita e orçamento válidos, e nas linguas desejadas:
fr_es_de_com_revenue_e_budget = dados.query("revenue > 0 and budget > 0 and original_language in @linguas")

# Construindo o gráfico de dispersão mais a reta de regressão linear para cada caso:
sns.lmplot(x='budget', y='revenue', data=fr_es_de_com_revenue_e_budget, hue= 'original_language', height=10, aspect=1.5)
plt.show()

