import requests
from datetime import datetime
from typing import NamedTuple
from enum import Enum
from coordinates import Coordinates

Celcius = int

class WeatherType(Enum):
    RAIN = 'Rain'
    THUNDERSTORM = 'Thunderstorm'
    DRIZZLE = 'Drizzle'
    CLOUDS = 'Clouds'
    SNOW = 'Snow'
    CLEAR = 'Clear'
    FOG = 'Fog'

class Weather(NamedTuple):
    temperature: Celcius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coords: Coordinates) -> Weather:
    """Requests weather from OpenWeatherAPI and returns it"""

    print('Checking for a weather in your city...')
 

    api_key = '799a68dd333c2cdc39c1a33d8d930a6e'
    lat, lon = coords

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}').json()

    # Parsing all needed data
    temperature = Celcius(result['main']['temp'] - 273)
    weather_type = result['weather'][0]['main']
    sunrise = datetime.fromtimestamp(result['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(result['sys']['sunset']).strftime('%H:%M')
    city = result['name']

    
    return Weather(temperature=temperature, weather_type=weather_type, sunrise=sunrise, sunset=sunset, city=city)