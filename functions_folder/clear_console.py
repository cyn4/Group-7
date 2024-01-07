def clear_console():  # Tobi
    """
    Clears the console screen.

    Returns:
    - None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
