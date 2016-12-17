# Turnkey-Twitter-WeatherBot

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6b9b75d059e54849a3aaec631b935791)](https://www.codacy.com/app/ajbbb/Turnkey-Twitter-WeatherBot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AYJAYY/Turnkey-Twitter-WeatherBot&amp;utm_campaign=badger)

Simple script to run a twitter weatherbot using wunderground's API written in Python 2.*

Requirements:
Python 2.*: json, urllib2, birdy, tweepy, python-pip<br>
You must get a wunderground API account. http://www.wunderground.com/weather/api/ - Fill in your API key in the forecast.py file<br>
You must have a Twitter account and app setup through: https://apps.twitter.com/ - Fill in your Consumer Key, Consumer Secret, Access Token, and Access Token Secret in the forecast.py file<br>

The following line in the forecast.py file sets which location to check the weather:<br>
```f = urllib2.urlopen("http://api.wunderground.com/api/YOUR-WUNDERGROUND-API-KEY-HERE/geolookup/conditions/q/GB/London.json")```

The server / computer you run this on must have a cron job created to run this every hour / half hour / however often you want it to run and post to the account.
