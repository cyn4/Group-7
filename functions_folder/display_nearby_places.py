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
        with open('user_search.txt', 'w', encoding='utf-8') as text_file: # Enumerating the output
            for idx, place in enumerate(places, start=1):
                text_file.write(f"{idx}. {place['name']}\n")
                text_file.write(f"Rating: {place.get('rating', 'Not rated')}\n")
                text_file.write(f"Address: {place.get('vicinity', 'Address not available')}\n\n") #Places are extracted into a text file
                # Printing the same content to the console
                print(f"{idx}. {place['name']}")
                print("Rating:", place.get('rating', 'Not rated'))
                print("Address:", place.get('vicinity', 'Address not available'))
                print()
    else:
        print("Search not found")
