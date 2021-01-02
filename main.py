'''
Covid Mapper
---------------
Adam Byrne 2021
'''
import pandas as pd
import plotly.express as px

url = 'https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D'
df = pd.read_csv(url)
fig = px.scatter(df, y = 'ConfirmedCovidCases', x = 'FID', opacity=0.6, title='Covid Cases in Ireland', trendline="lowess")
fig.show()