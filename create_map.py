import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
v_name = list(data["NAME"])
fg = folium.FeatureGroup(name='my_map')

for lt,ln,n in zip(lat,lon,v_name):
    fg.add_child(folium.Marker(location=[int(lt), int(ln)], popup=n, icon=folium.Icon(color='red')))

map = folium.Map(location=[47.645260156417585, -
                 122.32721740454191], zoom_start=6)




map.add_child(fg)
map.save('Map1.html')
