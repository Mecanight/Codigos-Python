import RPi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import Adafruit_DHT as dht
import os
import requests

gpio.setmode(gpio.BOARD)
led_vermelho = 11
led_verde = 12
botao = 8
pin_dht = 4
pin_t = 15
pin_e = 16

i = 0
espaco_vazio = 20

field_temp = '&field1='
field_umid = '&field2='
field_dist = '&field3='
field_ocup = '&field4='

api = 'https://api.thingspeak.com/update?api_key='
key = 'TKI3CK1L5ACBXSEO'

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

# def testa_conexao():
#     try:
#         urlopen('http://www.colegiomaterdei.com.br/', timeout = 1)
#         return True
#     except:
#         return False

if testa_conexao() == True:
    while True:
        umid, temp = dht.read(dht_sensor, pin_dht)
        print(umid)
        print(temp)
        print(distancia())
        espaco_disp = (distancia()/espaco_vazio)*100    
        espaco_ocup = 100 - espaco_disp
        
        print('Espaço disponível: ', str(espaco_disp))
        print('Espaço Ocupado: ', str(espaco_ocup))
        dados = (api+key+field_temp+str(temp)+field_umid+str(umid)
                 +field_dist+str(distancia())+field_ocup+str(espaco_ocup))
        print('Link API: ', dados)
        requests.post(dados)
        print('Dados enviados')
        
        delay.sleep(30)
        
else:
    while i <= 3:
        gpio.output(led_vermelho, True)
        delay.sleep(1)
        gpio.output(led_vermelho, False)
        delay.sleep(1)
        i += 1