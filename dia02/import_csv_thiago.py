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
