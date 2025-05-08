# Exercícios de Fixação de comandos Pandas e numpy

import numpy as np
import pandas as pd

# Exercício 01 - Medidas de Dispersão
Dados = np.array([2, 0, 1, 3, 2, 2, 0, 1, 2, 4])# criando a estrutura de dados principal

# a) Calcule a amplitude do número de acidentes
Amplitude = np.ptp(Dados)

# b) Calcule o desvio padrão amostral do número de acidentes
DpAmostral = np.std(Dados,ddof=1)

# Saida:
print(f'# Exercacio 01: Amplitude {Amplitude:.2f}')
print(60*'-')
print(f'# Exercacio 01: Desvio padrao amostral {DpAmostral:.2f}')
print(60*'-')

# Exercício 02 - Medidas de Dispersão

Dados_2 = np.array([7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 7.5])

# a) Calcule a variância populacional e amostral das notas
Var_pop = np.var(Dados_2,ddof=0)
Var_Amostral = np.var(Dados_2,ddof=1)

# b) Calcule o intervalo interquartil (IIQ) das notas.

IIQ_25 = np.percentile(Dados_2,25)
IIQ_50 = np.percentile(Dados_2,50)

# Saida:
print(f'# Exercicio 02: variancia populacional {Var_pop:.2f}')
print(60*'-')
print(f'# Exercicio 02: variancia amostral {Var_Amostral:.2f}')
print(60*'-')
print(f'# Exercicio 02: Intervalo interquartil(Q1 - Q2) =  Q1- {IIQ_25}; Q2- {IIQ_50}; IIQ- {IIQ_25-IIQ_50}') # intervalo interquartil é Q1 - Q2

# Exercício 03 - Medidas de Dispersão

Dados_3 = np.array([15.2, 16.5, 14.8, 17.0, 15.5, 16.0, 15.8, 16.2, 15.0, 16.8, 17.5, 15.3])

# a) Calcule o desvio padrão populacional das alturas usando NumPy.
Dp_pop = np.std(Dados_3,ddof=0)

# b) Calcule o iiq das alturas usando Pandas
Dados_3_1 = pd.Series([15.2, 16.5, 14.8, 17.0, 15.5, 16.0, 15.8, 16.2, 15.0, 16.8, 17.5, 15.3])
Q_1 = Dados_3_1.quantile(0.25)
Q_2 = Dados_3_1.quantile(0.75)
IIQ = Q_2 - Q_1

# Saida:
print(60*'-')
print(f'# Exercicio 03: desvio padrao populacional {Dp_pop:.2f}')
print(60*'-')
print(f'# Exercicio 03: iiq das alturas usando Pandas {IIQ:.2f}')
print(60*'-')

# Exercício 04 - Medidas de Dispersão

# a) Crie uma Series do Pandas com esses dados.
Tempo_espera = pd.Series([3, 5, 2, 8, 4, 4, 6, 3, 5, 7, 9, 3, 5, 4, 6])

# b) Calcule a amplitude do tempo de espera usando Pandas
Maximo = Tempo_espera.max()
Minimo = Tempo_espera.min()

# c) Calcule o desvio padrão amostral do tempo de espera usando Pandas
Dp_amostral = Tempo_espera.std(ddof=1)

# d) Calcule o intervalo interquartil (IIQ) do tempo de espera usando Pandas
Q_25 = Tempo_espera.quantile(0.25)
Q_75 = Tempo_espera.quantile(0.75)
IIQ2 = Q_75 - Q_25

# Saidas:
print(60*'-')
print(f'# Exercicio 04: DataFrame tempo de espera \n{[Tempo_espera]}')
print(60*'-')
print(f'# Exercicio 04: Amplitude {Maximo-Minimo}')
print(60*'-')
print(f'# Exercicio 04: desvio padrao amostral do tempo de espera usando Pandas {Dp_amostral:.2f}')
print(60*'-')
print(f'# Exercicio 04: intervalo interquartil (IIQ) do tempo de espera usando Pandas {IIQ2:.2f}')

# Exercício 05 - Medidas de Dispersão
Temperaturas_rec = pd.read_csv("temperaturas.csv")
print(60*'-')
print(Temperaturas_rec)
print(60*'-')
Temperaturas_array = np.array(Temperaturas_rec['Temperatura_Media_C']) # Filtrando a coluna temperaturas , e criando um array no numpy, para calcula as medidas
# a) Média
Media = np.mean(Temperaturas_array)

# b) Mediana
Mediana = np.median(Temperaturas_array)

# c) Moda
Moda = Temperaturas_rec['Temperatura_Media_C'].mode()

# d) Amplitude
Amplitude_2 = np.ptp(Temperaturas_array)

# e) Variância populacional e amostral
Var_Amostral2 = Temperaturas_rec['Temperatura_Media_C'].var(ddof=1)
Var_pop2 = Temperaturas_rec['Temperatura_Media_C'].var(ddof=0)

# f) Desvio padrão populacional e amostral
Dp_amostral2 = Temperaturas_rec['Temperatura_Media_C'].std(ddof=1)
Dp_pop2 = Temperaturas_rec['Temperatura_Media_C'].std(ddof=0)

# g) Q1, Q2, Q3 e IQQ

Q1 = Temperaturas_rec['Temperatura_Media_C'].quantile(0.25)
Q2 = Temperaturas_rec['Temperatura_Media_C'].quantile(0.50)
Q3 = Temperaturas_rec['Temperatura_Media_C'].quantile(0.75)
IIQ3 = Q3 - Q1

# Saidas:
print(60*'-')
print(f'# Exercicio 05: Media utilizando pandas {Media:.2f}')
print(60*'-')
print(f'# Exercicio 05: Mediana utilizando pandas {Mediana:.2f}')
print(60*'-')
print(f'# Exercicio 05: Moda utilizando pandas {Moda}')
print(60*'-')
print(f'# Exercicio 05: Amplitude utilizando pandas {Amplitude_2:.2f}')
print(60*'-')
print(f'# Exercicio 05: Variancia utilizando pandas, variancia amostral {Var_Amostral2:.2f} e variancia populacional {Var_pop2:.2f}')
print(60*'-')
print(f'# Exercicio 05: Desvio padrao populacional e amostral, desvio padrao amostral {Var_Amostral2:.2f} e desvil padrao {Var_pop2:.2f}')
print(60*'-')
print(f'# Exercicio 05: Quantil 1: {Q1}; Quantil 2: {Q2}; Quantil 3:{Q3}. Intervalo interquantil: {IIQ3}')









