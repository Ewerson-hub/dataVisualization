import pandas as pd
import matplotlib.pyplot as plt

plt.rcdefaults()
data = pd.read_json('dataset.json')

#ordenando os dados do maior para o menor de acordo com as Vendas
data.sort_values(by='Vendas', ascending=False)
#convertendo as vendas em unidade de milhão
data['Vendas'] = data['Vendas'].apply(lambda x: int(x / 1000000))


#Plot 1
plt.bar(data['Titulo'], data['Vendas'])

plt.ylabel('Vendas( em unidade de milhão)')
plt.title('Jogos Mais Vendidos')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()