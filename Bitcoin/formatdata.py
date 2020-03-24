import get_price_from_url
from datetime import datetime
from pytz import timezone

country = input('Enter Country Code : ')
def formatdata():
  data = get_price_from_url.get_data(country)

  format = "Date: %Y-%m-%d || Time: %H:%M:%S"
  # Current time in UTC
  now_utc = datetime.now(timezone('UTC'))
  # Convert to Asia/Kolkata time zone
  now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
  time = (now_asia.strftime(format))
  return (f'Price : {data} <br>{time} <br> <br> ')