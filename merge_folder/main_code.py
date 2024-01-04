from functions import get_location_coordinates, display_places, get_nearby_places, get_user_input, weather_check, direction, \
    clear_console
from travel_guide_logo import logo, greeting  # Importing specific art elements for visual display
if __name__ == "__main__":
    usage = True
    while usage:
        print(greeting, logo)  # Printing greeting and logo art
        # Getting user input
        user_city, user_country, search, user_rating, number_of_output = get_user_input()
        place = user_city, user_country
        location = get_location_coordinates(place)  # Getting coordinates for the user's location

        if location:
            # Displaying weather information for the user's location
            print(weather_check(user_city, user_country))
            # Getting and displaying nearby places based on user's input
            nearby_places = get_nearby_places(location, search, user_rating, number_of_output)
            display_places(nearby_places)

        travel = input("🧭 Will you like navigation service\n Type Yes or No: ").lower()  # Asking if the user wants navigation service
        if travel == 'yes':
            direction()  # Providing navigation directions if requested

        user_usage = input('Do you have other fun places and destinations to check out 😃?\nType yes or no: ').lower()
        if user_usage == "no":
            print("Sad to see you leave 😔. Check back soon.")
            break
        else:
            clear_console()  # Clearing the console for the next iteration