def get_location_coordinates(place):
    """
    Accesses the Google Maps API and returns the coordinates of a place.

    Args:
        place (str): The place for which coordinates are to be fetched.

    Returns:
        str: A string containing the latitude and longitude of the place,
              or None if the coordinates could not be found.
    """

    # API key for Google Maps 
    google_maps_api_key = 'AIzaSyCqXq0BqIAIojo2IGJKkivABWFNM0fUCYA'

    # Construct the API URL with the provided place and API key
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={google_maps_api_key}'

    # Send a GET request to the Google Maps API URL
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        location_data = response.json()

        # Check if the response contains results
        if location_data['results']:
            # Extract the latitude and longitude from the first result
            location = location_data['results'][0]['geometry']['location']
            return f"{location['lat']},{location['lng']}"  # Return coordinates as a string
        else:
            print("Location not found.")
            return None
    else:
        print("Failed to fetch location data.")
        return None
