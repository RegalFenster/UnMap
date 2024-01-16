import pandas as pd
import folium

# Read the CSV file with city names and coordinates
df = pd.read_csv('data/data.csv')  # Replace 'your_file.csv' with your actual file path

# Create a Folium map centered at an initial location
map_center = [df['Coordinates'].apply(lambda x: x[0]).mean(), df['Coordinates'].apply(lambda x: x[1]).mean()]  # Adjust the center as needed
mymap = folium.Map(location=map_center, zoom_start=4)

# Add markers for each city
for index, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['City']).add_to(mymap)

# Save the map as an HTML file or display it
mymap.save('map.html')
# OR
# mymap
