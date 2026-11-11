import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 4

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print("Temperature:", temperature, "C")
            print("Humidity:", humidity, "%")
        else:
            print("Sensor reading error")

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped")
