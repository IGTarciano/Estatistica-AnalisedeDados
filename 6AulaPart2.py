# Igor T Gomes
# 29/05/2025
# Modulo 2 - Estatistica Inferencial : 6° Aula 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.proportion import proportion_confint
# Estatística - Estimativa de proporções populacionais

# Exercicio 17: 

n = 150
tx_suc = 90
 
# a) 
Est_pontual = (tx_suc/n)*100
print(f'Exercicio 17. a): Estimativa pontual:{Est_pontual}')

# b)
try:
    limite_inf, limite_sup = proportion_confint(count=tx_suc,nobs=n,alpha=1-0.95)
    print(f'Exercicio 17. b): Intervalo de confianca. Limite inferior {limite_inf*100:.2f}% | Limite superior {limite_sup*100:.2f}%')
    print(f'Exericio 17. c): Sim , ten-se 15% de confiança nos dados ')
except TypeError as e:
    print('Verificar conteudo!')
    
# Exercicio 16:

try:
    n = 1000
    tx_suc = 25
    IC = 0.90
    limite_sup, limite_inf = proportion_confint(count=tx_suc,nobs=n,alpha=1-0.90)
    print(f'Exercicio 16: Intervalo de confianca. Limite inferior {limite_inf*100:.2f}% | Limite superior {limite_sup*100:.2f}%')
except ValueError: 
    print('Erro encontrado!')
    
# Teste de hipotese:

# função descritiva acumulada: stats.norm.cdf(zvalue)

# Exercicio 19: 

media = 1500
dp = 120
n = 45
media_amostral = 1560
se = 0.01
# Media ; H0 = 1500
# H1 > 1500

try:
    ErroPdr = dp/np.sqrt(n)
    z = stats.norm.ppf(1-se)
    vlr_critico = 1500 + z*ErroPdr
    if vlr_critico < media_amostral:
        print(f'H0 rejeitado')
    else: print(f'H0 aceito')
except TypeError:
    print('Tente novamente')
    
# Exercicio 20:

try:
    Media = 20
    n = 15
    media_amostral = 23
    dp = 6
    se = 0.05
    grau_linberdade = n - 1
    ErroPdr = dp/np.sqrt(n)
    z = stats.norm.ppf(1-se,grau_linberdade)
    vlr_critico = Media + z*ErroPdr
except TypeError:
    print('Tente novamente ')

