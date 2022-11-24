import RPi.GPIO as gpio
import os 
import time as delay
from urllib.request import urlopen
import requests

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

ledvermelho, ledverde = 11, 12
contador = 0

gpio.setup(ledverde, gpio.OUT)
gpio.setup(ledvermelho, gpio.OUT)

gpio.output(ledverde, False)
gpio.output(ledvermelho, False)


while True:
        consulta1 = requests.get('https://api.thingspeak.com/channels/codigo_id/fields/1/last?key=codigo_key')
        consulta2 = requests.get('https://api.thingspeak.com/channels/codigo_id/fields/2/last?key=codigo_key')
        consulta3 = requests.get('https://api.thingspeak.com/channels/codigo_id/fields/3/last?key=codigo_key')
        consulta4 = requests.get('https://api.thingspeak.com/channels/codigo_id/fields/4/last?key=codigo_key')
        print('Temperatura '+consulta1.text)
        print('Umidade '+consulta2.text)
        print('Distancia '+consulta3.text)
        print('Ocupação '+consulta4.text)
        delay.sleep(30)
