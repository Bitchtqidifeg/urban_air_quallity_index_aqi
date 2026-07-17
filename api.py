import requests

# Replace with your NEW API key
API_KEY = "14d260e1e15bfca186eca339a6765a8d"


# -------------------------------
# Get Latitude and Longitude
# -------------------------------
def get_coordinates(city):

    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    data = response.json()

    if not data:
        return None

    return data[0]["lat"], data[0]["lon"]


# -------------------------------
# Get Weather Data
# -------------------------------
def get_weather(lat, lon):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "pressure": data["main"]["pressure"]
    }


# -------------------------------
# Get Air Pollution Data
# -------------------------------
def get_air_quality(lat, lon):

    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)

    data = response.json()

    pollution = data["list"][0]

    return {
        "aqi": pollution["main"]["aqi"],
        "pm2_5": pollution["components"]["pm2_5"],
        "pm10": pollution["components"]["pm10"],
        "co": pollution["components"]["co"],
        "no2": pollution["components"]["no2"],
        "so2": pollution["components"]["so2"],
        "o3": pollution["components"]["o3"]
    }
if __name__ == "__main__":

    city = "Bangalore"

    coordinates = get_coordinates(city)

    if coordinates:

        lat, lon = coordinates

        print("Coordinates:", lat, lon)

        print("Weather Data:")
        print(get_weather(lat, lon))

        print("Air Quality:")
        print(get_air_quality(lat, lon))

    else:
        print("City not found.")