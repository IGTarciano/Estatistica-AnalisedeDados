# Lista de exercaicio: Estatistica dadsescritiva 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Z-score: ele indica quantos desvios  padrão um determinado valor está acima ou abaixo da média.
# interpretação: quanto mais distante de 0, mais disperso está os dados , e mais longe está da media;
# formula: z_score = (*dados* + media) / desvio_padrão 

# Exercício 1: Você tem dados da temperatura média diária (°C) em Fernando de Noronha durante um mês:

Temperatura = [28.1, 28.5, 27.9, 28.3, 35.2, 28.0, 28.2, 28.4, 27.8, 28.6, 28.1,
28.3, 27.7, 28.5, 28.2, 28.4, 27.9, 28.3, 28.1, 28.6, 28.0, 28.2,
28.4, 27.8, 28.5, 28.2, 28.3, 27.7, 28.6, 28.1]
tem_numpy = np.array(Temperatura)

# Calcule o Z-score para cada temperatura e identifique os dias que são outliers usando um limiar de +/- 3

Dp = np.std(Temperatura)
Media = np.mean(Temperatura)
Z_score = (Temperatura - Media)/Dp

for score, temp in zip(Z_score, tem_numpy):
    if score <= -3 or score >= 3:
        print(f'Score:{score:.2f}')
        print(f'Outliers: {temp:.2f}')
        
        
# Exercício 2: Os preços (em R$) de um determinado tipo de artesanato no Mercado de São José são:
Precos = [15, 18, 16, 20, 17, 19, 15, 22, 18, 17, 16, 19, 17, 20, 18, 16, 45,
17, 19, 21]
np.array(Precos)
# Utilize o método do Intervalo Interquartil (1.5 * IIQ) para identificar os outliers neste conjunto de preços.

Dp_precos = np.std(Precos)
Media_precos = np.mean(Precos)

Z_score_precos = (Precos-Media_precos)/Dp_precos
for score_precos,Preco in zip(Z_score_precos,Precos):
    if score_precos <= -3 or score_precos >= 3:
        print(f'Zscore precos: {score_precos:.2f} | Autliers precos: {Preco:.2f}')

# Exercicio 3:

Temp_viagem = [25, 30, 28, 35, 22, 40, 27, 60, 32, 29, 31, 33, 26, 38, 34]

plt.boxplot(Temp_viagem,
            patch_artist=True, # Preenche toda a caixa com a cor
            boxprops={'facecolor':'lightblue'}, # define a cor da caixa
            whiskerprops={'color':'gray'}, # define a cor dos bigodes do grafico
            capprops={'color':'black'}, # Define a cor da mediana 
            flierprops={'marker':'o','markerfacecolor':'red','markersize':8,'linestyle':'none','markeredgecolor':'black'} # Estilo dos outliers
            )
plt.xlabel('Altura dos predios do bairro do Pina')
plt.title('Teste de amostra: altura predial')
plt.grid()
plt.show()


# Exercício 4: 

Altura_metro = [80, 90, 75, 85, 105, 78, 82, 88, 70, 95, 81, 86, 77, 92, 150]
np.array(Altura_metro)
Q1_altura = np.percentile(Altura_metro,25)
Q3_altura = np.percentile(Altura_metro,75)
IIQ_altura = Q3_altura-Q1_altura     
Media_altura = np.mean(Altura_metro)
Dp_altura = np.std(Altura_metro)

# A)
Z_score_altura = (Altura_metro-Media_altura)/Dp_altura
for score_altura,Altura in zip(Z_score_altura,Altura_metro):
    if score_altura <= -3 or score_altura >= 3:
        print(f'A) Autliers: {Altura:.2f}')
# B)

Limite_inf = Q1_altura - 1.5 * IIQ_altura
Limite_sup = Q3_altura + 1.5 * IIQ_altura
for altura in Altura_metro:
    if altura <= Limite_inf or altura >= Limite_sup:
        print(f'B) Autliers: {altura:.2f}')