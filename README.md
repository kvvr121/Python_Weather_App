# Python Weather App

A simple and elegant weather application built with Python and Tkinter that displays real-time weather information for any city in the world.

## Features

- 🌍 **Global City Search**: Get weather for any city worldwide
- 🌡️ **Real-time Weather Data**: Temperature, humidity, and weather conditions
- 🎨 **User-friendly GUI**: Simple and intuitive Tkinter interface
- 🔓 **No API Key Required**: Uses the free Open-Meteo API
- 📱 **Responsive Design**: Clean, minimal interface

## Tech Stack

- **Language**: Python 3.11
- **GUI Framework**: Tkinter
- **Weather Data API**: Open-Meteo (Free, no authentication needed)
- **HTTP Requests**: Requests library
- **Geocoding API**: Open-Meteo Geocoding API

## Requirements

- Python 3.11 or higher
- requests library
- tkinter (usually comes pre-installed with Python)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kvvr121/Python_Weather_App.git
cd Python_Weather_App
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the App

Activate the virtual environment and run:
```bash
python weather.py
```

The GUI window will open with:
- A text input field to enter the city name
- A "Get Weather" button to fetch the weather data
- Weather information displayed in a popup message

### Example

1. Launch the app
2. Enter "New Delhi" in the text field
3. Click "Get Weather"
4. View the weather information:
   - Location (City, Country)
   - Current Temperature (°C)
   - Humidity (%)
   - Weather Condition

## API Information

### Open-Meteo Weather API
- **Endpoint**: `https://api.open-meteo.com/v1/forecast`
- **Features**: Free, no API key required
- **Parameters Used**:
  - `latitude`: City latitude
  - `longitude`: City longitude
  - `current`: Current weather parameters (temperature, humidity, weather code)
  - `temperature_unit`: Set to Celsius

### Open-Meteo Geocoding API
- **Endpoint**: `https://geocoding-api.open-meteo.com/v1/search`
- **Purpose**: Convert city names to coordinates

## Code Structure

### Main Functions

#### `get_weather(city)`
- Fetches weather data for a given city
- First uses the geocoding API to get coordinates
- Then retrieves current weather from the weather API
- Returns a dictionary with city name, country, temperature, humidity, and description

#### `get_weather_description(code)`
- Converts WMO weather codes to human-readable descriptions
- Supports 24 different weather conditions
- Returns descriptive text for the current weather condition

#### `show_weather()`
- Handles GUI interaction
- Validates user input
- Calls the weather API
- Displays results in a message box with error handling

### GUI Components
- **Root Window**: Main tkinter window with title "Weather App"
- **City Label**: Text label "Enter City Name:"
- **City Entry**: Text input field for city name
- **Get Weather Button**: Button to fetch weather data

## Supported Weather Codes

The app supports the following WMO weather codes:
- 0: Clear sky
- 1: Mainly clear
- 2: Partly cloudy
- 3: Overcast
- 45/48: Foggy conditions
- 51-55: Drizzle
- 61-65: Rain
- 71-75: Snow
- 80-82: Showers
- 85-86: Snow showers
- 95-99: Thunderstorms with hail

## Error Handling

The app handles various error scenarios gracefully:
- **Empty Input**: Prompts user to enter a city name
- **City Not Found**: Informs user if the city is not recognized
- **API Errors**: Displays detailed error messages
- **Network Issues**: Shows error message if connection fails
- **Invalid Data**: Handles malformed API responses

## Example Output

```
Location: New Delhi, India
Temperature: 21.8°C
Humidity: 47%
Condition: Clear sky
```

## File Structure

```
Python_Weather_App/
├── weather.py          # Main application file
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore file
└── venv/               # Virtual environment directory (not tracked in git)
```

## Troubleshooting

### Issue: ModuleNotFoundError: No module named '_tkinter'
**Solution**: Install tkinter using Homebrew on macOS:
```bash
brew install python-tk@3.11
```

### Issue: "City Not Found" for valid cities
**Solution**: Try entering the city name in English with proper spelling (e.g., "New Delhi", "London", "Tokyo")

### Issue: No response from API
**Solution**: Check your internet connection and ensure Open-Meteo APIs are accessible

## Future Enhancements

Potential improvements:
- Add weather forecast for multiple days
- Show weather icons/images
- Add temperature unit toggle (Celsius/Fahrenheit)
- Display additional metrics (wind speed, pressure, UV index)
- Save favorite cities
- Dark mode theme
- Search history
- Weather alerts and warnings

## License

This project is open source and available for personal and educational use.

## Author

Created as a simple Python GUI application for learning Tkinter and API integration.

## Support

For issues or questions, please refer to:
- Open-Meteo API Documentation: https://open-meteo.com/
- Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
- Requests Library: https://docs.python-requests.org/

---

**Enjoy using the Python Weather App!** 🌤️
