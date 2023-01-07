import RPi.GPIO as gpio
import os
import time as delay
from urllib.request import urlopen
import requests

gpio.setmode(gpio.BOARD)

led_vermelho, led_verde = 11, 12
contador = 0

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)

gpio.output(led_verde, False)
gpio.output(led_vermelho, False)


if testa_conexao() == True:
    while True:
        consulta1 = requests.get('https://api.thingspeak.com/channels/1909874/fields/1/last?key=I9BG5U67STC886QK')
        consulta2 = requests.get('https://api.thingspeak.com/channels/1909874/fields/2/last?key=I9BG5U67STC886QK')
        consulta3 = requests.get('https://api.thingspeak.com/channels/1909874/fields/3/last?key=I9BG5U67STC886QK')
        consulta4 = requests.get('https://api.thingspeak.com/channels/1909874/fields/4/last?key=I9BG5U67STC886QK')
        print('Temperatura: ',consulta1.text)
        print('Umidade: ',consulta2.text)
        print('Distância: ',consulta3.text)
        print('Ocupação: ',consulta4.text)
        delay.sleep(30)
        
        
else:
    while contador < 3:
        gpio.output(led_vermelho, True)
        delay.sleep(1)
        gpio.output(led_vermelho, False)
        delay.sleep(1)
        contador += 1