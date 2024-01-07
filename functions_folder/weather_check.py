def weather_check(user_city, user_country): #Tobi
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