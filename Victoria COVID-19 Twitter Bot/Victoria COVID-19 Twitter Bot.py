import json
import urllib.request
import emoji
import requests
import chardet
import boto3
import tweepy
from os import environ
from datetime import datetime

#Lambda Handler For AWS
def lambda_handler(event, context):  
    create_tweet()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

#Enter Your Twitter API Keys Here!
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def create_tweet():
    #Authenticate To Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    #Gathering The Data From The Victorian Govt's Website
    url = 'https://discover.data.vic.gov.au/api/3/action/datastore_search?resource_id=e3c72a49-6752-4158-82e6-116bea8f55c8&limit=1998'
    fileobj = urllib.request.urlopen(url) #opens URL
    data = json.loads(fileobj.read()) #Loads The Data In JSON Format
    today = datetime.today().strftime('%d/%m/%Y') #Sets The Date
    
    #Total Cases
    totalcases = 0
    for cases in data['result']['records']:
        totalcases = totalcases + int(cases['cases'])
       
    #Total New Cases   
    totalnewcases = 0
    for newcases in data['result']['records']:
        totalnewcases = totalnewcases + int(newcases['new'])
      
    #Total Active Cases  
    totalactivecases = 0
    for activecases in data['result']['records']:
        totalactivecases = totalactivecases + int(activecases['active'])
        
    #Total Postcodes Affected
    postcodesaffected = 0
    for postcode in data['result']['records']:
        if int(postcode['active']) > 0:
            postcodesaffected = postcodesaffected + 1
        
    #Replace With Donut Emoji
    if totalnewcases == 0:
        totalnewcases = emoji.emojize(":doughnut:") + " (That's Zero!)"
        
    #Make Print Message
    tweet = "Victoria COVID-19 Cases For " + str(today) + ":\n\nNew Cases: " + str(totalnewcases) + "\nActive Cases: " + str(totalactivecases) + "\nTotal Cases: " + str(totalcases) + "\nPostcodes Affected: " + str(postcodesaffected)
    moreinfo = "\nFind more information at: " + "https://bit.ly/34Of5xu"
    message = "Stay safe everyone!"
    athash = "\n@DanielAndrewsMP\n@VictorianCHO\n@VicGovDHHS\n#COVID19"
    
    #Create Status And Send To Twitter
    status = tweet + "\n" + moreinfo + "\n\n" + message + "\n" + athash
    api.update_status(status)
