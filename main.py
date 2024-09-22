from fetch import get_weather_data
from display import display_weather
import requests

def main():
    city = input("Enter the name of the city to get the weather for: ")
    try:
        weather_data = get_weather_data(city)
        display_weather(weather_data)
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred: ", err)
    except requests.exceptions.RequestException as err:
        print("Request error occurred: ", err)

if __name__ == "__main__":
    main()
 
