# Lista de Exercícios - Estatística Descritiva
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Medidas de tendencia central 

# Exercício 01: Dado o array de pontuações de 10 alunos em um teste:

Notas_Alunos = [75, 82, 90, 68,78, 85, 92, 70, 76, 88]
Notas_Alunos_numpy = np.array(Notas_Alunos)
# A) Media:
Media = np.mean(Notas_Alunos_numpy)
print(f'Media de notas dos alunos: {Media:.2f}')
print(60*'-')

# B) Mediana:
Mediana = np.median(Notas_Alunos_numpy)
print(f'Mediana das notas {Mediana:.2f}')
print(60*'-')

# Exercício 02: Uma empresa registrou o número de unidades vendidas de um produto durante 7 dias:
Und_vendidas = [25, 30, 28, 35, 32, 30, 27]
Und_vendidas_df = pd.Series(Und_vendidas)

# A) Media
Media_2 = Und_vendidas_df.mean()
print(f'Media das vendas: {Media_2:.2f}')
print(60*'-')

# B) Moda
Moda = Und_vendidas_df.mode()
print(f'Moda {Moda}')
print(60*'-')

# Exercício 03: As idades de 15 participantes de um congresso em Porto de Galinhas são:

Idade_Participantes = [28, 35, 42, 28, 30, 35, 45, 28, 32, 38, 40, 35, 28, 31, 36]
Idade_Participantes_arrays = np.array(Idade_Participantes)

# A) Moda utilizando numpy:

Ordem, contagem = np.unique(Idade_Participantes_arrays,return_counts=True)
Moda_2 = Ordem [contagem == np.max(contagem)]
print(f'A idade mais frequente e {Moda_2}')
print(60*'-')

# Exercício 04: As idades de 15 participantes de um congresso em Porto de Galinhas são:

Idades = [28, 35, 42, 28, 30, 35, 45, 28, 32, 38, 40, 35, 28, 31, 36]

# A) Media:
Idade_numpy = np.array(Idades)
Media_idade = np.mean(Idade_numpy)
print(f'A media das idades: {Media_idade:.2f}')
print(60*'-')

# B) Moda:
Idade_pd = pd.Series(Idades)
Moda_idade = Idade_pd.mode()
print(f'A idade mais frequente: {Moda_idade}')
print(60*'-')

# Exercício 05 - Uma pesquisa sobre o número de filhos por família em uma comunidade resultou nos seguintes dados:

Amostra_numero_filhos = [2, 1, 3, 2, 0, 4, 2, 2, 1, 3]

# A) Media :
Amostra_numpy = np.array(Amostra_numero_filhos)
Media_amostra_numpy = np.mean(Amostra_numpy)
print(f'Media do numero de filhos: {Media_amostra_numpy:.2f}')
print(60*'-')

# B) Moda pandas:
Amostra_pd = pd.Series(Amostra_numpy)
Moda_amostra_pd = Amostra_pd.mode()
print(f'Frequentemente tem {Moda_amostra_pd} na amostra')

# Exercício 06 - Os preços (em reais) de um mesmo livro em 5 livrarias diferentes são:

Precos = [45.50, 48.00, 46.20, 47.50, 46.20]

# A) Media:
Precos_numpy = np.array(Precos)
Media_preco  = np.mean(Precos_numpy)
print(f'A Media dos preços são: R$ {Media_preco:.2f}')
print(60*'-')

# B) Mediana : 
Mediana_precos = np.median(Precos_numpy)
print(f'As bibliotecas apresentam um preço de até R$ {Mediana_precos} ')
print(60*'-')

# C) Moda: 
Precos_pd = pd.Series(Precos)
Moda_precos = Precos_pd.mode()
print(f'Frequentemente tem o preço de R$ {Moda_precos}')
print(60*'-')
