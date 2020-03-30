# data from formatdata module
import formatdata
# time module is used to extract sleep method to set the time between data
# collection.
from time import sleep
# requests is used to post and create sessions
import requests
# this function takes event name as parameter and sent the data to IFTTT
# applet.


def sendtoIFTTT(event='Bitcoin_price'):
    # empty list is created to store the data from format data module
    datahistory = []
    # i is the variable to show in console that - how many times the data is
    # collected
    i = 1
    # infinite loop is created as new bitcoin price uodates keep coming
    while True:
        # data variable is used to stored data recieved from formatdata module.
        data = formatdata.formatdata()
        # everytime a data is collected it is added to the list.
        datahistory.append(data)

        print(f'Data collected {i} times !')
        # incrementing the i variable after every loop
        i += 1
        # time is set here (seconds)!
        sleep(5)
        # this is the IFTTT Token recieved from IFTTT services
        ifttt_url = f'''https://maker.ifttt.com/trigger/{event}/with/
        key/jeoII-tpwkkU0O5W4-xDTGYzk-V0mx7PCOMhblx-pGR'''
        if len(datahistory) == 5:
            try:

                # the data in list is add to string module .
                string = "".join([x + '\n' for x in datahistory])

                # value1 is the datafield we provided in IFTTT applet so we are
                # assigning our string to it
                data = {'value1': (string)}
                # session is opened to start posting
                s = requests.session()
                # url and and data is send as json
                requests.post(ifttt_url, json=data)
                print(f'\nsent ! ')
                # session is closed immediatelt after data is posted.
                s.close
                # collected data is deleted
                del data  # this is not needed but added in case of any failues
                # list is cleared to get new data in the new session
                datahistory = []

                print('Starting New Session !')
                # again new sesssion is started
                sendtoIFTTT()

            except Exception:
                print('something went wrong !!')
                sendtoIFTTT()
