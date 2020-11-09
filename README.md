# Victoria COVID-19 Twitter Bot 🤖

A Python bot that automates the extraction, formatting and posting of COVID-19 data from the Victorian Govt DHHS Website to Twitter.

You can see the bot in action here: https://twitter.com/VicCOVIDBot

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

Most of the code at the first half of the file you do not need to change. However, when you come to the variable 'url', you can change it to the URL of your choosing, provided it is formatted for data collection. The URL I am using in the bot is this one:

    https://discover.data.vic.gov.au/api/3/action/datastore_search?resource_id=e3c72a49-6752-4158-82e6-116bea8f55c8&limit=1998
    
The four API keys, indicated in the code as...

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']

...do not need to be altered with your actual keys in place of the 'environ[X]'. But, if you plan to run it from your local machine and are not setting environmental variables (which we are doing in AWS), replace the 'environ[X]' with the corresponding API key and it should run fine.

The different headings in the code, like "#Total Cases" or "#Total Active Cases" are just examples of me extracting data from the code. Each source file will be different. Make sure you understand the basics of Python and how to withdraw information from dictionaries. You can also completely change the "#Make Print Message" information.

The code at the very end of the file...

    api.update_status(status)
    
...is the code that actually sends information to Twitter and gets your Twitter profile to update it's status. You can put whatever you want in here. This Twitter bot can be a lot smaller, but I've used it to extract data and then format it so it naturally ends up a little longer.

Make sure you save this .py file as 'lambda_handler'. You can save it as something else, but only if you know what you're doing and you will change the handler name in the settings of the Lambda function in AWS.

## Deployment to AWS

To have your bot hosted somewhere that isn't your local computer, you'll need some kind of host. I've chosen AWS as my cloud computing platform of choice.

You'll need to create an Amazon Web Services account [here.](https://aws.amazon.com/)

Unfortunately, they'll require you to sign up with your bank card but they won't charge you unless you start using ridiculous amounts of cloud computing power. This Twitter bot will such a small amount of power that it'll cost you absolutely nothing.

### Creating A .ZIP File

Before you use the Lambda function in AWS, you'll need a zipped folder of all your dependencies plus your Python Twitter bot script. Normally, these will be kept in Python's folder located in Lib/site-packages. If you've set up your Python script in a virtual environment (highly recommended), then you'll find them in the virtual environments Lib/site-packages location.

You'll need to take all the folders of the dependencies and copy and put them in a separate folder along with your .py Python Twitter bot script. You should then go into this folder, select everything (Ctrl-A), right-click and hover over the 'Send to' menu item which will bring up a list of different places you can send these files. Send these files to a compressed (zipped) folder. Name this folder whatever you want, you'll need it for the next step.

### Using Lambda

With your Python script finished, under the AWS Management Console, search for 'Lambda'. Click on it, and when you come to the main Lambda page, click 'Create function'. Select 'Author from scratch', give your function a name and choose the appropriate runtime (in this case, Python 3.8). Click create function, and you'll be taken to the main function page.

Here, under the 'Function code' section, on the right side is a drop-down menu called 'Actions'. Here you'll click 'Upload a .zip file' to upload a zipped file of all your dependencies, plus your Python Twitter bot script. This is that .ZIP file you made earlier. The reason you need to do this is a lot of the modules that you need the Twitter script are not installed in AWS and you'll need to upload them yourself.

Once that's done, under the 'Environmental Variables' table, fill out the `ACCESS_KEY`, `ACCESS_SECRET`, `CONSUMER_KEY` and `CONSUMER_SECRET` variables. These are the 4 tokens you generated when you signed up for Twitter's developer account.

If everything is working fine, you can press the 'Test' button up at the top of the page and see if it runs successfully. If it does, congratulations!

### Using CloudWatch

The final step of your Twitter bot it setting up how often you want it to run. With AWS, we'll be using 'CloudWatch'. Head back to the AWS Management Console, search for 'CloudWatch', click on it and on the left side of the page there will be a menu. Under the 'Events' tab, there will be a smaller heading called 'Rules' - click on this.

Here, you should click 'Create rule' and under 'Event Source', click on the 'Schedule' option. You can choose either a 'Fixed rate' where you decide if it runs every certain amount of minutes, hours, days, etc. or you can use a cron expression (Google it!) to determine when you want it to run. 

Then under Targets, press 'Add Target', choose 'Lambda function' and click your Twitter bot. Click configure details and boom, you're all done. The bot is up and running, and it will run the script at the time you set it to.

## Thank you!

Thanks for stopping by. As always, programming is always a work-in-progress so please let me know if you have any improvements or suggestions you want to make. This is one of my first programming projects ever (!) so always looking for room to improve. 

Cheers! 🍻
