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
df_customers[df_customers['Points'] == df_customers['Points'].max()][["Name", "Points"]].iloc[0] 
# df_customers[df_customers['Points'] == df_customers['Points'].max()][["Name", "Points"]]

# %%
# Dessa forma conseguimos buscar o maior pontuador, sem chumbar o k
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %%
# filtro para verificar quem está em um intervalo

condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
condicao
# %%
# por ser vetorial, não podemos usar o and, então é necesário usar o &
# para criar um novo df, para evitar que o Python altere o dado principal,
# lembre-se que o python usa referência para tudo, então 
# coloque a função .copy() ao final do seu filtro ou condição.

condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao].copy()


df_1000_2000['Points'] = df_1000_2000["Points"] + 1000
df_1000_2000

# %%
df_customers[condicao].shape
# %%
# Series de Dados
df_customers['UUID']
# %% 
# Dataframe quando passamos uma Lista
# assim que navega no df pelas colunas
df_customers[['UUID', 'Name']]
# %%
# dessa forma eu posso ordenar a lista de colunas
# colunas = list(df_customers.columns)
colunas = df_customers.columns.tolist()
colunas.sort()
colunas
# %%
# aqui, eu posso reatribuir o meu df à ele mesmo e usar esses dados com 
# a coluna ordenada

df_customers = df_customers[colunas]
df_customers
 # %%
# para Renomear colunas usamos o seguinte comando...
# e podemos usar um dicionário para fazer isso
# ele gera um df novo, ele não altera o df anterior, só altera se reatribuirmos 
# ao dataframe
df_customers = df_customers.rename(columns={'Name' : 'Nome',
                                             'Points' : 'Pontos'})
df_customers
# %%
# Há uma outra forma de fazer esse rename.
# quando usamos o inplace, ele muda o df original, diferente do comando anterior
# por isso com o inplace não é necessário reatribuir ao df
df_customers.rename(columns={"UUID" : "Id"}, inplace=True)
df_customers

# %%
# Importando outro arquivo para o df.
# nessa parte do código, colocamos o nome das colunas, 
# já que o no arquivo não vinha com eles.
df_p = pd.read_csv("../data/products.csv", 
                   sep=";", 
                   #header=None, 
                   names=['Id', 'Name', 'Description'])
df_p
# %%
# Exercício
df_p = df_p.rename(columns={'Name':'Nome', 
                            'Description': 'Descrição',
                            "Id" : "Localizador"})
df_p
# %%
# Extraindo para virar uma lista e posteriormente adicioná-la a um dicionário.
df_pcolunas = df_p.columns.tolist()
df_pcolunas
# %%
# Renomeando as colunas sem a necessidade de usar a reatribuição.

df_p.rename(columns={"Localizador" : "Id",
                    "Nome" : "Comandos",
                     "Descrição" : "Texto Livre"}, inplace=True)

df_p
# %%
