# Victoria COVID-19 Twitter Bot 🤖

A Python bot that automates the extraction, formatting and posting of COVID-19 data from the Victorian Govt DHHS Website to Twitter.

## Disclaimer

I hold no liablity with what you do with this bot or how you plan to use it. Using bots can get you banned from Twitter, so make sure you read up on their [automation rules](https://help.twitter.com/en/rules-and-policies/twitter-automation) first.

## Installation

You can install the Twitter bot by using `pip`:

    pip install Victoria-COVID-19-Twitter-Bot

## Dependencies

You will need to install the Tweepy library:

    pip install tweepy
    
You also will need to install urllib.request, datetime, boto3, chardet, json, emoji, requests, and os. These are all required to make the bot run on Amazon Web Services (AWS).

It's also required that you sign up to Twitter and then apply [here](https://developer.twitter.com) to get a developer account.

Once you've made this account, you need to change the settings of your developer account to allow read & write.

You should then generate a new OAuth token with those permissions - this will generate 4 tokens that you can plug into the Twitter bot code if you wish to run it from your local machine.

However, we will be deploying the bot to AWS so we don't have to manually run the bot every time we want it to print a status. As such, we'll be inputting those 4 tokens into the environment variables section of the Lambda function in AWS.

If any of that sounded confusing, don't worry - I'll explain later.

## Usage
