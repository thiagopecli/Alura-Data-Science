import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um DataFrame com dados fictícios
filme1 = [2.5, 3.0, 4.0, 5.0, 2.0]
filme2 = [3.5, 4.0, 2.0, 4.5, 3.0]

# mostraremoss na tela as médias e as medianas das notas de ambos os filme ficticios:
media_filme1 = np.mean(filme1)
mediana_filme1 = np.median(filme1)

media_filme2 = np.mean(filme2) 
mediana_filme2 = np.median(filme2)

print(f"Média do Filme 1: {media_filme1}, Mediana do Filme 1: {mediana_filme1}")
print(f"Média do Filme 2: {media_filme2}, Mediana do Filme 2: {mediana_filme2}")

# Exibir histogramas dos dois filmes no mesmo gráfico
plt.figure(figsize=(8, 4))
plt.hist(filme1, bins=5, alpha=0.7, label='Filme 1', color='blue')
plt.hist(filme2, bins=5, alpha=0.7, label='Filme 2', color='green')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.title('Histograma das notas dos dois filmes')
plt.legend()
plt.show()

# Exibir boxplots dos dois filmes
plt.figure(figsize=(6, 4))
plt.boxplot([filme1, filme2], patch_artist=True, labels=['Filme 1', 'Filme 2'])
plt.ylabel('Nota')
plt.title('Boxplot das notas dos dois filmes')
plt.show()

