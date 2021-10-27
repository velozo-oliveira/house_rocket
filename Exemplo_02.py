import pandas as pd
from numpy import float64

data = pd.read_csv('DataSets/kc_house_data.csv/kc_house_data.csv')

# to_datetime funcao para converter a variavel para date
# data ['date'] = pd.to_datetime(data['date'])
#
# print (data['date'])

# Mostrar na tela o tipo de variavel de cada coluna
# print (data.dtypes)

# Como converter variaveis (Int64, float64, string, date) -> funcao .astype
# Remember to set every int as int64 or int 32. Do not Mix!
# data['bedrooms'] = data ['bedrooms'].astype(float64)
# print (data.dtypes)

# Como criar novas variaveis - colunas
# data['Rafael'] = "Rafael"
# data['amazonas'] = pd.to_datetime("9-9-9")
# print (data[['id','amazonas','Rafael']].head())

# Como deletar variaveis
# cols = ['amazonas']
# data = data.drop( cols, axis=1)
# data = data.drop('amazonas', axis=1)
# print (data.columns)

# Como selecionar linhas e colunas
# duplo colchetes: data [['nome da coluna1', 'nome da coluna2']]
# print (data[['date','price']])

# usando a funcao iloc dizendo os indices das linhas e colunas: data.iloc[0:3,0:10]
# print (data.iloc[0:3,0:4])

# selecionando os indices das linhas e os nomes das colunas
# print (data.loc[0:10, ['id','price']])

# Baseado nos indices booleanos
# cols = [True, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
# print(data.loc[0:10,cols])


# 1. Qual a data do imovel mais antigo?
# - Converter o tipo de variavel para data
# - Ordenar em ordem crescente
# print(data.dtypes)
# data['date'] = pd.to_datetime(data['date'])
# print(data['date'].sort_values(ascending=True))

# print((data['date']).min())


# 2. Quantos imoveis possuem o maior numero de andares?
# print(data['floors'].sort_values())
# print (data['floors'].unique())

# new_floors = data[data['floors'] == 3.5]
# print(new_floors[['floors','id']])
# print (new_floors.shape)


# 3. Criar uma classificacao de acordo com o preco do imovel $540,000 (Alto Padrao/ Baixo Padrao)
# data['standard'] = "Level"
# data.loc[data['price'] > 540000, 'standard'] = "High Standard"
# data.loc[data['price'] < 540000, 'standard'] = "Low Standard"
# print(data.head())


# 4. Relatorio ordenado pelo preco
# report = data[['id','date','price','bedrooms','sqft_lot','standard']].sort_values('price',ascending=False)
# print(report.head())
# report.to_csv('DataSets/new_report.csv', index=False)


# 5. Gostaria de um mapa indicando onde as casas estao localizadas
# Plotly - Biblioteca que desenha o mapa
# Scatter Mapbox - Funcao que desenha um mapa

# import plotly.express as px
#
# data_mapa = data[['id','lat','long','price']]
#
# mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long',
#                          hover_name='id', hover_data=['price'],
#                          color_discrete_sequence=['fuchsia'],
#                          zoom=10,
#                          height=300)
#
# # melhorias no mapa - desenhar o layout
# mapa.update_layout(mapbox_style='open-street-map')
# mapa.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0})
# mapa.show()


# 1. Crie uma nova coluna chamada "house_age"
# data['date'] = pd.to_datetime(data['date'])
#
# data['house_age'] = "house_age"
#
# data.loc[data['date'] > '2014-1-1', 'house_age'] = "new house"
# data.loc[data['date'] < '2014-1-1', 'house_age'] = "old house"
#
# print(data[['id','date','house_age']])
#
# print (data[data['house_age'] == 'old house'])


# 2. Crie uma nova coluna chamada "dormitory_type"
# print(data['bedrooms'].unique())
# data['dormitory_type'] = "standard"
# data.loc[data['bedrooms'] == 1, 'dormitory_type'] = "Studio"
# data.loc[data['bedrooms'] == 2, 'dormitory_type'] = "Apartment"
# data.loc[data['bedrooms'] > 2, 'dormitory_type'] = "House"
#
# print(data[['id','bedrooms','dormitory_type']])


# 3. Crie uma nova coluna chamada "condition_type"
# print(data.columns)
# print(data['condition'].unique())
# data['condition_type'] = "Standard"
# data.loc[data['condition'] <= 2, 'condition_type'] = "bad"
# data.loc[(data['condition'] == 3) | (data['condition'] == 4), 'condition_type'] = "regular"
# data.loc[data['condition'] >= 5, 'condition_type'] = "good"
#
# print(data[['id','condition','condition_type']])


# 4. Modifique o tipo da coluna condition para string
# data['condition'] = data['condition'].astype(str)
# print(data.dtypes)


# 5. Deletar as colunas 'sqft_living15' e 'sqft_lot15'
# data = data.drop(['sqft_living15','sqft_lot15'], axis=1)
# print(data.columns)


# 6/7. Modifique o tipo das colunas 'yr_built' e 'yr_renovated' para Date
# data['yr_built'] = pd.to_datetime(data['yr_built'])
# data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])
# print(data.dtypes)


# 8. Qual a data mais antiga da construcao de um imovel
# print (data[['id','yr_built']].sort_values('yr_built'))


# 9. Qual a data mais antiga de renovacao de um imovel
# print((data['yr_renovated'][data['yr_renovated'] > 0]).sort_values(ascending = False))
# print ((data['yr_renovated'][data['yr_renovated'] > 0]).min())


# 10. Quantos imoveis tem 2 andares?
# print(data.columns)
# print((data['floors'][data['floors'] == 2]).shape)


# 11. Quantos imoveis estao com a condicao igual a regular?
# print((data[['id','condition','condition_type']][data['condition_type'] == 'regular']).shape)


# 12. Quantos imoveis estao com condicao igual a 'bad' e possuem 'vista para agua;?
# print (data[['id','condition_type','waterfront']][(data['condition_type'] == 'bad') & (data['waterfront'] == 1)])


# 13. Quantos imoveis estao com a condicao igual a 'good' e sao 'new_house'
# print(data[['id','house_age','condition_type']][(data['house_age'] == 'new house') & (data['condition_type'] == 'good')])


# 14. Qual o valor do imovel mais caro do tipo 'studio'?
# print((data[['id','price','dormitory_type']][data['dormitory_type'] == 'Studio']).sort_values('price'))


# 15. Quantos imoveis do tipo 'apartment' foram reformados em 2015?
# print(data.columns)
# print(data['yr_renovated'].unique())
# print(data.dtypes)
# print(data[['id','yr_renovated']][data['yr_renovated'] == 2015])


# 16. Qual o maior numero de quartos que um imovel do tipo "house" possui?
# print((data[['id','bedrooms','dormitory_type']][data['dormitory_type'] == 'House']).max())


# 17. Quantos imoveis "new house" foram reformados em 2014?
# print(data[['id','house_age','yr_renovated']][(data['yr_renovated'] == 2014) & (data['house_age'] == 'new house')])


# 18. Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo metodo:
# 	18.1 – Direto pelo nome das colunas
# print(data.columns)
# print(data[['id','date','price','floors','zipcode']])

# 	18.2 – Pelos indices
# print(data.columns)
# print(data.iloc[:,[0,1,2,7,16]])

# 	18.3 – Pelos indices das linhas e o nome das colunas
# print(data.loc[:,['id','date','price','floors','zipcode']])

# 	18.4 – Indices booleanos
# cols = [True,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False]
# print(data.loc[:,cols])

# 19. Salve um arquivo .csv com somente as colunas do item 18.
# question_19 = data.loc[:,cols]
# question_19.to_csv('DataSets/answer19.csv', index = False)

# 20. Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”
# import plotly.express as px
#
# data_mapa = data[['id','lat','long','price']]
#
# mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long',
#                          hover_name='id', hover_data=['price'],
#                          color_discrete_sequence=['darkgreen'],
#                          zoom=10,
#                          height=300)
#
# # melhorias no mapa - desenhar o layout
# mapa.update_layout(mapbox_style='open-street-map')
# mapa.update_layout(height = 600, margin = {'r':0, 't':0, 'l':0, 'b':0})
# mapa.show()

