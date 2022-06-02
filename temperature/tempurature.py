import RPi.GPIO as GPIO
from DHT11_Python import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

module = dht11.DHT11(pin=27)

while True:
    result = module.read()
    if result.is_valid():
        print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        print("気温: " + str(result.temperature) + "℃")
        print("湿度: " + str(result.humidity) + "%")
        break
    time.sleep(7)
