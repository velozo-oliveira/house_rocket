

# carregue o conjunto de dados chamado kc_house_data.csv do HD para a memoria
import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv/kc_house_data.csv')

# 1. Quantas casas estao disponiveis para compra?
# print("O numero de casas e {}".format(len(data['id'].unique())))

# 2. Quantos atributos as casas possuem?
# # print(data.shape)
# # print(data.shape[1])
# print(len(data.columns.tolist()))

# 3. Quais sao os atributos das casas?
# print (data.columns)

# 4. Qual a casa mais cara?
# print(data.head())
# print ( data[['id','price']].sort_values('price', ascending=False).reset_index(drop=True).loc[0,'id'])

# mostrar na tela o id e valor das casas mais caras em ordem decrescente
# print ( data[['id','price']].sort_values('price', ascending=False))

# 5. Qual a casa com o maior numero de quartos?
# print ( data[['id','bedrooms']].sort_values('bedrooms'))

# 6. Qual a soma total de quartos do conjunto de dados?
# bedrooms_n = data['bedrooms'].sum()
# print (bedrooms_n)
# bedrooms_n = sum(data.bedrooms)
# print (bedrooms_n)

# mostrar na tela o id e numero de banheiros das casas
# print ( data[['id','bathrooms']].sort_values('bathrooms'))

# 7. Quantas casas possuem 2 banheiros?
# print (sum(data['bathrooms']==2))
# print( (list(data.bathrooms)).count(2))
# print ((data[['id','bathrooms']][data['bathrooms']==2]).shape[0])
# print (data[['id','bathrooms']][data['bathrooms']==2])

# print(data.loc[data['bathrooms']==2,['id','bathrooms']])

# 8. Qual o preco medio das casas do conjunto de dados?
# print (int(data['price'].mean()))

# 9. Qual o preco medio das casas com 2 banheiros
# print (((data[['price','bathrooms']][data['bathrooms']==2])).mean())
# print (data.loc[data['bathrooms'] == 2,'price'].mean())

# 10. Qual o preco minimo entre as casas com 3 quartos?
# print ((data[['price','bedrooms']][data['bedrooms']==3].min()))

# minumum_price_bedrooms_three = (data[['bedrooms','price']].loc[data['bedrooms'] == 3]).sort_values('price')
# print (minumum_price_bedroom_three)

# minimum_price_bedrooms_three = data.loc[data['bedrooms'] == 3,'price'].min()
# print (minimum_price_bedrooms_three)

# 11. Quantas casas possuem mais de 300 m2 na sala de estar?
# sq_ft = data[data['sqft_living'] > 3229.17]
# print(sq_ft[['id','sqft_living']])

# data['m2_living'] = data['sqft_living']*0.0929
# print (data[['id','m2_living']][data['m2_living'] > 300])

# 12. Quantas casas possuem mais de 2 andares?
# floor_number = data.loc[data['floors'] > 2]
# print(floor_number[['id','floors']])

# print (data[data['floors'] > 2].shape)

# 13. Quantas casas tem vista para o mar?
# sea_view = data.loc[data['waterfront'] == 1]
# print(sea_view[['id','waterfront']])

# print(data[['id','waterfront']][data['waterfront'] == 1])

# 14. Das casas com vista para o mar, quantas tem 3 quartos?
# sea_v_bedroom_three = sea_view.loc[sea_view['bedrooms'] == 3]
# print (sea_v_bedroom_three[['id','bedrooms']])

# print ((data[(data['waterfront'] == 1) & (data['bedrooms'] == 3)]).shape)

# 15. Das casas com mais de 300 m2 de sala de estar, quantas tem mais de 2 banheiros?
# bath_two_sq_ft_three_h = sq_ft.loc[sq_ft['bathrooms'] > 2]
# print (bath_two_sq_ft_three_h[['id','sqft_living','bathrooms']])

# print(data[['bathrooms','m2_living']][(data['m2_living'] > 300) & (data['bathrooms'] > 2)])
