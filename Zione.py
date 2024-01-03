def get_location_coordinates(place):
    """
    Accesses the Google Maps API and returns the coordinates of a place.

    Args:
        place (str): The place for which coordinates are to be fetched.

    Returns:
        str: A string containing the latitude and longitude of the place,
              or None if the coordinates could not be found.
    """

    # API key for Google Maps (replace 'YOUR API_KEY' with your actual API key)
    google_maps_api_key = 'YOUR API_KEY'

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


def display_places(places):
    """
    Displays a list of places, ratings, and addresses based on the provided data.

    Args:
        places (list): List of places with details.

    Returns:
        None
    """

    if places:
        print("Places:")

        # Open a text file to store the search results
        with open('user_search.txt', 'a') as text_file:  # 'a' mode for appending
            for idx, place in enumerate(places, start=1):
                # Write the place information to the text file
                text_file.write(f"{idx}. {place['name']}\n")
                text_file.write(f"Rating: {place.get('rating', 'Not rated')}\n")
                text_file.write(f"Address: {place.get('vicinity', 'Address not available')}\n\n")

                # Print the same content to the console
                print(f"{idx}. {place['name']}")
                print("Rating:", place.get('rating', 'Not rated'))
                print("Address:", place.get('vicinity', 'Address not available'))
                print()
    else:
        print("Search not found")