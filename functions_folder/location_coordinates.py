import requests
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()
#Get the Google Maps API key from the environment variables
google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY_PLACES ')

def get_location_coordinates(place):
    """
    This function accesses the Google Maps API and returns the coordinate of a place.
    It uses the 'requests' library to send a GET request to the Google Maps API.
    """
    # Build the Google Maps API url

    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={google_maps_api_key}' # Google Maps API url

    # Send a GET request to the Google Maps API
    response = requests.get(url)

    # Check if the GET request was successful (HTTP status code 200)
    if response.status_code == 200:
        location_data = response.json()

        # Check if the 'results' key exists in the location data
        if location_data['results']: # accessing the result key in the data dictionary
            location = location_data['results'][0]['geometry']['location']
            longitude = f"{location['lat']}"
            latitude = f"{location['lng']}"
            coordinates=f"{location['lat']},{location['lng']}"
            log_coordinates(place, longitude,latitude)
            # Return the longitude and latitude as a formatted string
            return coordinates
             
        else:
            print("Location not found.")
            return None
    else:
        print("Failed to fetch location data.")
        return None
def log_coordinates(place, longitude,latitude):
    """
    This function logs the coordinates (latitude and longitude) of a place to a text file.
    Each line in the file will contain the place and its coordinates.
    """
    # Open a text file in append mode or create it if it doesn't exist
    with open('coordinates_log.txt', 'a') as file:
        # Write the place and its coordinates to the file
        file.write(f"{place}  Longitude: {longitude}, Latitude: {latitude} \n")

get_location_coordinates('kenya, mombasa')
