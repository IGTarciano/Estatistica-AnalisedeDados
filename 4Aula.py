# Igor T Gomes
# 13/05/2025
# Modulo 2 - Detecção de outliers : 4° Aula 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Outliers : são pontos de dados que desviam siguinificamente dos outros dados em umn conjunto
# Ocorrem por conta da variabilidade natural extrema ou por erros na coleta de dados;
# É importante identificar por motivos:

# Distorção estatisticas;
# Indicam problemas na qualidade dos dados;
# Representar informações importantes.

# Metodos estatisticos para identificar autliers:

# Z-Score; Z-Score = 0 indica que o valor esta no padrão, quanto mais distante de zero, está mais fora do padrão;

# Exemplo : Calculando e identificando os autliers

# Você tem dados da temperatura média diária (°C) em Fernando de Noronha durante um mês:
Temperatura = [28.1, 28.5, 27.9, 28.3, 35.2, 28.0, 28.2, 28.4, 27.8, 28.6, 28.1,
28.3, 27.7, 28.5, 28.2, 28.4, 27.9, 28.3, 28.1, 28.6, 28.0, 28.2,
28.4, 27.8, 28.5, 28.2, 28.3, 27.7, 28.6, 28.1] 
temp_array = np.array(Temperatura)
# Calcule o Z-score para cada temperatura e identifique os dias que são outliers usando um limiar de +/- 3.
media = np.mean(Temperatura)
DesvioPd = np.std(Temperatura)
Z_score = (temp_array-media)/DesvioPd

for score,temp in zip(Z_score,temp_array): # score = Z_score e temp = temp_array, assim as variaveis interam entre elas. O zip ele junta as duas listas.
    if score <= -3 or score >= 3:
        print(f'Os valores mais assimetricos sao {score:.2f}')
        print(f'Outliers: {temp}')
print(f'A media dos valores a {media:.2f}')

# Exemplo :

# Os preços (em R$) de um determinado tipo de artesanato no Mercado de São José são:
Precos = [15, 18, 16, 20, 17, 19, 15, 22, 18, 17, 16, 19, 17, 20, 18, 16, 45,17, 19, 21]
# Utilize o método do Intervalo Interquartil (1.5 * IIQ) para identificar os outliers neste conjunto de preços.

Precos_numpy = np.array(Precos)

Q1 = np.percentile(Precos_numpy,25)
Q3 = np.percentile(Precos_numpy,75)
IIQ = Q3 - Q1
Limite_inf = Q1 - 1.5 * IIQ
Limite_sup = Q3 + 1.5 * IIQ

for i in Precos_numpy:
    if i >= Limite_sup or i <= Limite_inf:
        print(f'O autielrs : {i}')
        
plt.boxplot(Precos_numpy)
plt.grid(axis='y')
plt.show()