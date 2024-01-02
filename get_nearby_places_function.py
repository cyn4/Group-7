import requests

def get_nearby_places(location, search, user_rating, number_of_output):
    """
    Function to get nearby places using Google Places API.
    
    :param location: String, the latitude and longitude of the location.
    :param search: String, the type of place to search for.
    :param user_rating: String, filter the places by minimum user rating.
    :param number_of_output: Integer, the maximum number of places to return.
    
    :return: List of nearby places based on the provided filters.
    """
    google_maps_api_key = 'AIzaSyCqXq0BqIAIojo2IGJKkivABWFNM0fUCYA'
    
    # Build the API URL with the provided parameters
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=1500&type={search}&key={google_maps_api_key}'
    
    # Send a GET request to the API URL
    response = requests.get(url)
    
    try:
        # Check if the request was successful
        if response.status_code == 200:
            places_data = response.json()
            
            # If the user has specified "any" for user_rating, return all nearby places
            if user_rating == "any":
                return places_data['results'][:number_of_output]
            
            # If the user has specified a minimum user rating, return only the places with a rating greater than or equal to the specified value
            elif places_data['results'][0]['rating'] >= user_rating:
                return places_data['results'][:number_of_output]
        
        # If the request was not successful, print an error message
        else:
            print("Failed to fetch nearby places.")
            return None
    
    # Handle KeyError and other exceptions
    except KeyError as e:
        print("Invalid city / country or search")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None