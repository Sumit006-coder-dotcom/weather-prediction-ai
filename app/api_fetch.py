import requests

API_KEY = "df57c152a532b88aa2501d0141e9f090"

def fetch_5day_forecast(city):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return None
        
        lat = data["city"]["coord"]["lat"]
        lon = data["city"]["coord"]["lon"]
        country = data["city"]["country"]


        daily_forecast = {}
        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]  
            hour = item["dt_txt"].split(" ")[1]

            # Pick only midday data for each day
            if hour == "12:00:00" and date not in daily_forecast:
                daily_forecast[date] = {
                    "date": date,
                    "temp": item["main"]["temp"],
                    "humidity": item["main"]["humidity"],
                    "pressure": item["main"]["pressure"],
                    "wind_speed": item["wind"]["speed"],
                    "weather": item["weather"][0]["main"],
                    "latitude": data["city"]["coord"]["lat"],
                    "longitude": data["city"]["coord"]["lon"],
                    "city": data["city"]["name"],
                    "country": data["city"]["country"]
                }

        return list(daily_forecast.values())

    except requests.exceptions.RequestException as e:
        return str(e)