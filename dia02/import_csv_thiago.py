# %%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=";")
df_customers
# %%
# Tamanho do DF
df_customers.shape
# %%
# Quantos Bytes essa tabela ocupa da memória.
df_customers.info(memory_usage='deep')
# %%
# Fotografia da quantidade de pontos. Estatistica descritiva
df_customers['Points'].describe()
# %%
# Agora, vamos converter a coluna Points para integer
df_customers['Points'].astype(int)
# %%
# Descobrindo quem tem o maximo de pontos 
# fazendo operações lógicas

df_customers['Points'].max()

# %%
# Assim que fazemos filtros em Pandas

condicao = df_customers['Points'] > 1000
df_customers[condicao]

# %%
# Se fossemos trabalhar com lista, a operação seria realizada dessa forma:

notas = [4.5, 6, 7, 3.5]
for i in notas: 
    if i > 5:
        print(i)
# %%
# Para fazer a mesma operação em lista, como exemplo, adicionar +1 à elas:
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas
# %%
# Encontrando a pessoa que possui mais pontos
#
maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]

# %% 
# É normal visualizarmos algumas soluções de forma mais direta, 
# como por exemplo:
condicao = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao]

# Ou dessa forma:
# Ela retorna um Dataframe, então eu consigo navegar nas colunas
df_customers[df_customers['Points'] == df_customers['Points'].max()]["Name"].iloc[0]

# %%
# Dessa forma conseguimos buscar o maior pontuador, sem chumbar o k
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
# filtro para verificar quem está em um intervalo
# por ser vetorial, não podemos usar o and, então é necesário usar o &
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
condicao
# %%
df_customers[condicao].shape
# %%
