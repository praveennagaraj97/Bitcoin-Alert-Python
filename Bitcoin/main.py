from time import sleep
from tqdm import tqdm
import sys

try:

    animation = "✒✔༼ つ ◕_◕ ༽つ|/-\\"
    for i in range(25):
        sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("""
  ----------------------------------------------
  ----------------------------------------------
  ---------   BITCOIN ALERT SERVER   -----------
  ----------------------------------------------
  ----------------------------------------------
  """)
    print('''
  Available Country :
  INR - INDIA
  USD - UNITED STATES OF AMERICA
  JPY - JAPAN
  EUR - EUROPE
  AND Still more !
  ''')
    # this module is imported to run the whole code and
    # hide the all other working procedure to avoid
    # modifications form others.
    # Starting the server !
    loop = tqdm(total=100, position=0, leave=False)
    for k in range(100):
        loop.set_description("Starting the Server ! ")
        sleep(.1)
        loop.update(1)
    loop.close()
    import send
    send.sendtoIFTTT()
except(Exception):
    print('Country Code is Invalid')
