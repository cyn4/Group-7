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
        user_rating = int(number_of_output)

    return user_city, user_country, search, user_rating, number_of_output  # Returning multiple values as a tuple

# The rest of the code remains the same as previously commented.
