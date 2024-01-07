def discover_places_service():  
    """
    Function to handle discovering places based on user input.

    This function asks the user if they want to discover other places and continues the discovery process
    until the user decides not to discover more.

    Returns:
    - None
    """
    discover = True
    while discover:
        clear_console()
        discover_more_places()
        is_more_places = input("Will you like to discover other places ( Type yes or No):  ").lower()
        if is_more_places == "yes":
            clear_console()
        elif is_more_places == "no":
            break