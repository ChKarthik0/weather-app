from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    """Render homepage with search form"""
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    """Fetch and display weather data"""
    city = request.form.get('city')
    
    if not city:
        return render_template('index.html', error="Please enter a city name")

    # API request
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
            return render_template('weather.html', weather=weather)
        
        else:
            error_msg = data.get('message', 'Unknown error')
            return render_template('index.html', error=f"API Error: {error_msg}")

    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)