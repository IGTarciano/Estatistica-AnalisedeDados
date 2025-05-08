# Igor T Gomes
# 06/05/2025
# Modulo 2 - Estatisca descritiva : 2° Aula


# Conjunto de metodos que visam torna os dados coletados mais facil de entender;
# categoria: 
# * Medias de tendencia central: media;mediana e moda
# * Media de dispersão;
# * Vizualização de dados;

# Biblioteca - Numpy

import numpy as np
import pandas as pd

# np.mean(): calculamos a media do array
# np.mediana(): calculamos a mediana do array

# criando uma Serie :
passageiros = np.array([45,52,38,60,48,55,40,58,50,42])

# media = np.mean(passageiros) # Media
# mediana = np.median(passageiros) # Mediana
# print(media)
# print(mediana)
# calculando a Moda: no numpy não temos um comando que calcule a moda direto
# np.unique("Sequencia de dados") - é uma função que retorna os dados de forma unica , e e sua contagem, com isso conseguimos achar moda. 

Dados = [31.5,32.0,31.8,32.5,33.0,32.0]

Media = np.mean(Dados)
#print(Media)
Mediana = np.median(Dados)
#print(Mediana)
DadosPandas = pd.Series([31.5,32.0,31.8,32.5,33.0,32.0])
Moda = DadosPandas.mode()
#print(Moda) # Calculando a moda usando pandas

lista_ocorrencias, contagem = np.unique(Dados,return_counts=True) # o unique ordena e conta ;
moda = lista_ocorrencias [contagem == np.max(contagem)] # a moda é igual ao maximo de ocorrencias da lista;
#print(moda) # calculando a moda com numpy.

# Calculando a amplitude e o desvio padrão amostral:

bsdados = np.array([2,0,1,3,2,2,0,1,2,4])
# A - 
Amplitude = np.ptp(bsdados)
# B - 
dp = np.std(bsdados,ddof=1)

print(f'{Amplitude} & {dp}')