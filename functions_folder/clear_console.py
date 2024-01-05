def clear_console():
    """
    Clears console screen based on OS.
    This function uses the os.name attribute to check the user's operating system.
    If the operating system is Windows ('nt'), it uses the 'cls' command to clear
    the console.
    If the operating system is Unix/Linux, it uses the 'clear' command to clear the console

    Returns:
    - None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
