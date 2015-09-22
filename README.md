# Turnkey-Twitter-WeatherBot
Simple script to run a twitter weatherbot using wunderground's API written in Python 2.*

Requirements:
Python 2.*: json, urllib2, birdy, tweepy, python-pip<br>
You must get a wunderground API account. http://www.wunderground.com/weather/api/ - Fill in your API key in the forecast.py file<br>
You must have a Twitter account and app setup through: https://apps.twitter.com/ - Fill in your Consumer Key, Consumer Secret, Access Token, and Access Token Secret in the forecast.py file<br>
The following line in the forecast.py file sets which location to check the weather:
```f = urllib2.urlopen("http://api.wunderground.com/api/YOUR-WUNDERGROUND-API-KEY-HERE/geolookup/conditions/q/GB/London.json")```

The server / computer you run this on must have a cron job created to run this every hour / half hour / however often you want it to run and post to the account.
