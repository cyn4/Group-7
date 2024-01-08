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

                # Converting user_rating to float if it's not "any"
                if user_rating != "any":
                    user_rating = float(user_rating)
                nearby_places = get_nearby_places(location, search, user_rating, number_of_output)
                display_nearby_places(nearby_places)
            elif push_place_discovery_service == "no":
                break
        if more_navigation_service() == "no":
            break
