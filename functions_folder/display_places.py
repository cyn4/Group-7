def display_places(places):
    """
    Displays a list of places, ratings, and addresses based on the provided data.

    Args:
        places (list): List of places with details.

    Returns:
        None
    """

    if places:
        print("Places:")

        # Open a text file to store the search results
        with open('user_search.txt', 'a') as text_file:  # 'a' mode for appending
            for idx, place in enumerate(places, start=1):
                # Write the place information to the text file
                text_file.write(f"{idx}. {place['name']}\n")
                text_file.write(f"Rating: {place.get('rating', 'Not rated')}\n")
                text_file.write(f"Address: {place.get('vicinity', 'Address not available')}\n\n")

                # Print the same content to the console
                print(f"{idx}. {place['name']}")
                print("Rating:", place.get('rating', 'Not rated'))
                print("Address:", place.get('vicinity', 'Address not available'))
                print()
    else:
        print("Search not found")