import pandas as pd

# Criando um DataFrame simples:
# Criando um DataFrame com colunas específicas: 

dados = {"nome":["Rafael", "Davi", "Lucas", "Jean", "Rodrigo"],
         "idade": [32, 22, 29, 28, 27],
            "altura": [1.80, 1.75, 1.85, 1.78, 1.82]}
df = pd.DataFrame(dados, columns=["nome", "idade", "altura"])
print(df.info())