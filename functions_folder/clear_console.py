def clear_console(): 
    """
    Clears the console screen.

    Returns:
    - None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
