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
