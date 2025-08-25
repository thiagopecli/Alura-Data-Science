# Tabela com cargos, salarios e quantidade de funcionários por cargo:

quantidade_seguranca = 5
salario_seguranca = 3000

quantidade_docente = 16
salario_docente = 6000

quantidade_diretor = 1
salario_diretor = 12500

# 1. Somar a quantidade de funcionários:

quantidade_funcionarios = quantidade_seguranca + quantidade_docente + quantidade_diretor
print(quantidade_funcionarios)

# 2. Calcular a diferença entre o salario mais baixo e mais alto:

diferença_salarial_maior_menor = salario_diretor - salario_seguranca
print(diferença_salarial_maior_menor)

# 3. Média ponderada da faixa salarial da escola: 

media_salarial_escola = (quantidade_seguranca*salario_seguranca + quantidade_docente*salario_docente + quantidade_diretor*salario_diretor) / (quantidade_funcionarios)
print(f"{media_salarial_escola:.2f}")