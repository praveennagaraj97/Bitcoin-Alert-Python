import requests
def get_data(country):
  response = requests.get(url='https://blockchain.info/ticker')
  response_json = response.json()
  return (str(response_json[country.upper()]['last']) + ' ₹')
