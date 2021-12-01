import pandas as pd
import streamlit as st
import numpy as np
import folium
import plotly.express as px
import geopandas

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)
    return geofile

def set_feature (data):
    data = data.drop_duplicates(subset=['id'], keep='last')
    data['Price_m2'] = data['price'] / data['sqft_lot']
    return data

def overview_data (data):
    f_attributes = st.sidebar.multiselect('Enter columns: ', data.columns)
    f_zip_code = st.sidebar.multiselect('Enter ZipCode: ', data['zipcode'].unique())

    st.title('Data Overview')
    data_metrics = data.copy()

    # FILTROS
    # attributes + zipcode = Selecionar Colunas e linhas
    # attributes = Selecionar colunas
    # zipcodes = Selecionar Linhas
    # 0 + 0 = Retorno o dataset original

    if (f_attributes != []) & (f_zip_code != []):
        data = data.loc[data['zipcode'].isin(f_zip_code), f_attributes]

    elif (f_zip_code != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zip_code), :]

    elif (f_attributes != []) & (f_zip_code == []):
        data = data.loc[:, f_attributes]

    else:
        data = data.copy()

    st.dataframe(data)

    # Average Metrics
    df1 = data_metrics[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data_metrics[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data_metrics[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data_metrics[['Price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()

    # merge
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQRT LIVING', 'PRICE/M2']

    st.header('Metrics')
    st.dataframe(df, height=600)

    # Statistic Descriptive
    num_attributes = data.select_dtypes(include=['int64', 'float64'])
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))

    max_ = pd.DataFrame(num_attributes.apply(np.max))
    min_ = pd.DataFrame(num_attributes.apply(np.min))

    df1 = pd.concat([max_, min_, media, mediana, std], axis=1).reset_index()
    df1.columns = ['Attributes', 'Max', 'Min', 'Average', 'Median', 'Std']
    df1 = df1.drop(labels=0, axis=0)
    st.header('Descriptive Analysis')
    st.dataframe(df1, height=600)

    return None

def portfolio_density(data,geofile):
    st.title('Region Overview')
    c1, c2 = st.columns((1, 1))
    c1.header('Portfolio Density')

    df = data.sample(10)

    # Base Map - Folium
    density_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                             defaut_zoom_start=15)

    marker_cluster = MarkerCluster().add_to(density_map)
    for name, row in df.iterrows():
        folium.Marker([row['lat'], row['long']],
                      popup='Sold Price ${0} on {1}. Features: '
                            '{2} sqft, '
                            '{3} bedrooms,'
                            '{4} bathrooms, '
                            'year built: {5}'
                      .format(row['price'],
                              row['date'],
                              row['sqft_living'],
                              row['bedrooms'],
                              row['bathrooms'],
                              row['yr_built'])).add_to(marker_cluster)

    with c1:
        folium_static(density_map)

    # Region Price Map

    c2.header('Price Density')

    df = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()

    df.columns = ['ZIP', 'PRICE']

    geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]
    region_price_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                                  defaut_zoom_start=15)

    region_price_map.choropleth(data=df,
                                geo_data=geofile,
                                columns=['ZIP', 'PRICE'],
                                key_on='feature.properties.ZIP',
                                fill_color='YlOrRd',
                                fill_opacity=0.7,
                                line_opacity=0.2,
                                legend_name='AVG PRICE'
                                )
    with c2:
        folium_static(region_price_map)

    return None

def commercial_distribution(data):
    st.sidebar.title('Commercial Options')
    st.title('Commercial Attributes')

    # -------------- Average Price per Year

    # Filters
    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())

    st.sidebar.subheader('Select Max Year Built')
    f_year_built = st.sidebar.slider('Year Built', min_year_built,
                                     max_year_built,
                                     min_year_built)

    st.header('Average Price per Year Built')

    # Data selection
    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    # plot
    fig = px.line(df, x='yr_built', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # # -------------- Average Price per Year

    st.header('Average Price per Year Day')
    st.sidebar.subheader('Select Max Date')

    # Filters
    data['date'] = (pd.to_datetime(data['date']).dt.date)

    min_date = ((pd.to_datetime(data['date'])).dt.date).min()
    max_date = ((pd.to_datetime(data['date'])).dt.date).max()

    f_date = st.sidebar.slider('Date', min_date,
                               max_date,
                               min_date)

    # Data filtering
    df = data.loc[data['date'] < f_date]
    df = df[['date', 'price']].groupby('date').mean().reset_index()

    # plot
    fig = px.line(df, x='date', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # # ----------- Histogram
    st.header('Price Distribution')
    st.sidebar.subheader('Select Max Price')

    # filter
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price)
    df = data.loc[data['price'] < f_price]

    # data plot
    fig = px.histogram(df, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

    return None

def attributes_distribution(data):
    st.sidebar.title(('Attributes Options'))
    st.title('House Attributes')

    # filters
    f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', sorted(set(data['bedrooms'].unique())))

    # House per bedrooms
    st.header('Houses per bedrooms')
    df = data[data['bedrooms'] < f_bedrooms]
    fig = px.histogram(df, x='bedrooms', nbins=19)
    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == '__main__':
    # ETL - Extraction
    path = 'kc_house_data.csv'
    data = get_data(path)
    url = 'https://data-seattlecitygis.opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    geofile = get_geofile(url)


    # ETL - Transformation
    data = set_feature(data)
    overview_data(data)
    portfolio_density (data,geofile)
    commercial_distribution(data)
    attributes_distribution(data)