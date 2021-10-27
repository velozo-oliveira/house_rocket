# how to decide if we are buying a house or not

import pandas as pd

data = pd.read_csv('DataSets/kc_house_data.csv/kc_house_data.csv')

# we will group houses prices based on their location


df = data[['price','waterfront']].groupby('waterfront').mean().reset_index()
df.rename(columns={'price':'median_price'},inplace=True)

df2 = pd.merge(data,df,on='zipcode',how='inner')

for i in range(len(data)):
    if ((df2.loc[i,'price']) <= (df2.loc[i,'median_price'])) & (df2.loc[i,'condition'] > 2):
        df2['status'] = 'Comprar'
    elif: df2['status'] = 'Nao Comprar'

print(df2.loc[0:20,['id','price','zipcode','median_price','status']])