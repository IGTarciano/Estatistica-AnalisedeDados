# Exercícios de Fixação de Conceitos Pandas
import pandas as pd

# 1° - Exercício 1: Criando Serie 

Frutas = pd.Series(['Maca','Banana','Laranja','Morango'],index=['A','B','C','D'])
print(Frutas.index)

Preco = pd.Series(['R$ 2.50','R$ 1.80','R$ 3.20','R$ 4.00'],Frutas.index)
print(Preco)

# 2° - Exercício 2: Criando DataFrames

Dados_Alunos = {
    'Nome':['Juan','Thais','Caio','Crislayne','Jesua'],
    'Idade':[19,24,18,23,52],
    'Curso':['Engenharia','Computacao','Medicina','Direito','Biologia']
}

alunos = pd.DataFrame(Dados_Alunos) # criando um dataframe
print(alunos)

# 3° - Exercício 3: Acessando Dados em Series e DataFrames

print(Frutas['C']) # selecionando apenas um indice
print(alunos['Nome']) # Selecionando apenas uma ccoluna 
print(alunos[['Nome','Curso']]) # selecionando duas colunas no dataframe

# 4° - Exercício 4: Filtrando DataFrames

id_MaiorIgual = alunos['Idade'] >= 21
print(alunos[id_MaiorIgual]) 

# 5° - Exercício 5: Adicionando e Removendo Colunas

alunos['Cidade'] = ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador','Recife'] # inserindo uma coluna 
print(alunos)
remuvColum = alunos.drop('Curso',axis=1) # Removendo uma coluna 
print(remuvColum)   

# 6° - Exercício 6: Agrupamento de Dados

vendas_categoria = {
'Produto': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
'Categoria': ['Eletronico   s', 'Vestuario', 'Eletronicos', 'Alimentos', 'Vestuario', 'Alimentos','Eletronicos'],
'Valor': [100, 50, 120, 30, 60, 40, 110]
}

df_categoria_valor = pd.DataFrame(vendas_categoria)
df_categoria_valor_soma = df_categoria_valor.groupby(by=['Categoria'])['Valor'].sum()
print(df_categoria_valor_soma)

# O comando roupby(by=['Produto','Categoria']) realiza o agruopamento dos valores do indice
# e o comando sum() faz a soma deles

# 7° - Exercício 7: Ordenando DataFrames


ordemalf = alunos.groupby(by=['Nome'])

#print(f'Alunos em ordem alfabetica')
#for nome in ordemalf:
    # print(nome)
    
# 8° - Exercício 8: Aplicando Funçõe
def Dobrar(x): # criamos uma function para utilziar no comando aplly
    return x * 2

alunos['Idade_dobrada'] =  alunos['Idade'].apply(Dobrar) # e aqui junto ao comando apply utilizamos para dobrar as idades
print(alunos)

# Comandos utilizados:

# pd.Series - cria uma series 
# pd.DataFrame() - cria uma data frame
# apply() - é utilziada para aplicar uma função criada em um contexto
# df.groupby(by=['colum']) - utilziada para ordena uma coluna
# drop('Colum',axis=1) - utlizada para excluir colunas
