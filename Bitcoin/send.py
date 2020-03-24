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
    sleep(1)
    data = {'value1' : (string)}
    #data1 = {'value1' : 'You Will Recieve update soon'}
    ifttt_url = f'https://maker.ifttt.com/trigger/{event}/with/key/{IFTTT TOKEN} '
    
    try:
      if len(datahistory) == 5 :
        print(*datahistory)
        
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
