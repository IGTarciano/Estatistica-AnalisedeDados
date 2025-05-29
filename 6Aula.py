# Igor T Gomes
# 27/05/2025
# Modulo 2 - Estatistica Inferencial : 6° Aula 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats

# media das amostras == a media da população
# Calculando o erro :


# Intervalo de confiança
# Sintaxe para calcular intervalo de confiança:
# Interval_z_direct= stats.norm.interval(nivel_confiança,loc=media_amostral,scale=erro padrao)
#dp_pop = 0
#n_pop = 0
#ErroPdr = dp_pop / np.sqrt(n_pop) # Erro padrão: np.sqrt() 

# Exercicio 01:
#dp_pop = 20
#n_pop = 64
#pmedio = 1010
#Nv = 0.90
#Interval_z_direct = stats.norm.interval(Nv,loc=pmedio,scale=ErroPdr) # Irá gerar um lista 
#print(f'Intervalo de confiança: [R$ {Interval_z_direct[0]:.2f}, R$ {Interval_z_direct[1]:.2f}]') # nas chaves colocamos a posição do limite sendo interior=0 e superior=1

# Qnd o dp_pop é desconhecido: 
#Nv_confianca = 0
#Md_amostral = 0
#IC = 0
# Calculando o erro pd:
#dp_am = 0
#n_amostral = 0
#ErroPdr_t = dp_am / np.sqrt(n_amostral)
# Grau de liberdade: n - 1
#grau_liberdade = n_amostral - 1
# utilizando a função stats.t.interval: Interval_t_direct = stats.t.interval(nivel de confiança,df=grau de liberdade,loc=media amostral,scale=erro padrão)

# Exercicio 11:

# n amostral = 80
# media amostral = 8.5
# dp amostral = 2.8
# IC = 0.99

#n_amostral = 80
#Md_amostral = 8.5
#dp_am = 2.8
#Nv_confianca = 0.99
#Interval_t_direct = stats.t.interval(Nv_confianca,df=grau_liberdade,loc=Md_amostral,scale=ErroPdr_t)
#print(f'Intervalo de confiança: [{Interval_t_direct[0]:.2f}min, {Interval_t_direct[1]:.2f}min]') # nas chaves colocamos a posição do limite sendo interior=0 e superior=1


# Desafio:

try:
    Datase_aula6 = pd.read_csv('amostraPesoAltura.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'Online Retail.xlsx' não encontrado. Verifique o caminho.") # Tratando o erro caso não encontre o dataser

Media_peso = Datase_aula6['Weight(Pounds)'].mean()
Dp_amostral = Datase_aula6['Weight(Pounds)'].std()
IC = 0.90
grau_liberdade = 50 - 1
ErroPdrAmostral = Dp_amostral / np.sqrt(50)

Interval_t_direct = stats.t.interval(IC,df=grau_liberdade,loc=Media_peso,scale=ErroPdrAmostral)
print(f'Intervalo de confianca: [{Interval_t_direct[0]:.2f}, {Interval_t_direct[1]:.2f}]') # nas chaves colocamos a posição do limite sendo interior=0 e superior=1

try:
    Dataset_aula6 = pd.read_csv('populacaoPesoAltura.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'Online Retail.xlsx' não encontrado. Verifique o caminho.")
    
Media_peso_pop = Dataset_aula6['Weight(Pounds)'].mean()

if Media_peso_pop >= 125.79 and Media_peso_pop <= 131.90:
    print(f'Amostra  confiavel: {Media_peso_pop:.2f}')
else:
    print(f'Amostra inconfiavel. Busque pegar mais amostra: {Media_peso_pop:.2f}')

try:
    plt.hist(Interval_t_direct,)
    plt.show
except FileExistsError:
    print('Dados não encontrado!')