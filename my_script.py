#goal: print the latest closing price 

import json
import os 
import requests #will need to install requests package (in new environment, or activate previous environment that it was in)
#conda env list or pip install requests
from dotenv import load_dotenv #alternative method to get api key in
#pip install python-dotenv from environment 

API_KEY = os.environ.get("MY_API_KEY") #in other coding language, all caps means it is a constant value that cannot be changed
#define MY_API_KEY in the anaconda command line before running the python script using quotes

load_dotenv()
print(API_KEY)

exit() #will break from code and stop here in Python

#request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=demo"
#concatenation method: 
#request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=demo" + API_KEY
#interpolation method:
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey={API_KEY}"  


#make sure to remove API value before making a commit, otherwise people can see your password
#we can refer to it by some name, but we have to protect it 

response = requests.get(request_url)

print("RESPONSE STATUS: " + str(response.status_code))
print("RESPONSE TEXT: " + response.text)

parsed_response = json.loads(response.text)

print("THE LATEST CLOSING PRICE IS: $XYZ.OO ")


