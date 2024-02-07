from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
import pandas as pd
import os

FILE_PATH = 'data/data.csv'

# Get the absolute path to the CSV file
csv_file_path = os.path.join(os.getcwd(), FILE_PATH)

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Geocoding setup
geolocator = Nominatim(user_agent="UnMap")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Initialize a list to store new values
locations = []

# Get geo location
for index, row in data.iterrows():
    city = row['City']
    country = row['Country or Area']  
    location_info = f"{city}, {country}"

    try:
        location = geocode(location_info)
        if location:
            locations.append({'Coordinates': (location.latitude, location.longitude)})
            print(f"{location_info}: Latitude {location.latitude}, Longitude {location.longitude}")
    except Exception as e:
        locations.append(None)
        print(f"Error geocoding {location_info}: {e}")

# Add locations to data
data['Coordinates'] = locations
data.to_csv(csv_file_path, index=False)