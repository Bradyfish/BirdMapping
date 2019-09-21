import pandas as pd
import folium
import glob

statelatlongs = pd.read_csv("statelatlong.csv")

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
state_geo = f'{url}/us-states.json'
state_data = pd.read_csv("easternbluebirds.csv")
treeswallowdata = pd.read_csv("treeswallows.csv")

m = folium.Map(location=[40, -98], zoom_start=4)

folium.Choropleth(
    geo_data=state_geo,
    name='Eastern Bluebirds',
    data=state_data,
    columns=['State', 'Success'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Success Rate (%)'
).add_to(m)

folium.Choropleth(
    geo_data=state_geo,
    name='Tree Swallows',
    data=treeswallowdata,
    columns=['State', 'Success'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Success Rate (%)'
).add_to(m)

lats = statelatlongs["Latitude"]
longs = statelatlongs["Longitude"]
names = statelatlongs["State"]


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


fg = folium.FeatureGroup(name='Info')
for lat, lon, name in zip(lats, longs, names):
    html = f"""
    <img src="WY.png">
    """
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=html, radius=4, fill=True, color='black'))
m.add_child(fg)


folium.LayerControl().add_to(m)


m.save("index.html") #Saves the map as an html file