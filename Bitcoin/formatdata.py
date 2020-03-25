# data is taken from get_price_from_url
import get_price_from_url
# date module is used to access date and time to format the message
from datetime import datetime
# since IFTTT has difeerent time zone pytz module is used to get the required timezone.
from pytz import timezone
# country is asked once at the time of starting server
country = input('Enter Country Code : ')

# this function will format the data(from get_price_from_url module) and return the formated data into function.
def formatdata():
  try:
    # data is taken from get_price_from_url module and stored in data variable.
    data = get_price_from_url.get_data(country)
    # this is the format of date and time which will be recieved in telegram
    format = "Date: %Y-%m-%d || Time: %H:%M:%S"
    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    # Convert to Asia/Kolkata time zone
    now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
    # storing the converted timezone to time variable
    time = (now_asia.strftime(format))
    # returning teh formatted data back.
    return (f'Price : {data} <br>{time} <br> <br> ')
  except Exception :
    # if in case any problem this can be notificed easily!
    print("Problem occured in formatting !")