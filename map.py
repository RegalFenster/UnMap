import folium
import pandas as pd
from ast import literal_eval
import webbrowser

# Read CSV data
df = pd.read_csv('data/data.csv')

# Create a Folium map
my_map = folium.Map(location=("40","10"), zoom_start=10)

# Add markers to the map
for index, row in df.iterrows():
    try:
        coordinates = literal_eval(row['Coordinates'])  # Convert string to tuple
        folium.Marker([coordinates[0], coordinates[1]], popup=f"{row['City']},{row['Value']}").add_to(my_map)
    except (ValueError, SyntaxError):
        # Skip rows with malformed or missing coordinates
        pass

# Save and open the map in the default web browser
my_map.save('map.html')
# Manually open the HTML file in the default web browser
webbrowser.open('map.html', new=2)