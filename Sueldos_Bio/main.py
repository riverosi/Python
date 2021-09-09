import folium

#def add_marker(price, position)

m = folium.Map(
    width=700,
    height=700,
    location=[-38.416097, -63.616672],
    zoom_start=4,
    zoom_control=True)
	
folium.Marker(
    location=[-34.61315, -58.37723],
    tooltip = "<i>$77300 , 6 personas</i>",
    popup="Min: $50000 \n Max: $80000",
).add_to(m)

folium.Marker(
    location=[-31.4135, -64.18105],
    tooltip = "$67300 , 1 personas</i>",
    popup="Min: $53500 \n Max: $72300",
).add_to(m)

folium.LayerControl().add_to(m)

m.save("map.html")