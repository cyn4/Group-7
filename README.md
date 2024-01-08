# ExploreWayz

ExploreWayz is a Python application designed to facilitate efficient trip planning by providing users with a unified solution for location information, real-time weather updates, and recommendations for places like restaurants. The application leverages APIs such as Google Maps and OpenWeatherMap to offer users a seamless experience in exploring and adapting to new locations effortlessly.

## Features

- **Location Coordinates Retrieval:** Utilizes the Google Maps API to retrieve the coordinates (latitude and longitude) of a specific place.
- **Logging Coordinates:** Logs the coordinates of a place to a text file for future reference.
- **Discover Nearby Places:** Fetches nearby places based on user-input coordinates, search query, user rating preference, and number of results.
- **Display Nearby Places:** Presents a list of nearby places along with their ratings and addresses.
- **Weather Check:** Provides weather information for a given city and country, offering insights into the current weather conditions.
- **Directions and Navigation:** Offers directions between two locations based on user input, utilizing the Google Maps Directions API.
- **User Interaction:** Engages users through interactive prompts for discovering new places and navigation services.

## Dependencies

- Python
- Requests library: For making HTTP requests to web servers or APIs.
- BeautifulSoup library: For HTML parsing and cleaning up HTML/XML documents.
- dotenv library: For loading environment variables from a .env file.
- os module: For interacting with the operating system

## Getting Started

1. Download the Explorewayz documentation zip file, extract the file upon download, and open the index HTML in the build folder.
2. Clone the repository or download the codes in the merged folder.
3. Ensure Python is installed on your machine.
4. Install the required dependencies using the pip install -r requirements.txt or pip3 install -r requirements.txt depending on your IDE
5. Set up necessary API keys:
    - Obtain a Google Maps API key and OpenWeatherMap API key.
    - Create a `.env` file and store these keys:
        ```
        GOOGLE_MAPS_API_KEY_PLACES=your_google_maps_api_key
        GOOGLE_MAPS_API_COORDINATES=your_google_maps_api_key
        WEATHER_API_KEY=your_openweathermap_api_key
        ```
6. Run the main script `main.py`.
7. Ensure the `function.py` file is loaded whilst running the `main.py`
8. Follow the on-screen prompts to explore places or utilize navigation services.


## Usage

- Upon running the application, users are prompted to choose between discovering places or navigation services.
- For discovering places, users can input a city, country, search query, user rating preference, and number of results to display.
- Navigation services offer directions between two locations and the option to explore places in the destination.


## Example
<img src="Images/Welcomepage.png" width="300" height="200"> <img src="Images/Exploreplaces.png" width="300" height="200"><img src="Images/Navigation.png" width="300" height="200">


## Flow Charts
### App Flow Chart

<img width="7472" alt="Flow charts_app" src="https://github.com/cyn4/Group-7/assets/131699315/6b8f5441-f2da-414d-b8b6-d82d40d52cba">


## Function Explanation
There is webpage documentation for the functions used in developing this app console, which has been in the ExploWayz Documentation Zip file.
### How to access the webpage HTML file
       - Download the Zip file 
       - Extract the Zip file 
       - Open the documentation folder
       - Open build folder 
       - Open index HTML file 


### Code Structure

![Code Structure Flow Chart](Images/codeStructure_Flowchart.png)



## Contributors

- Oluwatobi
- Kafayat
- Cynthia
- Aishat
- Zione

# Individual Contribution

## Oluwatobi 
    - weather_check function
    - direction function
    - display_nearby_places function
    - clear_console
    - documentation
  
## Kafayat
    - main.py file
    - get_nearby_places function
    - app_exit function

## Cynthia
     - get_location_coordinate function
     - log_coordinate function
     - merge folder
     - Flow chart
    
## Aishat
     - title.py file
     - get_user_input function
     - discover_place_servicve function
     - discover_more_places function
    
## Zione
     - push_Navigation_service function
     - more_navigation_service function
     - navigation_service function

    
## Group Contribution 
     - Readme
     - PowerPoint presentation
     - .env file

    
  
  
