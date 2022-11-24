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
espaco_v = 20
contador_botao = 0

field_temp = '&field1='
field_umid = '&field2='
field_dist = '&field3='
field_ocup = '&field4='

api = 'https://api.thingspeak.com/update?api_key='
key = 'codigo_key'

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
    distancia = (tempo_d*34300)/2
    
    return distancia

c1 = ['codigo_id', 'codigo_key']
c2 = ['codigo_id', 'codigo_key']
c3 = ['codigo_id', 'codigo_key']

def consulta_dados(x):
    return[
    requests.get('https://api.thingspeak.com/channels/'+x[0]+'/fields/1/last?key='+x[1]),
    requests.get('https://api.thingspeak.com/channels/'+x[0]+'/fields/2/last?key='+x[1]),
    requests.get('https://api.thingspeak.com/channels/'+x[0]+'/fields/3/last?key='+x[1]),
    requests.get('https://api.thingspeak.com/channels/'+x[0]+'/fields/4/last?key='+x[1])
    ]
def imprime(x):
    consulta = consulta_dados(x)
    def imprime_consulta():
        print('Ocupação Lixeita '+consulta[0].text)
        print('Espaço Disponível '+consulta[1].text)
        print('Umidade '+consulta[2].text)
        print('Temperatura '+consulta[3].text)

    def imprime_erro():
        print('Erro')
        if consulta[0] <= 0:
            print('Ocupação Lixeita com valor = '+consulta[0].text)
        if consulta[1] <= 0:
            print('Espaço Disponível com valor = '+consulta[1].text)
        if consulta[2] <= 0:
            print('Umidade com valor = '+consulta[2].text)
        if consulta[3] <= 0:
            print('Temperatura com valor = '+consulta[3].text)

    if consulta[0] and consulta[1] and consulta[2] and consulta[3]:
        imprime_consulta()
    else:
        imprime_erro()

while True:
    if botao == True:
        contador_botao += 1
    if contador_botao == 1:
        gpio.output(led_vermelho, True)
        delay.sleep(2)
        gpio.output(led_vermelho, False)
        consulta_dados(c1)
                                    # continuar daqui
    if contador_botao == 2:
        if consulta_dados(c1)[0]> 70:
            gpio.output(led_vermelho, True)
        else:
            gpio.output(led_verde, True)
    # if contador_botao == 3: