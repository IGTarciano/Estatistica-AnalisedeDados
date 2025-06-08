# Dasafio de Analiose estatistica de dados : cooperativa agricola 

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.proportion import proportion_confint

Dados  = pd.read_csv('cana_de_acucar_produtividade.csv')
Data_base = Dados

# Estatistica descritiva gerais
try:
    AnaliseDescritiva_media_moda_mediana = [Data_base['rendimento_ton_hectare'],Data_base['idade_muda_meses'],Data_base['fertilizante_kg_hectare']]

    for i in AnaliseDescritiva_media_moda_mediana:
        Media = i.mean()
        Moda = i.mode()
        Mediana = i.median()
        
except ValueError as e:
    print('Sintaxe incorreta')

try:
    # Medidas de dispersão:
    
    AnaliseDespersao_dp_Amplitude = [Data_base['rendimento_ton_hectare'],Data_base['idade_muda_meses'],Data_base['fertilizante_kg_hectare']]

    for i in AnaliseDescritiva_media_moda_mediana:
        Desvio_padrao = i.std()
        Amplitude = i.max()-i.min()
    
    Q1 = Data_base['rendimento_ton_hectare'].quantile(0.25)
    Q3 = Data_base['rendimento_ton_hectare'].quantile(0.75)
    IIQ = Q3 - Q1

    Q1 = Data_base['idade_muda_meses'].quantile(0.25)
    Q3 = Data_base['idade_muda_meses'].quantile(0.75)
    IIQ = Q3 - Q1
    
    Q1 = Data_base['fertilizante_kg_hectare'].quantile(0.25)
    Q3 = Data_base['fertilizante_kg_hectare'].quantile(0.75)
    IIQ = Q3 - Q1
except ValueError as e:
    print('Erro de sintaxe')