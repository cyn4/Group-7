def more_navigation_service(): 
    """
    Function to ask the user if they want navigation services for other destinations.

    Returns:
    - str: User's choice ('Yes' or 'No')
    """
    more_navigation = input("\nDo you want navigation services for other destinations.\nType Yes or No: ").lower()
    return more_navigation
