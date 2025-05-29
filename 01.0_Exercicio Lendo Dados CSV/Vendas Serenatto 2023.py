import pandas as pd

# Lendo os dados de vendas
vendas = pd.read_csv(r"e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\serenatto_2sem_2023.csv", sep=",", encoding="utf-8")
print(vendas)

# Somatório de todas as vendas de "Ratatouille" do período;
total_vendas_ratatouille = vendas.loc[vendas["produto"] == "Ratatouille", "valor"].sum()
print("Total de vendas de Ratatouille: ", total_vendas_ratatouille)

# Freguencia dos métodos de pagamento para "Ratatouille";
frequencia_pagamento_ratatouille = vendas.loc[vendas["produto"] == "Ratatouille", "metodo_pagamento"].value_counts()
print("Frequência de pagamento de Ratatouille: ", frequencia_pagamento_ratatouille)

# Filtrar dados de uma coluna:
vendas_tiramisu = vendas.query('produto == "Tiramisù"').head()
print(vendas_tiramisu)

# Query para Filtrar dados de mais de uma coluna:
vendas_filtradas = vendas.query('valor > 10 and metodo_pagamento != "Dinheiro"')
print(vendas_filtradas)

# Query com operador @:
produtos = ["Café au lait", "Espresso", "Cappuccino"]
vendas_produtos = vendas.query('produto in @produtos and metodo_pagamento == "PIX"')
print(vendas_produtos)

# Comparar a quantidade de vendas realizadas por cada método de pagamento:
import matplotlib.pyplot as plt

metodos_pagamento = vendas["metodo_pagamento"].value_counts()
metodos_pagamento.plot(kind="bar", title="Métodos de Pagamento")
plt.xlabel("Métodos de Pagamento")
plt.ylabel("Quantidade de Vendas")
plt.show()
