import send
try:
  send.sendtoIFTTT()
except(Exception):
  print('Country Code is Invalid')
