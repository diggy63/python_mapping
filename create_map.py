import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")

lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])
name = list(data["NAME"])


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[47.645260156417585, -
                 122.32721740454191], zoom_start=6)
fg = folium.FeatureGroup(name = "My Map")

def colorElev(el):
    if el < 1000:
        return "green"
    elif el > 1000 and el < 3000:
        return "orange"
    else:
        return "red"
 
for lt, ln, el, name in zip(lat, lon, elv, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    el_color = colorElev(el)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius = 6, fill_color=el_color, color="grey", fill_opacity = 0.7))


fg.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.save('Map1.html')
