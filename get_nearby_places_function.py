import requests
def get_nearby_places(location, search, user_rating, number_of_output):
    """
    Returns a specific type of place based on coordinates, search query, user rating, and number of results.

    Args:
    - location (str): Coordinates (latitude,longitude) of the area.
    - search (str): Type of place to search for.
    - user_rating (int/str): Minimum user rating or 'any' for any rating.
    - number_of_output (int): Number of results to retrieve.

    Returns:
    - list: A list of nearby places based on the search criteria.
    """
    google_maps_api_key = 'AIzaSyCqXq0BqIAIojo2IGJKkivABWFNM0fUCYA'
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=1500&type={search}&key={google_maps_api_key}'
    response = requests.get(url)
    try:
        if response.status_code == 200:
            places_data = response.json()
            if user_rating == "any":
                return places_data['results'][:number_of_output]
            elif places_data['results'][0]['rating'] >= user_rating:
                return places_data['results'][:number_of_output]
        else:
            print("Failed to fetch nearby places.")
            return None
    except KeyError as e:
        print("Invalid city / country or search")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None