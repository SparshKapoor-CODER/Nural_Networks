import requests
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather_forecast(city):
    """Fetch 5-day weather forecast data from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "cnt": 5  # Fetching data for the next 5 timestamps
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        forecast_data = []
        
        for item in data["list"]:
            date = datetime.utcfromtimestamp(item["dt"]).strftime('%Y-%m-%d %H:%M')
            temp = item["main"]["temp"]
            humidity = item["main"]["humidity"]
            forecast_data.append((date, temp, humidity))
        
        return forecast_data
    else:
        return None

def plot_forecast(forecast_data, city):
    """Plot temperature and humidity trends."""
    dates = [item[0] for item in forecast_data]
    temps = [item[1] for item in forecast_data]
    humidities = [item[2] for item in forecast_data]

    plt.figure(figsize=(10, 5))

    # Temperature Plot
    plt.plot(dates, temps, marker='o', linestyle='-', color='r', label='Temperature (°C)')
    
    # Humidity Plot
    plt.plot(dates, humidities, marker='s', linestyle='-', color='b', label='Humidity (%)')

    plt.xlabel("Date & Time")
    plt.ylabel("Values")
    plt.title(f"5-Day Weather Forecast for {city}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    forecast = get_weather_forecast(city_name)

    if forecast:
        print(f"Weather Forecast for {city_name}:")
        for date, temp, humidity in forecast:
            print(f"{date} - Temp: {temp}°C, Humidity: {humidity}%")
        
        plot_forecast(forecast, city_name)
    else:
        print("Error fetching weather data. Please check your city name and API key.")