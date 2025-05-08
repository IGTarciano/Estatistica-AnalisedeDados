# Igor T Gomes
# 29/04/2025
# Modulo 2 - Estatisca para ciencia de dados : 1° Aula

# Estatistica descritiva : visa torna os dados coletados mais faceis de entender (Tabela, graficos e medidas);
# Estatistica inferencial : parte da estatistica que permite tomar conclusões sobre uma população.
# Conceitos estatiscia:
# População; Conjunto completo de dados para investigação;
# Amostra; Uma parte da população;
# Variavel : qualitativa e continua;

# import pandas:
# Oferece duas estruturas de dados:
# Seres; DataFrame(tabela bidimensionais com colunas de diferentes tipos);
# Conceitos!
# DataSets: conjunto de dados**


# Praticando com pandas: 

import pandas as pd
# sintaxe pandas: pd."função"
idades = pd.Series([25,30,22,28,35],index=['Ana','Vitor','Carlos','Rafael','Jonas']) # usando a estrutura de dados series
print(f'\nIdades series: {idades}')

# printando o indice:
print(f'Vizualizando os indices:{idades.index}')

# printando conteudo de um indice:
print(idades['Ana'])

# DataFrame é uma tabela, com linhas e colunas: 

Dados = {
    'Nome' : ['Igor','Thais','Ana','Jesua'],
    'Idade' :  [25,30,58,60]  
}

pad = pd.DataFrame(Dados) # criou uma tabela com o conteudo de Dados
print(pad)

print(Dados['Nome']) # manipulando apenaos a coluna 'nome' pelo indice, que é a posição do arrays;
mais_de_50 = pad['Idade'] > 50
print(pad[mais_de_50]) # filtrando os dados
pad['Cidades'] = ['Recife','Paulista','Jaboatão','Candeias'] # criando uma colunda no data frame pad
print(pad)
dados = pad.drop('Idade',axis=1) # excluindo uma coluna
print(dados)
dados = pad.drop(2,axis=0) # excluindo uma linha
print(dados)

# pd.head. : sintaxe para importação de arquivo;
funcionarios = pd.read_csv('funcionario.csv')
print(funcionarios)

# .head ; retorna os 5 primeiros 
print(funcionarios.head())

# .tail ; retorna os 5 ultimos
print(funcionarios.tail())

# pd.head : para arquivo excel;
funcionarios2 = pd.read_excel('funcionario2.xlsx',sheet_name='nome') # para arquivos excel , usar sheet_name= >nome da aba<, para importa a aba necessaria
print(funcionarios2.head())
print(funcionarios2.tail())
 