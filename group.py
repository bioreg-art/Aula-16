import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'vendas': [100, 200, 150, 300, 120],
    'quantidade': [1, 2, 1, 3, 2]
})
    #media de vendas por categria
df.groupby('categoria')['vendas'].mean()

print(df.groupby('categoria')['vendas'].mean())

#Soma por categoria (todas as colunas numericas)
df.groupby('categoria').sum()

print(df.groupby('categoria').sum())

#Agrupar por multiplas colunas
df.groupby(['categoria', 'quantidade'])['vendas'].sum()

print(df.groupby(['categoria','quantidade'],as_index=False)['vendas'].sum())

#Todas as operações na coluna vendas agrupadas pela coluna categoria
df.groupby('categoria')['vendas'].agg(['sum', 'mean','max','count'])
print(df.groupby('categoria')['vendas'].agg(['sum', 'mean','max','count']))
#Ou com nomes personalizados
""" df.groupby('categoria').agg(
    total_vendas=('vendas', 'sum'),
    media_vendas=('vendas', 'mean') """