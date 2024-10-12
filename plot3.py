import pandas as pd
import matplotlib.pyplot as plt
import re as regex

plt.rcdefaults()
data = pd.read_json('dataset.json')

#extraindo somente os anos da data de lançamento
data['Lançamento inicial'] = data['Lançamento inicial'].apply(lambda x: ''.join(regex.findall(r"\d{4}", x)))

#Ordenando os dados por lançamento de forma crescente
data = data.sort_values(by='Lançamento inicial')

plt.plot(data['Lançamento inicial'], data['Vendas'], marker="o", ls=':')

#Nomeado cada ponto do plot
for i, info in data.iterrows():
    plt.annotate(info.Titulo, (info['Lançamento inicial'],info['Vendas']),textcoords='offset points',xytext=(0,8), ha='center',fontsize=9)

plt.title('Relação entre os jogos mais vendidos e seu ano de lançamento')
plt.ylabel('Vendas(em unidade de milhão)')
plt.xlabel('Ano de Lançamento')

plt.tight_layout()
plt.show()