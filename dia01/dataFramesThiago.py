# %%
# Importando as libs:
import pandas as pd
# %%
# Vamos criar um dicionário 

data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade":[31, 32, 32, 2]
}

data
# %%
# descobrindo a idade da primeira pessoa
data["idade"][0]
# %%
# Transformar esse dicionário em um df
df = pd.DataFrame(data)
df
# %%
# Para garantir que é a primeira posição, coloca o iLoc
df["idade"].loc[0]
# %%
# acessando uma linha
df.iloc[0]
# %%
# descobrindo os nomes das colunas
df.columns
# %%
# mostra para nós em formato de texto o que estamos analisando
# além de mostrar a quantidade de memoria que esse df está consumindo
df.info(memory_usage='deep')
# %%
# Atributo que mostra os tipos de dados da coluna.
df.dtypes
# %%
# aplica estatísticas descritivas para as colunas numéricas
df.describe()
# %%
# Atribuir uma coluna nova
df['peso'] = [80, 53, 65, 14]
# %%
df.describe()
# %%
# Como o describe cria um dataframe com as estatísticas do nosso df, 
# é possível fazer uma pesquisa como nos demais dfs do python, então é possível
# buscar os dados como no exemplo a seguir.
sumario = df.describe()

sumario['peso']['mean']
# %%
