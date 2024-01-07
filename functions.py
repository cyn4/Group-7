"""
This file contains all functions required for the application to run effectively on the main_code
"""

import \
    requests  # Imports the entire requests library, providing functionalities for making HTTP requests to web
# servers or APIs.
import \
    json  # Imports the json library, which includes methods for working with JSON data, such as parsing JSON strings
# into Python data structures and vice versa.
from bs4 import \
    BeautifulSoup  # Imports the BeautifulSoup class specifically from the bs4 module. This syntax allows direct
# access to BeautifulSoup without needing to reference the bs4 module explicitly every time. It's used for HTML
# parsing and navigating HTML or XML documents
import \
    os  # Imports the entire os module, providing functions related to interacting with the operating system. In this


# script, it's specifically used for clearing the console screen, enhancing the user interface of the application


def weather_check(user_city, user_country):
    """
    Checks the weather by passing city and country.

    Args:
    - user_city (str): City for weather check.
    - user_country (str): Country for weather check.

    Returns:
    - str: Weather information based on the user's location.
    """
    api_key = 'c2fa876f2dbb08159882309066d54252'
    endpoint = 'http://api.openweathermap.org/data/2.5/weather'
    user_location = f"{user_city},{user_country}"
    payload = {
        'q': user_location,
        'unit': 'metrics',
        'appid': api_key
    }  # The parameters to be based to the get method
    response = requests.get(url=endpoint, params=payload)
    data = response.json()
    try:  # The try statement ensures the code doesn't break
        conversion = round(
            data['main']['feels_like'] - 273.15)  # This covert the temperature to degree
        if conversion >= 35:  # The 'if' block print a feedback based on the temparature of the user's location
            return (f"The weather is: {conversion}\n🌞 It is sunny in {user_city}, pack a screen 🍶 or pack a Umbrella "
                    f"☂️\n")
        elif conversion >= 20:
            return f"🌥️ The weather is: {conversion}\nNice weather in {user_city}\n "
        if conversion <= 19:
            return f"☃️ The weather is: {conversion}\nIt is very cold in {user_city}\n pack a sweater 🧥 and Gloves🧤\n"
    except KeyError as e:
        print("Invalid city or country")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  # End of the try statement


def direction():
    """
    Provides directions between two locations based on user input.

    Returns:
    - None
    """
    GOOGLE_MAPS_API_KEY = "AIzaSyCqXq0BqIAIojo2IGJKkivABWFNM0fUCYA"
    origin = input("🏨 Where is your intended location: ").lower()
    destination = input("🚘 Where will you like to visit: ").lower()
    mode = input("How will you be commuting? (🚶🏻 Walking,🚘 Driving,🚎 Bus,🚉 Train): ").lower()
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": {GOOGLE_MAPS_API_KEY}
    }  # The parameters to be based to the get method
    response = requests.get(base_url, params=params)
    data = response.json()
    try:  # The try statement ensures the code doesn't break
        duration = data['routes'][0]['legs'][0]['duration']['text']  # Extracting the duration from the Google API
        if mode not in ("walking", "driving", "bus", "train"):  # Checks  if the user inputted the recognized mode
            print("You have entered an invalid mode of transportation")
        else:
            print(f"It will take {duration} to get to {destination}")  # The duration is printed
            direction = data['routes'][0]['legs'][0]['steps']  # Getting the html direction from Google API
            with open('user_directions.json', 'w') as json_file:
                json.dump(direction, json_file, indent=2)  # writing the direction into a json file
            blank_direction = []
            is_direction = input(f"Do you want direction to {destination}?\nType Yes or No: ").lower()
            if is_direction == "yes":
                if len(direction) > 0:  # Check the number of html instruction in the dictionary
                    for i in range(0, len(direction)):
                        blank_direction.append(direction[i]['html_instructions'])  # Appending each html instruction
                        # to a blank list
                    print("Below is your direction:")
                    for i in blank_direction:
                        soup = BeautifulSoup(i,
                                             'html.parser')  # Using BeautifulSoup class to clean the html instruction
                        print(' '.join(
                            soup.stripped_strings))  # printing the cleaned html instruction whilst adding whitespace
                elif len(direction) == 0:
                    soup = BeautifulSoup(direction[0]['html_instructions'], 'html.parser')  # Using BeautifulSoup
                    # class to clean the single html instruction
                    print(
                        f"Below is your direction: \n{' '.join(soup.stripped_strings)}")  # printing the cleaned html instruction whilst adding whitespace
            else:
                print("Safe Travels 🧳✈️")  # If the user doesn't need direction this is printed in console
    except KeyError as e:
        print("Invalid location")
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred: {e}. Try providing location and destination with specific city and country")
        return None  # End of the try statement


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


def get_user_input(): 
    """
    Function to collect user inputs regarding city, country, search query, user rating preference, and number of results to display.

    Returns:
    - tuple: A tuple containing user input values for city, country, search query, user rating, and number of results.
    """
    user_city = input("🌆 What city would you like to check: ").title()  # Prompting for the city of interest
    user_country = input("🌍 What country would you like to check: ").title()  # Prompting for the country of interest
    search = input("🔍 What are you searching for (e.g Hospital): ").lower()  # Prompting for the type of place to search
    user_rating = input("💬 What rating do you want?.\n (Type any if you want all ratings) : ").lower()  # Prompting for the user's rating preference
    number_of_output = int(input("How many of your search results do you want to see: "))  # Prompting for the number of results to display

    # Converting user_rating to int if it's not "any"
    if user_rating != "any":
        user_rating = int(user_rating)

    return user_city, user_country, search, user_rating, number_of_output  # Returning multiple values as a tuple

#clears the terminal to restart the code depending on your device's operating system
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

