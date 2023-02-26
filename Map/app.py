import folium
from IPython.display import display

# Set the initial coordinates
latitude = 12.9716
longitude = 77.5946

# Create a map centered on the initial coordinates
m = folium.Map(location=[latitude, longitude], zoom_start=15)

# Add a marker to the map
marker = folium.Marker(location=[latitude, longitude], tooltip='Current Location').add_to(m)

# Display the map
display(m)
