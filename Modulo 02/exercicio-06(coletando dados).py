# Coletando Dados(Strings):

nome = input("\nEscreva seu nome: ")
print(nome)

ano_entrada_string = input('\nEscreva o ano de ingresso do estudante: ')
print(f"O ano '{ano_entrada_string}' foi escrito em um formato {type(ano_entrada_string)}.\n")

# Coletando Dados(Inteiro):

ano_entrada_int = int(input('\nEscreva o ano de ingresso do estudante: '))
print(f"O ano '{ano_entrada_int}' foi escrito em um formato {type(ano_entrada_int)}.\n")

# Coletando Dados(Float):

nota_entrada_float = float(input('\nDigite a nota do teste de ingresso: '))
print(f"O ano de entrada {ano_entrada_int} - nota do teste de ingresso {nota_entrada_float}.\n")