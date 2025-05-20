# Analise do DF temperaturas;13
# Bibliotecas:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o arquivo:
Temperatura_rec = pd.read_csv('temperaturas.csv')

# Medidas de tendencia centrais: 

# Temperatura media:
Df_temperaturas = Temperatura_rec['Temperatura_Media_C']

Media = Df_temperaturas.mean()
print(f'A temperatura media: {Media:.2f} C')
print(60*'-')
# Temperatura mais frequente: 
Moda = Df_temperaturas.mode()
print(f'A temperatura mais frequente foi: {Moda} C')
print(60*'-')
# Analise da mediana:
Mediana = Df_temperaturas.median()
print(f'Na amostra em 50% das datas se manteve em uma temperatura de : {Mediana:.2f} C')
print(60*'-')

# Medidas de dispersão:

# Desvio padrão e Variancia:
Desvio_Padrao = Df_temperaturas.std(ddof=1)
Variancia = Df_temperaturas.var(ddof=1)
print(f'A amostra em questao aprensenta um desvio de {Desvio_Padrao:.2f} e variancia {Variancia:.2f}, isso que dizer que os dados estao proximos a media e que nao estao tao dispersos')
print(60*'-')

# Amplitude:

Amplitude = Df_temperaturas.max()
Amplitude2 = Df_temperaturas.min()
print(f'As temperaturas veriavel em um intervalode {Amplitude-Amplitude2:.2f} C')
print(60*'-')

# Quartis: Q1,Q2 e Q3
Q1 = Df_temperaturas.quantile(0.25)
print(f'Quantil 1: {Q1:.2f}')
print(60*'-')

Q2 = Df_temperaturas.quantile(0.50)
print(f'Quantil 2: {Q2:.2f}')
print(60*'-')

Q3 = Df_temperaturas.quantile(0.75)
print(f'Quantil 3: {Q3:.2f}')
print(60*'-')

# Intervalo inter quartil :
IIQ = Q3-Q1

# Detectando Outliers:

Z_score = (Df_temperaturas-Media)/Desvio_Padrao
for score, temperatura in zip(Z_score,Df_temperaturas):
    if score <= -3 or score >= 3:
        print(f'Z-score: {score:.2f} e Outliers {temperatura:.2f}')
        
print(f'Z-score: {score:.2f} e Outliers {temperatura:.2f}')

