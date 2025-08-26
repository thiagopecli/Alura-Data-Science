# Exibindo os tipos de variáveis:

s1 = 'Alura'
s2 = "Alura"

print(f"O '{s1}' é uma {type(s1)}")
print(f"O '{s2}' é uma {type(s2)}")

# Formatando as strings:

texto = '  Geovana Alessandra diass Sanyos ' # Dados a ser formatado/corrigido

print(texto.upper())    # Converter o texto para Caixa Alta(maiuscula)
print(texto.lower())    # Converter o texto para caixa Baixa(minuscula)
print(texto.strip())    # Remove os caracteres(espaço) do inicio e final do texto
print(texto.title())    # Transforma as primeiras letras de cada palavra em maiuscula
print(texto.replace('diass', 'dias'))     # Substituir apenas o "diass"

texto_corrigido = texto.replace('diass', 'dias').replace('y', 't')    # Substitui o diass e "y"
print(texto_corrigido)

texto = texto.strip().replace('diass', 'dias').replace('y', 't').title() # Formata/corrige na mesma variável "texto": Remove os espaços, corrige os erros, põe as primeiras letras de cada palavra em maiuscula;
print(texto)

texto_formatado_corrigido = texto.strip().replace('diass', 'dias').replace('y', 't').title() # Formata/corrige em uma nova variável: Remove os espaços, corrige os erros, põe as primeiras letras de cada palavra em maiuscula;
print(texto_formatado_corrigido)

