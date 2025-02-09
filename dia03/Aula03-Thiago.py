# %%
import pandas as pd 
import numpy  as np
import os

# %%
# Listando os arquivos que temos dentro do diretório para pegar o nome correto.
os.listdir("../data/")


# %% 
# Importando o df de customers para o Python
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# ordenação do menor para o maior, por padrão o ascending vem como true.
df = df.sort_values(by = "Points")
df

# %% 
# ordenação do maior para o menor
df.sort_values(by = "Points", ascending=False, inplace=True)
df.rename(columns={"Name":"Nome", "Points": "Pontos"}, inplace=True)
df

# %%
# Qual é a melhor prática de usar ou não o inplace.
# Como criar um "pipeline de dados", aqui é possível encadear os comandos.
df = (df.sort_values(by = "Pontos", ascending=False).rename(
    columns={"Name":"Nome", "Points": "Pontos"}))
df

# %%
# aqui vamos ordenar os pontos do maior para o menor, 
# se tiver os mesmos pontos, o nome vai ser um critério de desempate.
# é possível usar uma lista dentro do sort_values by e também é possível 
# passar uma lista dentro da forma da ordenação.

df = df.sort_values(by = ["Pontos", "Nome"], ascending=[False, True])
df
# %%
df = (df.sort_values(by = ["Points", "Name"], 
                     ascending=[False, True]).rename(
                         columns={"Name":"Nome", "Points": "Pontos"}))
df
# %%
df.sort_values(by = ["Pontos", "Nome"], ascending=[False, True]).tail(10)
# %%
# --------------------------------------------------------------------------------
# ** Removendo Duplicatas
# --------------------------------------------------------------------------------
# %%
import pandas as pd 
import numpy  as np
import os

# %%
# Listando os arquivos que temos dentro do diretório para pegar o nome correto.
os.listdir("../data/")


# %% 
# Importando o df de customers para o Python
data = {
    "Nome": ["Thiago", "Andre", "Gabriela", "Thiago", "Gabriela", "Victor", "Arthur"],
    "Idade": [36,35,31,36,31,4,2], 
    "updated_at": [1,2,3,1,2,3,4]
        }

df = pd.DataFrame(data)
df
# %%
# Remover as duplicadas se os dados são exatamente iguais, 
# só o comando abaixo é suficiente, agora, se há alguma linha diferente
# é possível usar o comando da próxima camada
df.drop_duplicates()
# %%
# Aqui vamos comparar 2 colunas, independente da 3
# ele vai priorizar o primeiro na ordem das linhas por default

df.drop_duplicates(subset=["Nome","Idade"], keep="first")
# %%
# O correto ao usar o drop_duplicates é fazer a ordenação com base no campo 
# de atualização, ou uma coluna de controle e depois utilizar o comando.
# como no exemplo à seguir:

df.sort_values(by="updated_at", ascending=False)
# %%
# Tentativa de validação da ordem dos campos, para validar se temos o mesmo resultado
# encadeando os comandos

df = df.sort_values(by="updated_at", ascending=False).drop_duplicates(
    subset=["Nome","Idade"], keep="first")
df

# %%
# --------------------------------------------------------------------------------
# EXERCICIO
# Quer saber a última transação de cada ID_Customer
#
# --------------------------------------------------------------------------------
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
# %%
# Dropou as duplicadas e pegamos a ultima data de atualização

df_last = (df.sort_values(by="DtTransaction", ascending=False).drop_duplicates(
    subset=["IdCustomer"], keep="first"))
df_last
# %%
df_last['IdCustomer'].nunique()
# %%
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]
# %%
# Aqui provamos que o 

df_last[df_last["IdCustomer"] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
# %%
# %%
# --------------------------------------------------------------------------------
# 
# Convertendo tipos
#
# -------------------------------------------------------------------------------
# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
df.dtypes
# %%
# comando para converter 

df["Points"].astype(str)
# %%
