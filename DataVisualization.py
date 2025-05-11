# Importação das bibliotecas:
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Lista de Exercícios - Estatística Descritiva; Vizualização de dados:

# Exercicio 01: Gráfico de Linhas - Acompanhamento da Inflação no Recife (2024).

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
ipca_recife_2024 = [0.55, 0.62, 0.48, 0.59, 0.45, 0.38, 0.42, 0.51, 0.60, 0.53, 0.49, 0.57]

Meses = np.array(meses)
Inflacao_rec = np.array(ipca_recife_2024)

plt.plot(Meses,Inflacao_rec, ls='-',color='g')
plt.xlabel('Meses')
plt.ylabel('inflação Recife 2024')
plt.title('Acompanhamento da Inflação no Recife (2024)')
plt.grid()
plt.show()

# Exercico 02: Gráfico de Barras - Comparativo de Casos de Dengue por Bairro (Recife - 2025)

bairros_recife = ['Boa Viagem', 'Imbiribeira', 'Casa Amarela', 'Afogados', 'Boa Vista', 'Madalena']
casos_dengue_2025 = [125, 98, 150, 80, 110, 92]

np.array(bairros_recife)
np.array(casos_dengue_2025)

plt.bar(bairros_recife,casos_dengue_2025,color='g',width=0.2)
plt.xlabel('Bairros do Recife')
plt.ylabel('Casos registrados em 2025')
plt.title('Comparativo de Casos de Dengue por Bairro (Recife - 2025)')
plt.grid()
plt.show()

# Exercicios 03: Gráfico de Dispersão - Relação entre IMC e Pressão Arterial (Amostra em Olinda)

imc_olinda = [22.5, 28.1, 25.3, 30.2, 23.8, 27.5, 26.8, 29.5, 24.1, 31.5]
pressao_sistolica_olinda = [120, 135, 125, 145, 122, 130, 128, 140, 124, 150]

np.array(imc_olinda)
np.array(pressao_sistolica_olinda)

plt.scatter(pressao_sistolica_olinda,imc_olinda,color='r')
plt.xlabel('Pressão arterial: moradores de Olinda')
plt.ylabel('IMC media dos moradores de olinda')
plt.title('Relação entre IMC e Pressão Arterial (Amostra em Olinda)')
plt.grid()
plt.show()

# Exercico 04:  Histograma - Distribuição da Idade dos Participantes do Festival de Inverno de Garanhuns (2024)

idades_festival_garanhuns = [25, 32, 18, 45, 28, 38, 52, 21, 35, 48, 29, 31, 40, 23, 37, 55, 27,
33, 42, 19,30, 46, 26, 39, 50, 22, 36, 49, 24, 34, 41, 20, 33, 47, 28, 36, 51, 29, 32, 43,18, 31, 44,
27, 38, 53, 26, 35, 40, 21, 34, 48, 25, 37, 54, 23, 39, 45, 22, 33, 41, 19, 36, 52, 24, 38, 49, 28,
31, 42, 20, 35, 50, 26, 37, 46, 23, 32, 51, 29]

np.array(idades_festival_garanhuns)

plt.hist(idades_festival_garanhuns)
plt.xlabel('Distribuição das idades festival de Garanhuns 2024')
plt.grid()
plt.title('Histograma - Distribuicao da Idade dos Participantes do Festival de Inverno de Garanhuns (2024)')
plt.show()

# Exercicio 05: Gráfico de Pizza - Distribuição do Eleitorado por Faixa Etária (Recife - Eleições 2026)

faixas_etarias = ['16-24', '25-34', '35-44', '45-59', '60+']
percentual_eleitorado = [22, 28, 20, 18, 12]

np.array(faixas_etarias)
np.array(percentual_eleitorado)

plt.pie(percentual_eleitorado,labels=faixas_etarias,startangle=90) # No eixo X não ler string apenas conteudos numericos
plt.show()

# Exercicio 06: Gráfico de Barras Horizontais - Ranking de Filmes Mais Assistidos no Cinema da Fundação (Recife)

filmes = ['Bacurau', 'Aquarius', 'O Som ao Redor', 'Central do Brasil', 'Tropa de Elite']
espectadores = [450, 380, 520, 600, 410]

np.array(filmes)
np.array(espectadores)

plt.barh(espectadores,filmes,color='g',height=1)
plt.show()

# Exercicio 07: Gráfico de Dispersão com Cores - Relação entre Anos de Estudo e Salário por Escolaridade (Pernambuco)

anos_estudo = [8, 12, 16, 6, 10, 18, 11, 14, 9, 15]
np.array(anos_estudo)
salario = [1500, 2800, 4500, 1200, 2000, 6000, 2200, 3500, 1800, 4000]  
np.array(salario)
escolaridade = ['Fundamental', 'Médio', 'Superior', 'Fundamental', 'Médio', 'Superior', 'Médio',
'Superior', 'Fundamental', 'Superior']
np.array(escolaridade)

plt.scatter(anos_estudo,escolaridade,c=salario)
plt.show()

# Exercicio 08: Histograma Comparativo - Distribuição do Tempo de Espera em Dois Hospitais (Recife)

tempo_espera_hospital_a = np.random.normal(loc=35, scale=10, size=100)
tempo_espera_hospital_b = np.random.normal(loc=28, scale=8, size=100)

plt.hist(tempo_espera_hospital_a,bins=5,alpha=0.5,label=tempo_espera_hospital_a,color='blue',edgecolor='black')
plt.hist(tempo_espera_hospital_b,bins=5,alpha=0.5,label=tempo_espera_hospital_b,color='red',edgecolor='black')

# bins define o número de barras (ou intervalos) do histograma.
# alpha controla a transparência das barras (útil para ver sobreposição).
# label define o rótulo para a legenda.
# color define a cor das barras.
# edgecolor define a cor das bordas das barras.

plt.xlabel('Tempo de espera no hospital A')
plt.ylabel('Tempo de espera no hospital B')
plt.title('Hist comparativo')
plt.grid()
plt.show()