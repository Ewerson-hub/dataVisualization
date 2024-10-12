import pandas as pd
import matplotlib.pyplot as plt

plt.rcdefaults()

data = pd.read_json('dataset.json')

#Relacionando as vendas e as plataformas
vendas_por_plataforma = data.groupby('Plataforma(s)')['Vendas'].sum()

plt.pie(vendas_por_plataforma, labels=vendas_por_plataforma.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das Vendas por Plataforma')
plt.axis('equal')
plt.show()