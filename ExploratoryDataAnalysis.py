# Using the Online Retail dataset, we'll conduct exploratory data analysis and create an ABC curve.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Import the dataset
try:
    DataFrame_OnlineRetail = pd.read_excel("Online Retail.xlsx")
except FileNotFoundError:
    print("Erro: Arquivo 'Online Retail.xlsx' não encontrado. Verifique o caminho.") # Tratando o erro caso não encontre o dataser

# Clean DataFrame: removendo linhas com valores ausentes e duplicadas
DataFrame_OnlineRetail_Clean = DataFrame_OnlineRetail.dropna().drop_duplicates().copy() # Usar .copy() para garantir que temos um DataFrame independente

# Total value sales products : Usar .loc[:, 'NovaColuna'] para atribuir à coluna no DataFrame limpo
DataFrame_OnlineRetail_Clean.loc[:,'TotalValue'] = DataFrame_OnlineRetail_Clean['Quantity'] * DataFrame_OnlineRetail_Clean['UnitPrice'] # ":" siguinifica que será aplicado a todas as linhas

# Utilizando a coluna InvoiceDate para criar colunas uteis para a analise: assim poderemos fazer analises periodicas
try:
    Invoice_date_dt = pd.to_datetime(DataFrame_OnlineRetail_Clean['InvoiceDate'],errors='coerce')
except Exception as e:
    print(f"Erro ao converter 'InvoiceDate' para datetime: {e}")
    # Feita limpeza nas colunas utilizando: errors='coerce';
    
DataFrame_OnlineRetail_Clean['Year'] = Invoice_date_dt.dt.year
DataFrame_OnlineRetail_Clean['Month'] = Invoice_date_dt.dt.month
DataFrame_OnlineRetail_Clean['Day'] = Invoice_date_dt.dt.day
DataFrame_OnlineRetail_Clean['DayOfWeek'] = Invoice_date_dt.dt.dayofweek

# Ordenando os itens do maior para o menor faturamento durante os meses:
Year_Month_max_sales_df = DataFrame_OnlineRetail_Clean.groupby(['Year','Month'])['TotalValue'].sum()

x_label = [f'{year}-{month:02d}' for year,month in Year_Month_max_sales_df.index] # Criar rótulos formatados para o eixo X
plt.figure(figsize=(15,7)) # Aumenta o tamanho para melhor visualização
plt.bar(x_label,Year_Month_max_sales_df,color='skyblue')
plt.xlabel('Relação Ano-mês')
plt.ylabel('Faturamento total')
plt.title('Relação Anos/Meses X Total de faturamento')

plt.xticks(rotation=60,ha='right') # Rotaciona os rótulos para evitar sobreposição
# rotation=60:define o ângulo de rotação dos rótulos do eixo X em graus
# ha='right' (ou horizontalalignment='right'): alinhamento horizontal do texto do rótulo em relação ao,significa que o lado direito do texto do rótulo estará alinhado com a posição do tick

plt.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona linhas de grade horizontais
# axis: Este argumento especifica em qual(is) eixo(s) a grade será exibida.
# linestyle='--': Define o estilo da linha da grade.
# alpha=0.7:Controla a transparência (opacidade) das linhas da grade.

plt.tight_layout() # Ajusta o layout para evitar cortes
plt.show()

# Relacionar: Produto(codigo produto e descrição) x Qtd x Valor

Product_Qnt_value = DataFrame_OnlineRetail_Clean.groupby(['Description'])[['Quantity','TotalValue']].sum().sort_values(by='TotalValue',ascending=False).head(10).copy()

plt.figure(figsize=(12,5))
Product_Qnt_value['TotalValue'].plot(kind=bar,color='skyblue')
plt.title('Produto com maior faturamento')
plt.xlabel('Valor total')
plt.ylabel('Produto: descrição')
plt.xticks(rotation=45,ha='right')
plt.grid()
plt.show()