# Dependencies
import tweepy
import time
import json
import random
import requests as req



# Twitter API Keys
consumer_key = "FzZ3zDr36XP0GAPLBLVS3m6QW"
consumer_secret = "3mcWJI9APvwGpltQeibFB1hU88I4j0Pu9kC5p4dzubkUCbj7fG"
access_token = "808542776673583104-m6fHan4xPmQOaPDwP5e59p3ioEoFmXW"
access_token_secret = "CdcMy49dc15SRSBqLrJeT6hsQFu56VOis5xKFSGyyMbmu"

# Weather API
api_key = "ed791b853161a5241e77846e1a84d4db


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "london"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "London Weather as of %s: %s F" %
        (datetime.datetime.now().strftime("%I:%M %p"),
         weather_json["main"]["temp"]))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(3600)