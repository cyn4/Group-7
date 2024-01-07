# Importing necessary functions from 'functions' module and specific art elements from 'Title' module
from functions import discover_places_service, push_navigation_services, navigation_services, app_exit, clear_console
from Title import logo # Importing specific art elements for visual display

if __name__ == "__main__": # Main execution of the program
    usage = True
    while usage:
        print(logo) # Printing greeting and logo art
        service_type = input(
            "Do you want to Discover places 🏨 or Do you want Navigation services 🗺️\n Type (Places or "
            "Navigation): ").lower()
        if service_type == "places":
            discover_places_service() # Executing function to discover places
            if push_navigation_services() == "yes": # Asking user if they want to proceed with navigation services
                navigation_services() # Executing function to provide navigation services
            if app_exit() == "yes": # Asking user if they want to exit the program
                print("Sad to see you leave 😔. Check back soon.")
                break
            else:
                clear_console() # Clearing console for a fresh start
        if service_type == "navigation":
            navigation_services() # Executing function to provide navigation services
            print("\n")
            if app_exit() == "yes": # Asking user if they want to exit the program
                print("Sad to see you leave 😔. Check back soon.")
                print("\n")
                break
            else:
                clear_console() # Clearing console for a fresh start
