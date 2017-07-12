#map stuff
import folium
#math stuff
import pandas

#read in a csv of lat, long, and other column data - currently city,state,latitude,longitude,timezone,dst,zipcode
df=pandas.read_csv("ZipLatLongTest.csv")

#define a map, set the location of the map to the means of the lats and longs, choose a texture layer (alt: mapboxbright)
map=folium.Map(location=[df["latitude"].mean(),df["longitude"].mean()],zoom_start=12,tiles="openstreetmap")

#Create a set of locations
fg=folium.FeatureGroup(name="Zipcode Locations")

#Add a marker for each location and give it a name. 
for lat,lon,name,zipNum in zip(df["latitude"],df["longitude"],df["city"],df["zipcode"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(str(zipNum).zfill(5))),icon=folium.Icon(icon_color="blue")))

#append the locations to the map
map.add_child(fg)

#append the Census polygon data to the map.
map.add_child(folium.GeoJson(data=open("2016CensusZipDemo.geojson"), name="Delivery Areas"))

#use Folium's LayerControl function to toggle layers
map.add_child(folium.LayerControl())

#save the thing
map.save(outfile="ZipDemo.html")
