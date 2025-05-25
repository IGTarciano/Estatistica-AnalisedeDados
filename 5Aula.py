# Igor T Gomes
# 20/05/2025
# Modulo 2 - Probabilidade : 5° Aula 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats


# Exemplo 1: probabilidade binominal
# Utilizasse quando cada tentativa tem a mesma probabilidade de sucesso
pb_vencer = 0.7
Total_n = 5
pb_vencer_3 = 3
pb = stats.binom.pmf(3,5,0.7)
print(f'Probabilidade de vencer 3 jogos: {pb:.2f}')

# Exemplo 2:
frequencia = 2
pb_falha = 6
pb_poisson = stats.poisson.pmf(pb_falha,frequencia)
print(f'A probabilidade de nenhuma da erro : {pb_poisson:.3f}')

# Exemplo 3: 
pb_total = 0.6
n = 8
pb2 = 0
for i in range (6,9):
    pb = stats.binom.pmf(i,n,pb_total)
    pb2 += pb
    print(f'Probabilidade de haver pelo menos um brasileiro: {pb2:.4f} e {pb:.4f}')
    
# Exemplo 4:
frequencia2 = 12
pb_falha = 0
for i in range(10,16):
    pb = stats.poisson.pmf(i,frequencia2)
    pb_falha += i

print(f'A probabilidade de haver visitantes nesse horario seria de {pb_falha:.4f}')


# Igor T Gomes
# 2/05/2025
# Modulo 2 - Probabilidade part 2 : 6° Aula

# Distribuição uniforme: deve-se definir :
# sintaxe: uniform(loc=0,loc=)
# rvs(size=x)
# Exemplo:


# Exercicio 1:

a = 5
b = 30
distribuicao_normal = stats.uniform(loc=a,scale=b-a)
prob_espera_10min = distribuicao_normal.cdf(10)
print(f'A probabilidade de esperar menos de 10: {prob_espera_10min:.2f}%')

# Exercicio 2:

Media = 30
Dp = 1.5
dis_unif = stats.uniform(loc=Media,scale=Media-Dp)
prob = 1 - dis_unif.cdf(32)
print(f'A probabilidade da temperatura bater no maximo 32: {prob:.4f}%')

# Exercico :

taxa_cliente = 10
escala_lambd = 1 / taxa_cliente
dis_exp = stats.expon(loc=0,scale=escala_lambd)
#amostra = dis_exp.rvs(size=60)
prob_2 = 1 - dis_exp.cdf(10/60)
print(f'probabilidade :{prob_2}')
