def weather_check(user_city, user_country):
    """
    Check the weather by passing city and country.

    Args:
    - user_city (str): City for weather check.
    - user_country (str): Country for weather check.

    Returns:
    - str: Weather information based on the user's location.
    """
    weather_api_key = os.getenv("WEATHER_API_KEY") # Retrieve API key from environment variable
    endpoint = 'http://api.openweathermap.org/data/2.5/weather' # API endpoint for weather data
    user_location = f"{user_city},{user_country}" # Format location string for API request
    payload = {
        'q': user_location,
        'unit': 'metrics',
        'appid': weather_api_key
    }  # The parameters to be passed to the get method
    response = requests.get(url=endpoint, params=payload)
    data = response.json()
    try:  # The try statement ensures the code doesn't break
        conversion = round(data['main']['feels_like'] - 273.15)  # This converts the temperature to degrees
        if conversion >= 35:  # The 'if' block prints feedback based on the temperature of the user's location
            return (f"The weather is: {conversion}°\n🌞 It is sunny in {user_city}, pack a sunscreen 🍶 or pack an "
                    f"Umbrella"
                    f"☂️\n")
        elif conversion >= 20:
            return f"🌥️ The weather is: {conversion}°\nNice weather in {user_city}, let your hair out💃🏻 "
        if conversion <= 19:
            return f"☃️ 🥶 The weather is: {conversion}°\nIt is very cold in {user_city} pack a sweater 🧥 and Gloves🧤\n"
    except KeyError as e:
        print("Invalid city or country") # Handle invalid location input
        return None
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  # Handle other potential errors
        return None  # End of the try statement
