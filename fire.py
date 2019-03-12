"""from firebase import firebase
firebase=firebase.FirebaseApplication('https://locations-ccc0b.firebaseio.com/')
result=firebase.post('/user',{'hi':'hi'})
print(result)"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tweepy
import csv
import json
from geopy.geocoders import Nominatim


consumer_key = 'NRptEoE4t7OwAgCyyAivwPfBw'
consumer_secret = 'NhlOT7TRiNmTGWenwYmfB78yYiBEg1GmQrXfYDOfQTz6V061Jd'
access_token = '2565365424-lKWzAy2Y8JOFybxj9zbiNYvZqkx5Lmk7UVZShct'
access_secret = 'mqI4sXlkaf5eK0V9euy6X0k7d6WjvkBW52y8tTwL2mPG8'




# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://locations-ccc0b.firebaseio.com'
})

root = db.reference('/users1/')

i=0
maximum_number_of_tweets_to_be_extracted = \
    int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')
geolocator = Nominatim()
"""users_ref = ref.child('user')"""
for tweet in tweepy.Cursor(api.search, q='#' + hashtag, lang='en',
                           rpp=100).items(maximum_number_of_tweets_to_be_extracted):
    location = geolocator.geocode(tweet.user.location)
    if location is not None:
    	ref= root.child(str(i))
    	ref.set({
    		i:{
    			'latitude':(location.latitude),
    			'longitude':(location.longitude)
    		}
    	})
    	i=i+1