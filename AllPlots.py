import pandas as pd
import matplotlib.pyplot as plt
import re as regex

plt.rcdefaults()
data = pd.read_json('dataset.json')


def pointPlot(data):
    #extraindo somente os anos da data de lançamento
    data['Lançamento inicial'] = data['Lançamento inicial'].apply(lambda x: ''.join(regex.findall(r"\d{4}", x)))

    #Ordenando os dados por lançamento de forma cescente
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
def pizzaPlot(data):
    vendas_por_plataforma = data.groupby('Plataforma(s)')['Vendas'].sum()

    plt.pie(vendas_por_plataforma, labels=vendas_por_plataforma.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição das Vendas por Plataforma')
    plt.axis('equal')
    plt.show()
def barPlot(data) :
    # ordenando os dados do maior para o menor de acordo com as Vendas
    data.sort_values(by='Vendas', ascending=False)

    # convertendo as vendas em unidade de milhão
    data['Vendas'] = data['Vendas'].apply(lambda x: int(x / 1000000))

    plt.bar(data['Titulo'], data['Vendas'])
    plt.xticks(rotation=45, ha='right')

    plt.ylabel('Vendas( em unidade de milhão)')
    plt.title('Jogos Mais Vendidos')


    plt.tight_layout()
    plt.show()



barPlot(data)
pizzaPlot(data)
pointPlot(data)


