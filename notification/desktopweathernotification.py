import requests
import json
from plyer import notification
import time

API_KEY = "3bf0d155b64d22daaef53f39c5289906"  # Replace with your OpenWeatherMap API key
CITY = "Kampala"  # Replace with your desired city

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def show_notification(weather_data):
    if weather_data:
        temp = round(weather_data["main"]["temp"] - 273.15) # Convert Kelvin to Celsius
        description = weather_data["weather"][0]["description"]
        title = f"Weather in {CITY}"
        message = f"Temperature: {temp}°C\nConditions: {description}"
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )
    else:
        notification.notify(
            title="Weather Update Error",
            message="Could not retrieve weather data.",
            timeout=10
        )

if __name__ == "__main__":
    while True:
        weather_data = get_weather_data(CITY, API_KEY)
        show_notification(weather_data)
        time.sleep(60 * 60) # Update every hour
