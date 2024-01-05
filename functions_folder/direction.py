def direction():
    """
    Provides directions between two locations based on user input.

    Returns:
    - None
    """
    # Retrieve API key from environment variable
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY_PLACES") 
    # Gather user input for destination and travel preferences
    destination_country = input("What country is the destination?: ").lower()
    destination_city = input("What city is the destination").lower()
    origin = input("🏨 Where is your location: ").lower()
    destination = input("🚘 Where is the destination: ").lower()
    mode = input("How will you be commuting? (🚶🏻 Walking,🚘 Driving,🚎 Bus,🚉 Train): ").lower()
    # Construct the URL for the Google Maps Directions API
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": {GOOGLE_MAPS_API_KEY}
    }  # The parameters to be passed to the get method
     # Send request to the API and parse the response
    response = requests.get(base_url, params=params)
    data = response.json()
    try:  # The try statement ensures the code doesn't break
        duration = data['routes'][0]['legs'][0]['duration']['text']  # Extracting the duration from the Google API
        if mode not in ("walking", "driving", "bus", "train"):  # Checks if the user inputted the recognized mode
            print("You have entered an invalid mode of transportation")
        else:
            print(weather_check(destination_city, destination_country))
            print(f"It will take {duration} to get to {destination}")  # The duration is printed
            direction = data['routes'][0]['legs'][0]['steps']  # Getting the detailed HTML direction from Google API
            with open('user_directions.json', 'w') as json_file:
                json.dump(direction, json_file, indent=2)  # Writing the direction into a JSON file
            blank_direction = []
            is_direction = input(f"Do you want direction to {destination}?\nType Yes or No: ").lower()
            if is_direction == "yes":
                if len(direction) > 0:  # Check the number of HTML instructions in the dictionary
                    for i in range(0, len(direction)):
                        blank_direction.append(direction[i]['html_instructions'])  # Appending each HTML instruction
                        # to a blank list
                    print("Below is your direction:")
                    for i in blank_direction:
                        soup = BeautifulSoup(i,
                                             'html.parser')  # Using BeautifulSoup class to clean the HTML instruction
                        print(' '.join(
                            soup.stripped_strings))  # Printing the cleaned HTML instruction while adding whitespace
                elif len(direction) == 0:
                    soup = BeautifulSoup(direction[0]['html_instructions'], 'html.parser')  # Using BeautifulSoup
                    # class to clean the single HTML instruction
                    print(
                        f"Below is your direction: \n{' '.join(soup.stripped_strings)}")  # Printing the cleaned HTML               
    except KeyError as e:
        print("Invalid location")
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred: {e}. Try providing location and destination with a specific city and country")
        return None  # End of the try statement
    return destination_country, destination_city
