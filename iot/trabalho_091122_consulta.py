import RPi.GPIO as gpio
import os
import time as delay
from urllib.request import urlopen
import requests

gpio.setmode(gpio.BOARD)

led_vermelho, led_verde = 11, 12
botao = 18
contador = 0

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)
gpio.setup(botao, gpio.IN)

gpio.output(led_verde, False)
gpio.output(led_vermelho, False)


while True:#API da Vitoria
    consulta1 = requests.get('https://api.thingspeak.com/channels/1928249/fields/1/last?key=YK45KPNG2GOYJBTB')
    consulta2 = requests.get('https://api.thingspeak.com/channels/1928249/fields/2/last?key=YK45KPNG2GOYJBTB')
    consulta3 = requests.get('https://api.thingspeak.com/channels/1928249/fields/3/last?key=YK45KPNG2GOYJBTB')
    consulta4 = requests.get('https://api.thingspeak.com/channels/1928249/fields/4/last?key=YK45KPNG2GOYJBTB')
    print('Ocupação: ',consulta1.text)
    print('Disponível: ',consulta2.text)
    print('Umidade: ',consulta3.text)
    print('Temperatura: ',consulta4.text)
    delay.sleep(10)