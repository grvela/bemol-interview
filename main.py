import pandas as pd
from decimal import Decimal

def to_double(object):
    string = object.replace("R$", "")
    string = string.replace(",", "")
    double = float(string)
    return double


data = pd.read_csv("data/data.csv")

data = data[['Filial', 'nome', 'valor_compra']]
data["valor_compra"] = data["valor_compra"].map(to_double)
data_compressed = data.pivot_table(index='Filial', columns='nome', aggfunc=sum)

manoa = data_compressed.loc['Loja Manoa']
manoa = manoa.dropna()

armando_mendes = data_compressed.loc['Loja Armando Mendes']
armando_mendes = armando_mendes.dropna()

cachoerinha = data_compressed.loc['Loja Cachoerinha']
cachoerinha = cachoerinha.dropna()

nome_manoa = manoa.sort_values().index[-1]
nome_armando = armando_mendes.sort_values().index[-1]
nome_cachoerinha = cachoerinha.sort_values().index[-1]

melhor_manoa = (nome_manoa[1], manoa.sort_values().values[-1])
melhor_armando = (nome_armando[1] ,  armando_mendes.sort_values().values[-1])
melhor_cachoerinha = (nome_cachoerinha[1] ,  cachoerinha.sort_values().values[-1])

# print(melhor_manoa, melhor_armando, melhor_cachoerinha)

melhores_vendedores = pd.DataFrame({
    'loja': ['Manoa', 'Armando Mendes', 'Cachoerinha'],
    'nome':[melhor_manoa[0], melhor_armando[0], melhor_cachoerinha[0]],
    'valor total': [melhor_manoa[1], melhor_armando[1], melhor_cachoerinha[1]]
    })

print(melhores_vendedores)

# data_mv = melhores_vendedores.sort_values(by="valor total")
# plot = data_mv[['valor total', 'nome']].plot(kind='bar')
# fig = plot.get_figure()
# fig.savefig('output_1.png')