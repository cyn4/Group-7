"""
This file contains all functions required for the application to run effectively on the main_code
Functions: get_location_coordinates,log_coordinates, display_places, get_nearby_places, 
get_user_input, weather_check, direction,clear_console

import requests:
-->Imports the entire requests library, providing functionalities for making HTTP requests to web servers or APIs.

import json:
-->Imports the json library, which includes methods for working with JSON data, such as parsing JSON strings into Python 
data structures and vice versa.
-Allows us to send and receive data in JSON format.

from bs4 import BeautifulSoup:
-->Imports the BeautifulSoup class specifically from the bs4 module. 
-This syntax allows direct access to BeautifulSoup without needing to reference the bs4 module explicitly every time.
-It's used for HTML parsing and navigating HTML or XML documents

import os:
-->Imports the entire os module, providing functions related to interacting with the operating system.

from dotenv import load_dotenv:
-->Dotenv is a zero-dependency module that loads these environment variables from a .env file into your Node.js application. 
-Its designed to work with any platform and supports loading environment variables directly from a .env file or from an object.
-The above statement imports the load_dotenv function.
-->load_dotenv() is a method that loads values from .env files into the environment variables.

"""

import requests 
import json 
from bs4 import BeautifulSoup 
from dotenv import load_dotenv
import os  


# load .env file
load_dotenv()
#Get the Google Maps API key from the environment variables
google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY_PLACES')
google_maps_api_key = os.getenv('GOOGLE_MAPS_API_COORDINATES')
weather_api_key = os.getenv('WEATHER_API_KEY')

def weather_check(user_city, user_country):
    """
    Checks the weather by passing city and country.

    Args:
    - user_city (str): City for weather check.
    - user_country (str): Country for weather check.

    Returns:
    - str: Weather information based on the user's location.
    """
    weather_api_key = os.getenv("WEATHER_API_KEY")
    endpoint = 'http://api.openweathermap.org/data/2.5/weather'
    user_location = f"{user_city},{user_country}"
    payload = {
        'q': user_location,
        'unit': 'metrics',
        'appid': weather_api_key
    }  # The parameters to be based to the get method
    response = requests.get(url=endpoint, params=payload)
    data = response.json()
    try:  # The try statement ensures the code doesn't break
        conversion = round(
            data['main']['feels_like'] - 273.15)  # This covert the temperature to degree
        if conversion >= 35:  # The 'if' block print a feedback based on the temparature of the user's location
            return (f"The weather is: {conversion}°\n🌞 It is sunny in {user_city}, pack a sun screen 🍶 or pack a "
                    f"Umbrella"
                    f"☂️\n")
        elif conversion >= 20:
            return f"🌥️ The weather is: {conversion}°\nNice weather in {user_city}, let you hair out💃🏻 "
        if conversion <= 19:
            return f"☃️ 🥶 The weather is: {conversion}°\nIt is very cold in {user_city} pack a sweater 🧥 and Gloves🧤\n"
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
    origin = input("🏨 Where is your intended location: ").lower()
    destination = input("🚘 Where will you like to visit: ").lower()
    mode = input("How will you be commuting? (🚶🏻 Walking,🚘 Driving,🚎 Bus,🚉 Train): ").lower()
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": {google_maps_api_key}
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
    
def get_location_coordinates(place):
    """
    This function accesses the Google Maps API and returns the coordinate of a place.
    It uses the 'requests' library to send a GET request to the Google Maps API.
    """
    # Build the Google Maps API url

    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={google_maps_api_key}' 

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
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=1500&type={search}&key={google_maps_api_key}'
    response = requests.get(url)
    try:
        if response.status_code == 200:
            places_data = response.json()
            if user_rating == "any":
                return places_data['results'][:number_of_output]
        #     elif places_data['results'][0]['rating'] >= user_rating:
        #         return places_data['results'][:number_of_output]
            else:
                filtered_places = [
                    place for place in places_data['results'] if
                    'rating' in place and place.get('rating', 0) >= user_rating
                ]  # Due to the nature of the json file we are using a list comprehension to carry out the filtration
                return filtered_places[:number_of_output]
        else:
            print("Failed to fetch nearby places.")
            return None
    except KeyError:
        print("Invalid city / country or search.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
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


def display_nearby_places(places):  
    """
    Displays a list of places, ratings, and addresses based on the provided data.

    Args:
    - places (list): List of places with details.

    Returns:
    - None
    """
    if places:
        print("\nNearby Places:")
        with open('user_search.txt', 'w', encoding='utf-8') as text_file:
            for idx, place in enumerate(places, start=1):
                text_file.write(f"{idx}. {place['name']}\n")
                text_file.write(f"Rating: {place.get('rating', 'Not rated')}\n")
                text_file.write(f"Address: {place.get('vicinity', 'Address not available')}\n\n") #places are extracted into a text file
                # Printing the same content to the console
                print(f"{idx}. {place['name']}")
                print("Rating:", place.get('rating', 'Not rated'))
                print("Address:", place.get('vicinity', 'Address not available'))
                print()
    else:
        print("Search not found")

def clear_console():
    '''Function clears the terminal to restart the code 
    depending on your device's operating system
    enhancing the user interface of the application
    '''
    os.system('cls' if os.name == 'nt' else 'clear')




def discover_more_places(): #Aishat
    print(places)
    user_city, user_country, search, user_rating, number_of_output = get_user_input()
    place = user_city, user_country
    location = get_location_coordinates(place)  # Getting coordinates for the user's location
    # Displaying weather information for the user's location
    print(weather_check(user_city, user_country))
    # Getting and displaying nearby places based on user's input
    nearby_places = get_nearby_places(location, search, user_rating, number_of_output)
    return display_nearby_places(nearby_places)


def discover_places_service():
    """
    Function to handle discovering places based on user input.

    This function asks the user if they want to discover other places and continues the discovery process
    until the user decides not to discover more.

    Returns:
    - None
    """
    discover = True
    while discover:
        clear_console()
        discover_more_places()
        is_more_places = input("Will you like to discover other places ( Type yes or No):  ").lower()
        if is_more_places == "yes":
            clear_console()
        elif is_more_places == "no":
            break


def push_navigation_services(): 
    """
    Function to prompt the user about exploring the navigation service.

    Returns:
    - str: User's choice ('Yes' or 'No')
    """
    navigation_push = input("Hey🙋🏻‍♀️! before you go, will you love to check out our Navigation "
                            "service.\n Type Yes or No: ").lower()
    return navigation_push


def more_navigation_service(): 
    """
    Function to ask the user if they want navigation services for other destinations.

    Returns:
    - str: User's choice ('Yes' or 'No')
    """
    more_navigation = input("\nDo you want navigation services for other destinations.\nType Yes or No: ").lower()
    return more_navigation


def navigation_services(): 
    """
    Function to orchestrate the navigation service.

    This function manages the navigation service by asking users if they want to discover new places in a destination.
    It also runs the directions functions.
    It gathers user preferences like the type of place to search for, the rating preference, and the number of results
    to display. It uses these preferences to fetch and display nearby places.

    Returns:
    - None
    """
    navigation = True
    while navigation:
        clear_console()
        print(navigation_art)
        destination_country, destination_city = direction()
        activate_place_discovery_push = True
        while activate_place_discovery_push:
            push_place_discovery_service = input(
                "\nDo you want to discover new or more places in this destination?\n Type Yes or "
                "No: ").lower()
            if push_place_discovery_service == "yes":
                clear_console()
                print(places)
                place = destination_city, destination_country
                location = get_location_coordinates(place)
                search = input(
                    "🔍 What are you searching for (e.g Hospital): ").lower()  # Prompting for the type of place to
                # search
                user_rating = input(
                    "💬 What rating do you want?.\n(Type any if you want all ratings, otherwise give a number between ("
                    "1-4) : ").lower()  # Prompting
                # for the user's rating preference
                number_of_output = int(
                    input("How many of your search results do you want to see: "))  # Prompting for the number
                # of results to display

                # Converting user_rating to int if it's not "any"
                if user_rating != "any":
                    user_rating = float(user_rating)
                nearby_places = get_nearby_places(location, search, user_rating, number_of_output)
                display_nearby_places(nearby_places)
            elif push_place_discovery_service == "no":
                break
        if more_navigation_service() == "no":
            break


def app_exit(): 
    """
    Function to ask the user if they want to exit the app.

    Returns:
    - str: User's choice ('Yes' or 'No')
    """
    exit = input("Do you want to exit app. Type Yes or No:  ").lower()
    return exit




