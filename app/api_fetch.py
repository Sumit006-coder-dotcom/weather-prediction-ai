import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather(city_input):
    city_input = city_input.strip()

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city_input}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return {
            "error": True,
            "message": (
                "City not found. Try format: City or City,CountryCode "
                "(e.g., London,UK | New York,US | Delhi,IN)"
            )
        }

    return {
    "error": False,
    "city": data["name"],
    "country": data["sys"]["country"],
    "latitude": data["coord"]["lat"],
    "longitude": data["coord"][API_KEY = os.getenv("OPENWEATHER_API_KEY")
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"],
    "wind_speed": data["wind"]["speed"],
    "weather": data["weather"][0]["main"]
}