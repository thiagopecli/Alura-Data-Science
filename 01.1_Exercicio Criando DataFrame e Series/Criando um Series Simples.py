import pandas as pd

# Criando um Series com dados de notas:

nota = pd.Series([8.0, 7.5, 9.0, 6.5, 8.5], index=["Rafael", "Davi", "Lucas", "Jean", "Rodrigo"])
print(nota.sort_values(ascending=False))
print("A maior nota da turma foi a do: ", nota.idxmax())
print("A menor nota da turma foi a do: ", nota.idxmin())
print("A média da turma é: ", nota.mean())
print("A mediana da turma é: ", nota.median())