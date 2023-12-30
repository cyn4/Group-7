import requests
def get_location_coordinates(place):
    """
    This function access the Google map API and returns a coordinate of a place
    """
    google_maps_api_key = 'AIzaSyCqXq0BqIAIojo2IGJKkivABWFNM0fUCYA'  # API key
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={google_maps_api_key}'  # google
    # map url place here is the variable passed into the url
    response = requests.get(url)
    if response.status_code == 200:
        location_data = response.json()
        if location_data['results']:  # accessing the result key in the data dictionary
            location = location_data['results'][0]['geometry']['location']
            return f"{location['lat']},{location['lng']}"  # returns the longitude and latitude
        else:
            print("Location not found.")
            return None
    else:
        print("Failed to fetch location data.")
        return None
