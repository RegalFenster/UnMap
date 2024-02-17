import folium
import pandas 
from ast import literal_eval
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex

# Read CSV data
df = pandas.read_csv('data/data.csv')

# Define color map
cmap = plt.cm.get_cmap('RdYlGn')  # Red-Yellow-Green colormap
norm = plt.Normalize(vmin=df['Value'].min(), vmax=df['Value'].max())

# Create a Folium map
my_map = folium.Map(location=(40, 10), zoom_start=10)

# Add markers to the map
for index, row in df.iterrows():
    try:
        coordinates = literal_eval(row['Coordinates'])  # Convert string to tuple
        # Get the population value
        population = float(row['Value'])  # Ensure population is numeric
        color = rgb2hex(cmap(norm(population)))
        # Construct popup content with city name and population
        popup_content = f"{row['City']}<br>Population: {population}"
        folium.CircleMarker(location=[coordinates[0], coordinates[1]], radius=5, color=color, fill=True, fill_color=color, popup=popup_content).add_to(my_map)
    except (ValueError, SyntaxError):
        # Skip rows with malformed or missing coordinates
        pass

# Save and open the map in the default web browser
my_map.save('map.html')
# Manually open the HTML file in the default web browser
webbrowser.open('map.html', new=2)