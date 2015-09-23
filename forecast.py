# -*- coding: utf-8 -*-
# Weather Twitter Bot - AJBBB - 7/8/2015 v2.*
 
import urllib2
import json
from birdy.twitter import UserClient
import tweepy
 
#Twitter Keys
CONSUMER_KEY = "raG9oBdjOKEkwAXXTHzuY0uqt"
CONSUMER_SECRET = " StO81j9QpgRZXgjw0jHCSZt6SARMT23zg4DzOdjE8A2sD1cE6G"
ACCESS_TOKEN = " 489164437-2VFwrUg2Wtn2hidc6kVeN9T7rKPWgfs4fRBUt7Lj"
ACCESS_TOKEN_SECRET = "JB5BSKqR4veacRv1CeTMQRAegSWGena7xxiNhqyc4s2G7"
 
#Get the wundergound json file to be read - THIS LINK MUST BE CHANGED IF YOU WANT TO CHANGE WEATHER LOCATION - Default is GB - London
f = urllib2.urlopen("http://api.wunderground.com/api/64d9bc1797c1cf51/geolookup/conditions/q/GB/Grimsby.json")
#read from the json file
json_string = f.read()
#parse the json file
parsed_json = json.loads(json_string)
#get info from current_observation in json file
temp_c = parsed_json['current_observation']['temp_c']
wind = parsed_json['current_observation']['wind_kph']
winddir = parsed_json['current_observation']['wind_dir']
windstr = parsed_json['current_observation']['wind_string']
weather = parsed_json['current_observation']['weather']
 
#Define the degree symbol
degree = u'\N{DEGREE SIGN}'
 
#Connect Using Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
#oAuth Client Info
client = UserClient(CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)
 
 
def tweet(message):
    #Simple tweet function to tweet whatever is passed to message.
    client.api.statuses.update.post(status=message)
 
if wind > 0.0:
    #Tweet out the current weather with numerical wind speed.
    tweet("Current weather in Grimsby, UK: " + str(temp_c) +
    degree + "C" + " and " + str(weather) + ". Wind: " + str(wind) +
    " KPH #weather #Grimsby #news #UK http://www.wunderground.com/personal-weather-station/dashboard?ID=IGRIMSBY5") # The link here goes to the LONDON wundeground page.
else:
    #Tweet out the current weather with text.
    tweet("Current weather in Grimsby, UK: " + str(temp_c) +
    degree + "C" + " and " + str(weather) +
    ". Little to no wind. #weather #london #news #UK http://is.gd/UyLFWz") # The link here goes to the LONDON wundeground page.
