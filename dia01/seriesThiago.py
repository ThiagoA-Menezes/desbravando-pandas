# %%
# Importando as bibliotecas
import pandas as pd


# %%
# Criando a lista de idades.
idades = [30, 42, 90, 34]
idades
# %%
# Média das idades.
media = sum(idades) / len(idades)
media
# %%
# Variância

total = 0
for i in idades:
    total += (media - i)**2
variancia = total / (len(idades) - 1)

variancia
# %%
#Pegando a lista e transformando em uma serie de dados 
# Tranformação para series pandas
series_idades = pd.Series(idades)
series_idades
# %%
## Métodos pandas!
# Media 
# Depois de converter a lista em Serie, fica mais fácil de manipular com o pandas
series_idades.mean()
# %%
#Variancia
series_idades.var()
# %%
# Desvio Padrão
series_idades.std()
# %%
# Mediana
series_idades.median()
# %%
# Quartil
# 1 Quartil
series_idades.quantile(0.25)
# %%
# Sumarização
series_idades.describe()
# %%
# Dimensão da serie
series_idades.shape[0]
# %%
# Navegando na lista
series_idades[3]
# %%
# Navegando na serie

series_idades[:-1]
# %%
# Verificando o indice da serie
series_idades.index
# %%
# Navegando na serie de forma mais explicita

# Busca pela posição do indice, independente da forma como o indice 
# está estruturado. Ainda é possível passar o intervalo [0:2].
# Vai garantir a posição.
series_idades.iloc[0]
# %%
# É possível criar um novo para a serie
series_idades.name = 'idades'
series_idades
# %%
