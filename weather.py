import requests

# --- Configuration ---
# Your actual OpenWeatherMap API key
API_KEY = "518b3dd455ca5be34f865b8757a70e65"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# ---------------------

def get_weather(city_name)
    """
    Fetches the current weather data for a given city name.
    """
    # Parameters to send with the API request
    params = {
        'q': city_name,     # The city name
        'appid': API_KEY,   # Your unique API key
        'units': 'metric'   # Get temperature in Celsius (use 'imperial' for Fahrenheit)
    }

    try:
        # 1. Make the API request
        response = requests.get(BASE_URL, params=params)
        
        # 2. Check for successful response (HTTP status code 200)
        # Raises an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status() 
        
        # 3. Parse the JSON data from the response
        weather_data = response.json()

        # Check if the city was found based on the API's response structure
        if weather_data.get('cod') == '404':
            print(f"Error: City '{city_name}' not found.")
            return None
        
        # 4. Extract relevant information
        main_temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        description = weather_data['weather'][0]['description'].capitalize()
        
        # 5. Return the extracted data
        return {
            'city': city_name.capitalize(),
            'temperature': main_temp,
            'feels_like': feels_like,
            'description': description
        }

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except KeyError:
        print("Error: Could not parse expected weather data. Check API documentation.")
        
    return None

def main():
    """Main function to handle user interaction and display results."""
    print("--- Simple Weather Reporter ---")
    city = input("Enter the city name: ").strip()
    
    if city:
        weather = get_weather(city)
        
        if weather:
            print("\n--- Current Weather ---")
            print(f"City: {weather['city']}")
            print(f"Temperature: {weather['temperature']} °C")
            print(f"Feels Like: {weather['feels_like']} °C")
            print(f"Conditions: {weather['description']}")
            print("-------------------------")
    else:
        print("City name cannot be empty.")

if __name__ == "__main__":
    main()
