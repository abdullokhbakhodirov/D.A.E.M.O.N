import requests
from geopy.geocoders import Nominatim
import geocoder


def get_weather(CITY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY= "7daf597c88cbbde8f8bb0ff1c3ccb047"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        return temperature, CITY
    else:
        return False


def get_location():
    Nomi_locator = Nominatim(user_agent="My App")
    my_location = geocoder.ip('me')
    latitude = my_location.geojson['features'][0]['properties']['lat']
    longitude = my_location.geojson['features'][0]['properties']['lng']
    location = Nomi_locator.reverse(f"{latitude}, {longitude}")
    if location and 'address' in location.raw:
        address = location.raw['address']
        city = address.get('city', '')
        return get_weather(city)