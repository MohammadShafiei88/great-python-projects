import json
import requests
from typing import Final
from datetime import datetime as dt
from dataclasses import dataclass



@dataclass
class Weather:
    date: dt
    details: dict
    temp: str
    weather: list[dict]
    description: str

    def __str__(self):
        return f'[{self.date:%H:%M}] {self.temp}C° ({self.description})'


API_KEY: Final[str] = ''
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(city_name: str, mock: bool = False) -> dict:
    if mock:
        print('Using mock data...')
        with open('dummy_data.json') as file:
            return json.load(file)

    payload: dict = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data


def get_weather_details(weather: dict) -> list[Weather]:

    days: list[dict] = weather.get('list')

    # If there is no data for days, no point in continuing
    if not days:
        raise Exception(f'Problem with json: {weather}')

    # Try to add the info we want to our list_of_weather
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description'))
        list_of_weather.append(w)

    return list_of_weather

def main():
    user_city: str = input('Enter a city: ')

    current_weather: dict = get_weather(user_city, mock=False)
    weather_details: list[Weather] = get_weather_details(current_weather)

    dfmt: str = '%d/%m/%y'
    days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_details})

    for day in days:
        print(day)
        print('---')

        grouped: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)

        print()


if __name__ == '__main__':
    main()
