# requests module is used to access data from api
import requests

# get_data function will return the data from url based on the country given


def get_data(country):
    try:
        # connection is being established to the url
        connection = requests.get(url='https://blockchain.info/ticker')
        # data is encoded into json format
        data_in__json = connection.json()
        # returning the data to the function,
        # which can be accessed in other module
        # last will get the latest bitcoin price and symbol will return the
        # symbol of the country provided.
        return (str(data_in__json[country.upper()]['last']) +
                ' ' + str(data_in__json[country.upper()]['symbol']))
    # if in case the url we gave is offline the code will terminate and we
    # need to change the url.
    except Exception:
        print('Data is not accessable from the url provided.')
