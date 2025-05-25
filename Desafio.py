# Desafio: criando vizualizações de dados com arquivo csv;
# Bibliotecas:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Arquivo:
Dataset = pd.read_csv('avaliacao_turistas_recife.csv')

# Distribuição do numero de dias de estadia dos turista em Recife: 
Num_day = Dataset['Dias_Estadia']

plt.hist(Num_day)
plt.xlabel('Dias de estadia')
plt.ylabel('Frequencia')
plt.grid(color='blue')
plt.title('Distribuição do numero de dias de estadia dos turista em Recife')
plt.show()

# Media de avaliações para cada aspecto: Atrativos,Hospedagem,Transporte,Gastronomia

Av_Atrativos = Dataset['Avaliacao_Atrativos']
Media_Atrativos = Av_Atrativos.mean()
plt.bar(Av_Atrativos,Media_Atrativos,color='Blue',width=0.2)
plt.grid()
plt.xlabel('Atrativos')
plt.ylabel('Media Atrativos')
plt.title('Avaliações: Atrativos x MediaAtrativos')
plt.show()

Av_Hospedagem = Dataset['Avaliacao_Hospedagem']
Media_Hospedagem = Av_Hospedagem.mean()
plt.bar(Av_Hospedagem,Media_Hospedagem,color='Blue',width=0.2)
plt.grid()
plt.xlabel('Hospedagem')
plt.ylabel('Media Hospedagem')
plt.title('Avaliações: Hospedagem x MediaHospedagem')
plt.show()

Av_Transporte = Dataset['Avaliacao_Transporte']
Media_Transporte = Av_Transporte.mean()
plt.bar(Av_Transporte,Media_Transporte,color='Blue',width=0.2)
plt.grid()
plt.xlabel('Transporte')
plt.ylabel('Media Transporte')
plt.title('Avaliações: Transporte x MediaTransporte')
plt.show()

Av_Gastronomia = Dataset['Avaliacao_Gastronomia']
Media_Gastronomia = Av_Gastronomia.mean()
plt.bar(Av_Gastronomia,Media_Gastronomia,color='Blue',width=0.2)
plt.grid()
plt.xlabel('Gastronomia')
plt.ylabel('Media Gastronomia')
plt.title('Avaliações: Atrativos x MediaGastronomia')
plt.show()

# Relação: dias de estadia x av geral

Av_geral_sum = Av_Hospedagem + Av_Gastronomia + Av_Atrativos + Av_Transporte
Mean_Av_Total = Av_geral_sum.mean()

plt.scatter(Num_day,Av_geral_sum)
plt.xlabel('Dias de Estadia')
plt.ylabel('Avaliação Geral')
plt.title('Dias de estadia x Av geral')
plt.grid()
plt.show()

# Avaliacao turista: Brasileiros x Gringos 5

# Turistas brasileiros: 5.1
Dataset['Turista_brasileiros'] = (Dataset['Nacionalidade'] == 'Brasil')

# Avaliações: Brasileiros x Turistas 5.2
Av_brasileiros = Dataset.loc[['Turista_brasileiros'],'Avaliacao_Atrativos'] # Usamos a coluna booleana para selecionar as linhas e depois a coluna de avaliação.
print('Avaliacoes: Brasileiros x Atrativos')
print(Av_brasileiros.describe())

# Avaliações: Brasileiros x Turistas 5.3

Av_turista = Dataset.loc[~Dataset['Nacionalidade'],'Avaliacao_Atrativos'] # Usamos o operador '~' para inverter a coluna booleana (True vira False e vice-versa).
print('Avaliacoes: Turista x Atrativos')
print(Av_turista.describe())

