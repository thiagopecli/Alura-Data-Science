import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importando e lendo arquivo CSV:
notas = pd.read_csv(r"e:\Documentos\FACULDADE\Alura---Data-Science\01.0_Exercicio Lendo Dados CSV\ratings.csv", sep=",", encoding="latin1")

# Alterando os nomes das colunas para português:
notas.columns = ["Usuário", "Filme", "Nota", "Momento"]

# Exibir quais foram as notas possíveis
print(notas["Nota"].unique())

# Exibir os dados unicos da coluna "Nota":
print(notas["Nota"].value_counts())

# Exibir a média e a mediana das notas:
print("A média das notas é: ", notas["Nota"].mean())
print("A mediana das notas é: ", notas["Nota"].median())

# Para descrever os dados das notas dos usuários:
print(notas["Nota"].describe())

# Exibir histograma das notas:
notas["Nota"].hist(bins=10, color="blue", alpha=0.7)
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.title("Histograma das Notas")
plt.show()

# Exibir boxplot das notas:
notas.boxplot(column="Nota", color="blue", vert=False)
plt.xlabel("Nota")
plt.title("Boxplot das Notas")
plt.show()

print(notas)