<h1>SimpleWeather - A Minimal Weather Application</h1>
This is a simple Flask-based application that gives you the current weather data for any city in the world. You can also get weather data for your current location (based on your IP address). The data includes city name, temperature, humidity, wind speed and weather description.

<h2>Getting Started</h2>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.6+</li>
  <li>Flask</li>
  <li>requests</li>
  <li>OpenWeatherMap API Key</li>
</ul>

<h2>Installation</h2>

Clone the repository:
```md
git clone https://github.com/JohnNtirintis/Weather-Application.git
```

Navigate to the cloned project directory
```md
cd Weather-Application
```

Install the necessary packages
```md
pip install flask requests
```

<h2>OpenWeatherMap API Key</h2>
<p>For this project you will need an API key to make requests to OpenWeatherMap, if you dont add an API key this project will not work.</p>
<p>Note: i chose OpenWeatherApp because it has a completely free plan and costs litteraly nothing to use.</p>
 
<ol>
  <li>Visit the OpenWeatherMap website and create an account if you don't have one already.</li>
  <li>Once you are logged in, you can generate your API Key.</li>
  <li>Create a file named api-key.txt in the project's root directory.</li>
  <li>Copy your API key and paste it in the api-key.txt file.</li>
  <li>Save the api-key.txt file and run the project.</li>
</ol>

Run the application
```md
python -m flask --app main run
```


<h2>How to Use</h2>
<h3>The application has four main routes:</h3>

<ol>
  <li>Home route '/' : This route will render the home page of the application.</li>
  <li>By city route '/weather/x' : This route will show the current weather data for the specified city. Replace x with the name of the city.</li>
  <li>By IP route '/weather/' : This route will show the current weather data for the location determined by your IP address.</li>
    Note: the ip tracker is not very accurate.
  <li>Search bar: on the top right of the website there is a search bar that the user can enter their desired city to search for the currect weather forecast.</li>
</ol>

```md
The application will show an error message if the weather data for the specified city is not available.
```
    
<h2>Built With</h2>
  <ul>
    <li>Flask - The web framework used.</li>
    <li>OpenWeatherMap - The API used to get the weather data.</li>
    <li>IPAPI - The ip tracker used to locate the user's city.</li>
  </ul>
