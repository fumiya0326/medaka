import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

def main(): 
    instance = dht11.DHT11(pin=14)
    while True: 
        result = instance.read()
        if result.is_valid():
            print(result.temperature, result.humidity)
        time.sleep(1)

if __name__ == "__main__":
    try:
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()