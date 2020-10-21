import pandas as pd


def to_double(object):
    string = object.replace("R$", "")
    string = string.replace(",", "")
    double = float(string)
    return double


def rank_lojas(string):
    loja = data_compressed.loc[string]
    rank_loja = loja.dropna()
    return rank_loja


def nome_melhor_vendedor(object):
    nome = object.sort_values().index[-1]
    return nome[1]


def total_vendas_melhor_vendedor(object):
    return object.sort_values().values[-1]


def melhor_da_filial(object):
    return (nome_melhor_vendedor(object), total_vendas_melhor_vendedor(object))



data = pd.read_csv("data/data.csv")

data = data[['Filial', 'nome', 'valor_compra']]
data["valor_compra"] = data["valor_compra"].map(to_double)
data_compressed = data.pivot_table(index='Filial', columns='nome', aggfunc=sum)

data_manoa = rank_lojas('Loja Manoa')
data_armando_mendes = rank_lojas('Loja Armando Mendes')
data_cachoerinha = rank_lojas('Loja Cachoerinha')

melhor_manoa = melhor_da_filial(data_manoa)
melhor_armando = melhor_da_filial(data_armando_mendes)
melhor_cachoerinha = melhor_da_filial(data_cachoerinha)


melhores_vendedores = pd.DataFrame({
    'nome':[melhor_manoa[0], melhor_armando[0], melhor_cachoerinha[0]],
    'valor total': [melhor_manoa[1], melhor_armando[1], melhor_cachoerinha[1]]
    }, index=['Loja Manoa', 'Loja Armando Mendes', 'Loja Cachoerinha'])

print(melhores_vendedores)

#erro ao plotar corretamente
# data_mv = melhores_vendedores.sort_values(by="valor total")
# plot = data_mv['valor total'].plot(kind='bar', ylabel="Total de vendas em R$", legend=True)
# fig = plot.get_figure()
# fig.savefig('output_1.png')