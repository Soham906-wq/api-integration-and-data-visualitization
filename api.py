import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Define the API key and base URL
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Function to fetch weather data
def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use "metric" for Celsius, "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}, {response.text}")

# Function to process data for visualization
def process_weather_data(data):
    timestamps = []
    temperatures = []
    humidities = []
    weather_descriptions = []

    for entry in data['list']:
        timestamps.append(entry['dt_txt'])
        temperatures.append(entry['main']['temp'])
        humidities.append(entry['main']['humidity'])
        weather_descriptions.append(entry['weather'][0]['description'])

    return timestamps, temperatures, humidities, weather_descriptions

# Function to create visualizations
def create_visualizations(timestamps, temperatures, humidities):
    sns.set(style="whitegrid")
    
    # Plot temperature trends
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="orange", marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.title("Temperature Trend")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot humidity trends
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, humidities, label="Humidity (%)", color="blue", marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.title("Humidity Trend")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main script
if __name__ == "__main__":
    city = input("Enter the city name: ")
    try:
        # Fetch data
        weather_data = fetch_weather_data(city)

        # Process data
        timestamps, temperatures, humidities, weather_descriptions = process_weather_data(weather_data)

        # Visualize data
        create_visualizations(timestamps, temperatures, humidities)
    except Exception as e:
        print(f"An error occurred: {e}")
