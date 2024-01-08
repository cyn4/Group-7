def direction(): 
    """
    Provides directions between two locations based on user input.

    Returns:
    - None
    """
    GOOGLE_MAPS_API_KEY = "AIzaSyCqXq0BqIAIojo2IGJKkivABWFNM0fUCYA"
    destination_country = input("What country is the destination?: ").lower()
    destination_city = input("What city is the destination?: ").lower()
    origin = input("🏨 Enter your current location: ").lower()
    destination = input("🗺️ Enter your destination: ").lower()
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
            print("\n")
            print(weather_check(destination_city, destination_country))
            print(f"\nEstimated duration: It will take {duration} to get to {destination}")  # The duration is printed
            direction = data['routes'][0]['legs'][0]['steps']  # Getting the html direction from Google API
            with open('user_directions.json', 'w') as json_file:
                json.dump(direction, json_file, indent=2)  # writing the direction into a json file
            blank_direction = []
            is_direction = input(f"Do you want direction to {destination}?\nType Yes or No: ").lower()
            if is_direction == "yes":
                if len(direction) > 1:  # Check the number of html instruction in the dictionary
                    for i in range(0, len(direction)):
                        blank_direction.append(direction[i]['html_instructions'])  # Appending each html instruction
                        # to a blank list
                    print("\nHere are the directions:")
                    for i in blank_direction:
                        soup = BeautifulSoup(i,
                                             'html.parser')  # Using BeautifulSoup class to clean the html instruction
                        print(' '.join(
                            soup.stripped_strings))  # printing the cleaned html instruction whilst adding whitespace
                elif len(direction) == 1:
                    soup = BeautifulSoup(direction[0]['html_instructions'], 'html.parser')  # Using BeautifulSoup
                    # class to clean the single html instruction
                    print(
                        f"\nHere are the directions: \n{' '.join(soup.stripped_strings)}")  # printing the cleaned html
                    # instruction whilst adding whitespace
    except KeyError as e:
        print("Invalid location")
        return None
    except Exception as e:
        print(
            f"An unexpected error occurred: {e}. Try providing location and destination with specific city and country")
        return None  # End of the try statement
    return destination_country, destination_city
