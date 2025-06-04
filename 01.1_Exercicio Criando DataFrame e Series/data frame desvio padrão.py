import pandas as pd
import numpy as np

# Criando o Data Frame de exemplo:

dados = np.array([[ 10, 120, 90, 110, 130], [80, 150, 70, 140, 60]])
df = pd.DataFrame(dados, index = ["Semana 1", "Semana 2"],
                  columns = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"])

# Calculando o desvio padrão das visitas por semana:

desvio_padrao_semana1 = df.loc["Semana 1"].std()
desvio_padrao_semana2 = df.loc["Semana 2"].std()

print(df)
print("\nDesvio Padrão da Semana 1:", round(desvio_padrao_semana1, 2))
print("Desvio Padrão da Semana 2:", round(desvio_padrao_semana2, 2))