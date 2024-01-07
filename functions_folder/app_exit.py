def app_exit():
    """
    Function to ask the user if they want to exit the app.

    Returns:
    - str: User's choice ('Yes' or 'No')
    """
    exit = input("Do you want to exit app. Type Yes or No:  ").lower()
    return exit