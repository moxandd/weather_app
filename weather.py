from coordinates import get_loc
from weather_api import get_weather
from weather_formatter import format_weather


def main():
    coords = get_loc()
    weather = get_weather(coords)
    print(format_weather(weather))

if __name__ == '__main__':
    main()