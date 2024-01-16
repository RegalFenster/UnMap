
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
import pandas
import os 

FILE_PATH = 'data/data.csv'

# Get the absolute path to the CSV file
csv_file_path = os.path.join(os.getcwd(), FILE_PATH)

# Read the CSV file into a DataFrame
data = pandas.read_csv(csv_file_path)

# Geocoding setup
geolocator = Nominatim(user_agent="UnMap")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Initialize a list to store new values
locations = []

# Get geo location
for city in data.City:
        try:
            location = geocode(city)
            locations.append((location.latitude, location.longitude))
            print(f"{city}: Latitude {location.latitude}, Longitude {location.longitude}")
        except Exception as e:
            locations.append(None)
            print(f"Error geocoding {city}")

# Add locations to data
data['Coordinates'] = locations
data.to_csv(csv_file_path, index=False)


