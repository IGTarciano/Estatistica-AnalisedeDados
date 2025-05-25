# Lista de Exercícios - Probabilidade
# Bibliotecas usadas:
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats

# Distribuição de Probabilidade Discreta

# Exercicio 1: Time de volei
pct_vencer = 0.7
n = 5
pb_de_sucesso = 3
pb_TimeVolei = stats.binom.pmf(pb_de_sucesso,n,pct_vencer)
print(f'O time apresenta uma probabilidade de {pb_TimeVolei:.4f} para vencer 3 partidas no campeonato!')
print(60*'-')

# Exercicio 2: Poisson, utilizando quando os eventos ocorrem em um intervalo de tempo ou espaço fixo
Tx_falhaMedia = 0.02
pb_falha = 0
pb_falha_N100 = stats.poisson.pmf(pb_falha,Tx_falhaMedia)
print(f'A empresa apresenta uma taxa de {pb_falha_N100:.4f}%, para as 100 primeiras placas!')
print(60*'-')

# Exercicio 3: Poisson
Tx_media = 3
pb = 5
pb_chegada_5 = stats.poisson.pmf(Tx_media,pb)
print(f'A probabilidade de chegar  jangada nos proximos 15 minutos seria de {pb_chegada_5:.4f}%!')
print(60*'-')

# Exercicio 4: Binominal
Freq_media = 8
pct_brasileiro = 0.6
pb_turistabrasileiro = 0
for i in range(6,9):
    pb_b = stats.binom.pmf(i,Freq_media,pct_brasileiro)
    pb_turistabrasileiro += pb_b
    print(f'Indica-se que a probabilidade de haver brasileiro nao passaria de {pb_b:.4f}%, para cada frequencia {pb_turistabrasileiro:.4f}!')
print(60*'-')

# Exercicio 5: Binominal 
pct_defeitos = 0.05
n_pc = 20
pb_sucesso = 2
pb_defeitos = stats.binom.pmf(pb_de_sucesso,n,pct_defeitos)
print(f'A probabilidade de duas pecas darem defeitos na amostra seria de {pb_defeitos:.4f}%')
print(60*'-')

# Exercicio 6: Poisson
Freq_media_ligacoes = 1.5
pb_frenq_2 = 2
pb_ligacoes = stats.poisson.pmf(pb_frenq_2,Freq_media_ligacoes)
print(f'A chance para haver pelo menos 2 ligacoes na proxima hora e de {pb_ligacoes:.6f}')
print(60*'-')

# Exercicio 7: Binominal

prcnt_acerto = 0.8
n = 3
pb_acerto = 3
pb_acerto2 = stats.binom.pmf(pb_acerto,n,prcnt_acerto)
print(f'A probabilidade de acerta os 3 lances {pb_acerto2:.4f}')
print(60*'-')

# Exercicio 7: Poisson

Frqnc_visitantes = 12
for i  in range(10,16):
    pb_visitantes = stats.poisson.pmf(i,Frqnc_visitantes)
    print(f'A probabilidade dos visitantes no mesmo horario esta entre {i} e de, {pb_visitantes:.4f}%')
print(60*'-')
