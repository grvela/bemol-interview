import pandas as pd


def to_double(object):
    string = object.replace("R$", "")
    string = string.replace(",", "")
    double = float(string)
    return double



data = pd.read_csv("data/data.csv")

data = data[['Filial', 'nome', 'valor_compra']]

data["valor_compra"] = data["valor_compra"].map(to_double)

print(data)

data_compressed = data.pivot_table(index='Filial', columns='nome', aggfunc=sum)

print(data_compressed)

manoa = data_compressed.loc['Loja Manoa']

print(manoa)

manoa = manoa.dropna()

print(manoa.sort_values()) #esse aqui é o que mais vendeu
