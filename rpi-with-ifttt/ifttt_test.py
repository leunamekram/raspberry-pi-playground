
from time import sleep
import requests
dir(requests)
# import RPi.GPIO as io
# io.setwarnings(False)
# io.setmode(io.BOARD)

# io.setup(3,io.OUT)
led = 3

while True:
    data = requests.request(url="https://maker.ifttt.com/trigger/LED Trigger/with/key/b1mDdlhFukUlVjVrSDuTfX")
    print(data.text)

    if (data.text=="1"):
        # io.output(led,True)      
        print('led on')
        time.sleep(1)

    elif (data.text=="0"):
        # io.output(led,False)       
        time.sleep(1)
        print('led off')
