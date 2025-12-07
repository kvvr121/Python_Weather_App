# build a python weather app using tkinter that fetches data from open-meteo api (no API key required)
import tkinter as tk
from tkinter import messagebox

import requests

def get_weather(city):
    # Using Open-Meteo API - Free, no API key required
    # First get coordinates for the city
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    
    try:
        geocoding_response = requests.get(geocoding_url)
        geocoding_data = geocoding_response.json()
        
        if not geocoding_data.get("results"):
            return {"error": "City not found"}
        
        city_data = geocoding_data["results"][0]
        latitude = city_data["latitude"]
        longitude = city_data["longitude"]
        city_name = city_data["name"]
        country = city_data.get("country", "")
        
        # Get weather data - using current endpoint with correct parameters
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,weather_code&temperature_unit=celsius"
        
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        current = weather_data.get("current", {})
        
        return {
            "city": city_name,
            "country": country,
            "temperature": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "description": get_weather_description(current.get("weather_code", 0))
        }
    except Exception as e:
        return {"error": str(e)}

def get_weather_description(code):
    """Convert WMO weather codes to descriptions"""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Freezing fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight showers",
        81: "Moderate showers",
        82: "Violent showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }
    return descriptions.get(code, "Unknown")
def show_weather():
    city = city_entry.get()
    if not city.strip():
        messagebox.showerror("Error", "Please enter a city name!")
        return
    
    weather_data = get_weather(city)
    
    if "error" in weather_data:
        messagebox.showerror("Error", f"Unable to fetch weather: {weather_data['error']}")
        return
    
    try:
        city_name = weather_data.get("city", city)
        country = weather_data.get("country", "")
        temp = weather_data.get("temperature")
        humidity = weather_data.get("humidity")
        description = weather_data.get("description")
        
        location = f"{city_name}, {country}" if country else city_name
        weather_info = f"Location: {location}\nTemperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description}"
        messagebox.showinfo("Weather Info", weather_info)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to parse weather data: {str(e)}")
app = tk.Tk()
app.title("Weather App")
app.geometry("300x150")
city_label = tk.Label(app, text="Enter City Name:")
city_label.pack(pady=10)
city_entry = tk.Entry(app)
city_entry.pack(pady=5)
get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)
app.mainloop()