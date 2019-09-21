import pandas as pd
import folium

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
state_geo = f'{url}/us-states.json'

state_data = pd.read_csv("bbs2019.csv")

m = folium.Map(location=[40, -98], zoom_start=4)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Success'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Success Rate (%)'
).add_to(m)

folium.LayerControl().add_to(m)