# Igor T Gomes
# 08/05/2025
# Modulo 2 - Vizualização de dados : 3° Aula 

# Faciliatam a compreensão;
# Identifica padrões e tendencias;
# Facilitam e validão as tomadas de decisões;
# Exploração de dados. 

# Tipicos de graficos:
# obs : detectação de outlires , são medidas foras do padrão.

# Graficos de barras; Histograma; grafico de linhas;grafico de pizza

# Biblioteca Matplolib: biblioteca fundamental para a criação de graficos e vizualizações de dados em python. 
# . Altamente personalizável;
# . Controle granular;
# . Integração completa com numpy e pandas. 

# obs: pyplot; submodulo da biblioteca Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([6,9])  # Eixo x 
y = np.array([6,250]) # Eixo y

#plt.plot(x,y,'o') # plot; grafico em linha
# sintaxe coloca-se os eixos que são os arrays , no lugar onde tem o 'O' é como saíra a vizualização da linha, nesse caso sairá so os pontos.
#plt.show() # A forma de dar print no matplotlib

# Exemplo:

categoria = ['Moradia','Alimentacao','Transporte','Educacao','Lazer','Outros']
porcentagens = [35,25,15,10,8,7]

#plt.pie(porcentagens,labels=categoria) # labels = , é a legenda do grafico de pizza, onde nas procentagens irá dar o nome correspondente / pie; grafico de pizza 
#plt.show()

trimestres = np.array(['01/23', '02/23','03/23', '04/23','01/24', '02/24','03/24', '04/24'])
taxa_desemprego = np.array([14.2, 13.8, 13.5, 13.2, 12.9, 12.5,12.2,12.0])

plt.plot(trimestres,taxa_desemprego,linestyle='dashed',)
# linestyle = ; conseguimos mudar o formato da linha
# markert = ; conseguimos alterar os marcadores
plt.xlabel('Trimestres 2023 e 2024') # legenda do eixo x
plt.ylabel('Taxa de desemprego') # legenda do eixo y
plt.title('Taxa de desemprego dos anos de 2023 a 2024') # titulo do grafico
plt.grid()
plt.show()

# Exemplo 2:

temperaturas = np.array([30, 32, 28, 33, 29, 31, 27, 34, 30, 32, 28, 33, 31, 29, 34])
vendas = np.array([120, 150, 100, 160, 115, 135, 90, 170, 125, 145, 105, 165,140,110,175])

plt.scatter(temperaturas,vendas)
plt.xlabel('Sorvetes vendidos')
plt.ylabel('Temperatura maxima C°')
plt.title('Relacao temperatura vendas')
plt.grid()
plt.show()