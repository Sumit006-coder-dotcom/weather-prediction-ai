import requests

API_KEY = "df57c152a532b88aa2501d0141e9f090"

def fetch_weather(city_input):
    city_input = city_input.strip()

    # 🔥 If user enters only city, try city + IN first
    if "," not in city_input:
        city_query = f"{city_input},IN"
    else:
        city_query = city_input

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city_query}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    # If still fails, try without country (global fallback)
    if response.status_code != 200 and "," in city_query:
        fallback_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city_input}&appid={API_KEY}&units=metric"
        )
        response = requests.get(fallback_url)
        data = response.json()

    if response.status_code != 200:
        return {
            "error": True,
            "message": (
                "City not found. Try format: City,CountryCode "
                "(e.g., Delhi,IN | London,UK | New York,US)"
            )
        }

    return {
        "error": False,
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "latitude": data["coord"]["lat"],
        "longitude": data["coord"]["lon"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "weather": data["weather"][0]["main"]
    }