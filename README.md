# Bitcoin-Alert-Based-on-Python
Bitcoin telegram notification using IFTTT services
Bitcoin Price Notifications

Telegram link: http://t.me/praveenNagaraj

Introduction

Bitcoin emerged out of the 2008 global economic crisis when big banks were caught misusing borrowers' money, manipulating the system, and charging exorbitant fees. To address such issues, Bitcoin creators wanted to put the owners of bitcoins in-charge of the transactions, eliminate the middleman, cut high interest rates and transaction fees, and make transactions transparent. They created a distributed network system, where people could control their funds in a transparent way.
Bitcoin has grown rapidly and spread far in a relatively short period of time. Across the world, companies from a large jewellery chain in the US, to a private hospital in Poland, accept bitcoin currency. Multi-billion-dollar corporations such as Dell, PayPal, Microsoft, Expedia, etc., are dealing in bitcoins. Websites promote bitcoins, magazines are publishing bitcoin news, and forums are discussing cryptocurrencies and trading in bitcoins. Bitcoin has its own Application Programming Interface (API), price index, trading exchanges and exchange rate.
However, there are issues with bitcoins such as hackers breaking into accounts, high volatility of bitcoins, and long transaction delays. Elsewhere, particularly people in third world countries find Bitcoins as a reliable channel for transacting money bypassing pesky intermediaries.


What is IFTTT?
If This Then That, also known as IFTTT is a freeware web-based service that creates chains of simple conditional statements, called applets.
An applet is triggered by changes that occur within other web services such as Gmail, Facebook, Telegram, Instagram, or Pinterest. 
What is Telegram?

Telegram is a cloud-based instant messaging and voice over IP service. Telegram client apps are available for Android, iOS, Windows Phone, Windows NT, macOS and Linux. Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Telegram's client-side code is open-source software but the source code for recent versions is not always immediately published, whereas its server-side code is closed-source and proprietary. The service also provides APIs to independent developers. In March 2018, Telegram stated that it had 200 million monthly active users. 
Default messages and media in Telegram are encrypted when stored on its servers, but can be accessed by the Telegram service provider, who holds the encryption keys. In addition Telegram provides optional end-to-end encrypted "secret" chats between two online users, yet not for groups or channels. 
The client-server communication is also encrypted. The service provides end-to-end encryption for voice calls. 


Project Overview:
•	This Project will send notification of bitcoin latest price for every one hour.
•	The notifications will be sent to telegram channel “AttainU Bitcoin IFTTT”.
•	The channel is global and anyone can access the channel and get regular updates of bitcoin prices. 


Features: 
•	Anyone with the link can join and chat along the channel.
•	This Project is alive forever.



Working Procedure:
•	The project runs in ‘Python anywhere console’, which will keep the code run alive.
•	The Project is Divided into Four Modules:
	Get data Module
	Format Date Module
	Send Data to IFTTT
	Main Module 
	Get data Module – Here I have used request module to collect data from source(‘blockchain.com’), Once it gets data it will convert the data into json format which is returned back to the function.
	Format Data Module – The main objective of this module is to format the notification message which will be sent to users.
	Send Data to IFTTT – Here the formatted data is sent to users as notifications once it acquires data from previous module.
	Main – Here it will ask for the server maintainer to enter the country code.

•	IFTTT Applets:
	Webhooks and Telegram services are used here. 
	When an event is occurred in the webhooks it will send the event value to telegram.
 






•	Result:
 
	Asking the server maintainer to enter country code
 
	Hosted Server Page.
 
	Telegram Channel Message which is obtained by IFTTT.
 

	Notifications in telegram
Source code:

Get Data Module:
 
         import requests
         def get_data(country):
             response = requests.get(url='https://blockchain.info/ticker')
             response_json = response.json()
             return (str(response_json[country.upper()]['last']) + ' ₹')


Format Data Module:

         import get_price_from_url
         from datetime import datetime
         from pytz import timezone

         country = input(‘Enter Country Code : ‘)
         def formatdata():
             data = get_price_from_url.get_data(country)

             format = "Date: %Y-%m-%d || Time: %H:%M:%S"
             # Current time in UTC
             now_utc = datetime.now(timezone('UTC'))
             # Convert to Asia/Kolkata time zone
             now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
             time = (now_asia.strftime(format))
             return (f'Price : {data} <br>{time} <br> <br> ')






Send to IFTTT Module:

        import formatdata
        from time import sleep
        import requests
        def sendtoIFTTT(event='Bitcoin_price'):
        datahistory = []
        i = 1
        sent = 1
        while True:
           data = formatdata.formatdata()
           datahistory.append(data)
           print(i)
           i += 1

           string = "".join([x+'\n' for x in datahistory])
           sleep(2)
           data = {'value1' : (string)}
           #data1 = {'value1' : 'You Will Recieve update soon'}
           ifttt_url = f'https://maker.ifttt.com/trigger/{event}/with/key/{IFTTT TOKEN} '
    
           try:
              if len(datahistory) == 5 :
              s = requests.session()
              requests.post(ifttt_url,json=data)
              del data
              s.close
              print('Starting New Session !')
              sent += 1
              sendtoIFTTT()
              datahistory = []
           except Exception:
              print('something went wrong !!')
              sendtoIFTTT()






Main Module:

      import send
      try:
         send.sendtoIFTTT()
      except(Exception):
         print(‘Country Code is Invalid’)

# AttainU
# Source Code by Praveen Nagaraj


Conclusion:
	This Project helps in understanding about IFTTT and it’s services along with Bitcoin price and it’s news.
Since this project is developed using Python it will help in understanding about modules and using python in real world example.




