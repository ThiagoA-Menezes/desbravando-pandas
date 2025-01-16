# %%
#Parquet
import pandas as pd

df = pd.read_parquet("../data/transactions_cart.parquet")
df
# %%
df.shape

# %%
df.head()

# %%
df.tail()

colunas = df.columns.tolist()
colunas.sort()
colunas
# %%

# colunas = ['UUID',
#            "Points",
#            'IdCustomer',
#            "DtTransaction"]
# 
df = df[colunas]
df

# %%
df.info(memory_usage='deep')

# %%
## Exercício:
## Fazer a leitura do arquido data/ipea/homicidios.csv de forma correta e informe
## Quantidade de Linhas --  891 Linhas
## Quantidade de colunas -- 4 Colunas
## Nome da Primeira linha 
## nome da última coluna


## Carregue os dados do arquivo data/ipea/homicidios-mulheres-negras.csv de forma correta
## e informe:
## Quantas colunas do tipo numérico?
## Quantas colunas são do tipo object?
## Qual o tamanho destes dados em memória?


df_hom = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df_hom

# %%
# Nome da Primeira Linha --> Name: 0, dtype: object
df_hom.iloc[0]
# %%
# Nome da ultima coluna --> Name: 890, dtype: object
df_hom.iloc[-1]
# %%
# O maior valor de homicidios
condicao_max = df_hom["valor"] == df_hom["valor"].max()
df_hom[condicao_max]
# %%
# menor número de homicidios
condicao_min = df_hom["valor"] == df_hom["valor"].min()
df_hom[condicao_min]

# %% 
# Vou colocar a OS só para verificar quais os arquivos estão na pasta
# para não errar o nome do arquivo.
import os 
os.listdir("../data/ipea")

# %%
# Agora vamos analisar os de mulheres negras
df_hom_m_pretas = pd.read_csv("../data/ipea/homicidios-mulheres-negras.csv", sep=";")
df_hom_m_pretas
# %%
df_hom_m_pretas.describe()
# %%
# Aqui eu vou conseguir uma estatística descritiva do 
# dataframe.
df_hom_m_pretas.shape
# %%
# Aqui eu vou descobrir quais são as colunas do tipo object e 
# o tamanho de memória qu esse df ocupa.
df_hom_m_pretas.info(memory_usage="deep")
# %%
# Maior número de mortes de mulheres pretas
maior_hom = df_hom_m_pretas["valor"] == df_hom_m_pretas["valor"].max()
df_hom_m_pretas[maior_hom]
# %%
# Quais foram os menores, mas aqui acredito que não havia levantamento com o 
# detalhe que temos nos dias de hoje.
menor_hom = df_hom_m_pretas["valor"] == df_hom_m_pretas["valor"].min()
df_hom_m_pretas[menor_hom]

# %%
