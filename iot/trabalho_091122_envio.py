import RPi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import Adafruit_DHT as dht
import os
import requests

gpio.setmode(gpio.BOARD)
led_vermelho = 11
led_verde = 12
botao = 18
pin_dht = 4
pin_t = 15
pin_e = 16

i = 0
espaco_vazio = 20

field_ocup = '&field1='
field_disp = '&field2='
field_umid = '&field3='
field_temp = '&field4='

api = 'https://api.thingspeak.com/update?api_key='
key = '576Q6RAE9TFPD2GC'

dht_sensor = dht.DHT11

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)
gpio.setup(botao, gpio.IN)
gpio.setup(pin_t, gpio.OUT)
gpio.setup(pin_e, gpio.IN)

gpio.output(led_vermelho, False)
gpio.output(led_verde, False)

def distancia():
    gpio.output(pin_t, True)
    delay.sleep(0.000001)
    gpio.output(pin_t, False)
    tempo_i = delay.time()
    tempo_f = delay.time()
    
    while gpio.input(pin_e) == False:
        tempo_i = delay.time()
    while gpio.input(pin_e) == True:
        tempo_f = delay.time()
        
    tempo_d = tempo_f - tempo_i
    distancia = (tempo_d * 34300) / 2
    
    return distancia

while True:
    umid, temp = dht.read(dht_sensor, pin_dht)
    espaco_disp = (distancia()/espaco_vazio)*100    
    espaco_ocup = 100 - espaco_disp
    print('Distância', distancia())
    print('Espaço disponível: ', str(espaco_disp))
    print('Espaço Ocupado: ', str(espaco_ocup))
    print(umid)
    print(temp)
    dados = (api+key+field_ocup+str(espaco_ocup)+field_disp+str(espaco_disp)
             +field_umid+str(umid)+field_temp+str(temp))
    print('Link API: ', dados)
    requests.post(dados)
    print('Dados enviados')

    delay.sleep(60)