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
contador = 0

field_temp = '&field1='
field_umid = '&field2='
field_dist = '&field3='
field_ocup = '&field4='

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

c1 = ['1928247', 'G37I8C7N8N56H27S']
c2 = ['1928249', 'YK45KPNG2GOYJBTB']
c3 = ['1928250', 'MO1P1Q7MM9WXJTX4']

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
    if gpio.input(botao) == True:
        contador_botao = contador_botao + 1
        print(contador_botao, 'º Clique')
    if contador_botao == 1 and contador == 0:
        contador = 1
        gpio.output(led_vermelho, True)
        delay.sleep(2)
        gpio.output(led_vermelho, False)
        imprime(c2)
    if contador_botao == 2 and contador == 1:
        contador = 2
        if float((consulta_dados(c2)[0]).text) > 70:
            gpio.output(led_vermelho, True)
            print('Mais que 70%')
        else:
            print('Menos que 70%')
            gpio.output(led_verde, True)
        imprime(c2)
#     if contador_botao == 3: