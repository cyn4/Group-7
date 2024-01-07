def discover_more_places():  
    print(places)
    user_city, user_country, search, user_rating, number_of_output = get_user_input()
    place = user_city, user_country
    location = get_location_coordinates(place)  # Getting coordinates for the user's location
    # Displaying weather information for the user's location
    print(weather_check(user_city, user_country))
    # Getting and displaying nearby places based on user's input
    nearby_places = get_nearby_places(location, search, user_rating, number_of_output)
    return display_nearby_places(nearby_places)