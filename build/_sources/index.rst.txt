.. smart Travel Documentation documentation master file, created by
   sphinx-quickstart on Sun Dec 31 05:18:32 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to smart Travel Documentation!
======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. contents:: Table of Contents
   :depth: 2

Functions and Usage
===================================

Introduction
------------

This documentation covers the functionalities provided by the functions in the `functions.py` script.
It also covers the functionalities provided by the get_user_input() in the `main.py` script

Get Location Coordinates Function
---------------------------------

The `get_location_coordinates` function accesses the Google Maps API to return the coordinates (latitude and longitude) of a specified place.

Usage
~~~~~

The function takes one argument:

- `place` (str): The location for which coordinates are to be fetched.

Returns
~~~~~~~

A string containing the latitude and longitude in the format "latitude,longitude".

Example
~~~~~~~

Here is an example of how to use the function:

.. code-block:: python

    from functions import get_location_coordinates

    location = "San Francisco"
    coordinates = get_location_coordinates(location)
    print("Coordinates:", coordinates)

Note
~~~~

- If the specified place is not found, the function returns `None`.

---

Get Nearby Places Function
--------------------------

The `get_nearby_places` function retrieves a specific type of place based on coordinates, search query, user rating, and the number of results.

Usage
~~~~~

The function takes four arguments:

- `location` (str): Coordinates (latitude,longitude) of the area.
- `search` (str): Type of place to search for.
- `user_rating` (int/str): Minimum user rating or 'any' for any rating.
- `number_of_output` (int): Number of results to retrieve.

Returns
~~~~~~~

A list of nearby places based on the search criteria.

Example
~~~~~~~

Here is an example of how to use the function:

.. code-block:: python

    from functions import get_nearby_places

    location = "37.7749,-122.4194"
    search_query = "restaurant"
    rating = 4
    results = 5

    nearby_places = get_nearby_places(location, search_query, rating, results)
    print("Nearby Places:", nearby_places)

Note
~~~~

- If the function fails to fetch nearby places, it returns `None`.
- An unexpected error might occur due to invalid city/country or search queries.

---

Display Nearby Places Function
------------------------------

The `display_nearby_places` function displays a list of places, ratings, and addresses based on the provided data.

Usage
~~~~~

The function takes one argument:

- `places` (list): List of places with details.

Returns
~~~~~~~

None (Prints the information to the console).

Example
~~~~~~~

The function usage might look like this:

.. code-block:: python

    from functions import display_nearby_places

    places_data = [
        {
            'name': 'Place 1',
            'rating': 4.5,
            'vicinity': 'Address 1'
        },
        {
            'name': 'Place 2',
            'rating': 3.8,
            'vicinity': 'Address 2'
        }
        # Add more places data here...
    ]

    display_nearby_places(places_data)

Note
~~~~

- If no search results are found, it prints "Search not found".

---

Weather Check Function
----------------------

The `weather_check` function checks the weather by passing city and country parameters.

Usage
~~~~~

The function takes two arguments:

- `user_city` (str): City for weather check.
- `user_country` (str): Country for weather check.

Returns
~~~~~~~

A string providing information about the weather conditions.

Example
~~~~~~~

Here is an example of how to use the function:

.. code-block:: python

    from functions import weather_check

    city = "New York"
    country = "US"

    weather_info = weather_check(city, country)
    print("Weather Information:", weather_info)

Note
~~~~

- If the specified city or country is invalid, the function returns `None`.
- An unexpected error might occur due to network issues or incorrect inputs.

---

Direction Function
------------------

The `direction` function provides directions between two locations based on user input.

Usage
~~~~~

The function takes no arguments interactively using input() method.

Returns
~~~~~~~

None (Prints directions to the console).

Example
~~~~~~~

The function usage might look like this:

.. code-block:: python

    from functions import direction

    direction()

Note
~~~~

- If an invalid location is provided, the function raises an exception.
- Ensure to provide specific city and country inputs for accurate directions.

---

Clear Console Function
----------------------

The `clear_console` function clears the console screen.

Usage
~~~~~

No arguments are required for this function.

Returns
~~~~~~~

None

Example
~~~~~~~

Usage might look like this:

.. code-block:: python

    from functions import clear_console

    clear_console()

Note
~~~~

- This function uses the `os` module and may behave differently on different operating systems.

---

Get User Input Function
-----------------------

The `get_user_input` function collects user inputs regarding city, country, search query, user rating preference, and the number of results to display.

Usage
~~~~~

The function prompts the user for inputs using the `input()` function. It expects the following inputs:

- `user_city` (str): The city of interest.
- `user_country` (str): The country of interest.
- `search` (str): The type of place the user is searching for.
- `user_rating` (int/str): The user's rating preference. It can be an integer (for a specific rating) or "any" (for all ratings).
- `number_of_output` (int): The number of search results to display.

Returns
~~~~~~~

A tuple containing user input values for city, country, search query, user rating, and the number of results.

Example
~~~~~~~

Here is an example of how to use the function:

.. code-block:: python

    from functions import get_user_input

    user_inputs = get_user_input()
    print("User Inputs:", user_inputs)

Note
~~~~

- The function uses input prompts and expects user inputs in a specific format.
- Ensure to provide accurate and valid inputs to receive the desired results.

---
                     HAPPY CODING!!!
---


