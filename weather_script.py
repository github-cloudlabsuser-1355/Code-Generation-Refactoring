import requests

# Ensure the 'requests' module is installed:
# You can install it using: pip install requests
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

API_KEY = 'cf5a0745aafecfc67917ab4cb6c5df77'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    if weather_data:
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")