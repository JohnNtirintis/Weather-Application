# SimpleWeather - A Modern, User-Centric Weather Application

SimpleWeather is a Flask and MongoDB-based web application that provides users with current and weekly weather data for any city in the world. The application has evolved to include features like user registration, authentication, and the ability to save favorite cities. This project, being my first personal venture, has been an enriching experience, providing a deeper understanding of web development, databases, and user-centered design.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

## Prerequisites

- Python 3.6+
- Flask
- PyMongo
- Flask-Login
- WTForms
- bcrypt
- OpenWeatherMap API Key

## Installation

1. Clone the repository:
 ```md
 git clone https://github.com/JohnNtirintis/Weather-Application.git
 ```
2. Navigate to the clone project directory:
 ```md
 cd Weather-Application
 ```
3. Install the necessary packages::
 ```md
 pip install -r requirements.txt
 ```


## OpenWeatherMap API Key

To fetch the weather data, you'll need an API key from OpenWeatherMap.

1. Sign up for a free account on OpenWeatherMap (if you don't already have one).
2. Generate your API Key.
3. Create a file named api-key.txt in the project's root directory.
4. Paste your API key in the api-key.txt file.
5. Save the file.

## Running the Application

Start the application with the following command:
```md
python -m flask --app main run
```

## How to Use

The application includes the following key features:

1. Home Page ('/'): Displays the landing page of the application.
2. Search Bar: Allows users to find weather forecasts for their desired city.
3. IP-based Weather ('/weather/'): Provides weather data based on the user's IP address (accuracy may vary).
4. City-specific URL ('/weather/<city_name>'): Shows current weather data for a specified city.
5. User Registration and Login: Users can create accounts, log in, and save their favorite cities.

Note: An error message will be displayed if the weather data for a particular city is unavailable.

## Built With

- Flask - The web framework used.
- MongoDB - The database used for user registration, login and favorite cities.
- OpenWeatherMap - The API used to get weather data.
- IPAPI - The IP tracker used to locate the user's city (accuracy may vary).
- WTForms - For form handling and validation.
- Flask-Login - For user authentication.
- bcrypt - For password hashing and verification.


This project marks my first step in the exciting journey of web development. I've learned a lot in the process and am eager to learn and build more. Your feedback is welcome and appreciated.

  
