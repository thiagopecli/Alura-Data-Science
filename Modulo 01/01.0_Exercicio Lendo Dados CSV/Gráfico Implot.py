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

# Construindo o gráfico de dispersão com subplots para cada idioma:
sns.lmplot(
    data=fr_es_de_com_revenue_e_budget,
    x="budget",
    y="revenue",
    col="original_language",      # Cria um gráfico para cada idioma
    hue="original_language",      # Cores diferentes para cada idioma
    ci=None,                      # Remove intervalo de confiança
    height=4,                     # Altura de cada subplot
    scatter_kws={"s": 30, "alpha": 0.5}  # Tamanho e transparência dos pontos
)
plt.show()

