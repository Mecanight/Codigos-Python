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
contador_botao = 0
contador = 0

gpio.setup(led_vermelho, gpio.OUT)
gpio.setup(led_verde, gpio.OUT)
gpio.setup(botao, gpio.IN)

gpio.output(led_vermelho, False)
gpio.output(led_verde, False)

def consulta1():
    return [
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/1/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/2/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/3/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/4/last?key=codigo_key')).text)
    ]

def consulta2():
    return [
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/1/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/2/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/3/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/4/last?key=codigo_key')).text)
    ]

def consulta3():
    return [
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/1/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/2/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/3/last?key=codigo_key')).text),
    float((requests.get('https://api.thingspeak.com/channels/codigo_id/fields/4/last?key=codigo_key')).text)
    ]

def imprime_consulta(x):
    print('Ocupação Lixeita {:.2f}%'.format(x[0]))
    print('Espaço Disponível {:.2f}%'.format(x[1]))
    print('Umidade {:.1f}%'.format(x[2]))
    print('Temperatura {:.1f}º'.format(x[3]))

def imprime_erros(x):
        if x[0] is None or x[0] < 0:
            print('Erro! Ocupação Lixeita com valor {:.2f}'.format(x[0]))
        if x[1] is None or x[1] < 0:
            print('Erro! Espaço Disponível com valor {:.2f}'.format(x[1]))
        if x[2] is None or x[2] < 0:
            print('Erro! Umidade com valor {:.1f}'.format(x[2]))
        if x[3] is None or x[3] < 0:
            print('Erro! Temperatura com valor {:.1f}'.format(x[3]))

def verifica_erro(x):
    if (x[0] is None or x[0] < 0) or (x[1] is None or x[1] < 0) or (x[2] is None or x[2] < 0) or (x[3] is None or x[3] < 0):
        return True
    else:
        return False

while True:
    if gpio.input(botao) == True:
        contador_botao += 1
        print(contador_botao, 'º Clique')
    if contador_botao == 1 and contador == 0:
        delay.sleep(1)
        contador = 1
        gpio.output(led_vermelho, True)
        delay.sleep(2)
        gpio.output(led_vermelho, False)
        consultac2 = consulta2()
        print('Consulta finalizada')
        if verifica_erro(consultac2):
            for i in range(0,5):
                gpio.output(led_vermelho, True)
                delay.sleep(0.5)
                gpio.output(led_vermelho, False)
                delay.sleep(0.5)
            imprime_erros(consultac2)
        else:
            for i in range(0,3):
                gpio.output(led_verde, True)
                delay.sleep(0.5)
                gpio.output(led_verde, False)
                delay.sleep(0.5)
            imprime_consulta(consultac2)
    if contador_botao == 2 and contador == 1:
        delay.sleep(1)
        contador = 2
        if consultac2[0] > 70:
            gpio.output(led_vermelho, True)
            print('Mais que 70%')
        else:
            gpio.output(led_verde, True)
            print('Menos que 70%')
        print('Ocupação: {:.1f}'.format(consultac2[0]))
    if contador_botao == 3 and contador == 2:
        delay.sleep(1)
        gpio.output(led_vermelho, False)
        gpio.output(led_verde, False)
        contador = 3
        consultac1 = consulta1()
        print('Consulta finalizada')
        dif_umi = consultac1[2] - consultac2[2]
        if dif_umi < 0:
            dif_umi = dif_umi * (-1)
        dif_temp = consultac1[3] - consultac2[3]
        if dif_temp < 0:
            dif_temp = dif_temp * (-1)
        print('Sensores Colega')
        print('Umidade {:.1f}%'.format(consultac2[2]))
        print('Temperatura {:.1f}º'.format(consultac2[3]))
        print('Meus sensores')
        print('Umidade {:.1f}%, >>> diferença de {:.1f} pontos percentuais entre os sensores'.format(consultac1[2], dif_umi))
        print('Temperatura {:.1f}º, >>> diferença de {:.1f}º C entre os sensores'.format(consultac1[3], dif_temp))
    if contador_botao == 4 and contador == 3:
        delay.sleep(1)
        contador = 4
        consultac3 = consulta3()
        print('Consulta finalizada')
        print('Ocupação minha lixeira: {:.1f}'.format(consultac1[0]))
        print('Ocupação lixeira colega equipe: {:.1f}'.format(consultac2[0]))
        print('Ocupação lixeira colega externo: {:.1f}'.format(consultac3[0]))
        if consultac1[1] > consultac2[1] and consultac1[1] > consultac3[1]:
            gpio.output(led_verde, True)
            delay.sleep(0.5)
        if consultac2[1] > consultac1[1] and consultac2[1] > consultac3[1]:
            for i in range(0,5):
                gpio.output(led_verde, True)
                delay.sleep(0.5)
                gpio.output(led_verde, False)
                delay.sleep(0.5)
        if consultac3[1] > consultac2[1] and consultac3[1] > consultac1[1]:
            gpio.output(led_vermelho, True)
    if contador_botao == 5 and contador == 4:
        delay.sleep(1)
        contador_botao = 0
        contador = 0
        consultac1 = []
        consultac2 = []
        consultac3 = []
        gpio.output(led_vermelho, False)
        gpio.output(led_verde, False)
        print('Valores zerados')
        print('Consulta colega 1 :',consultac1)
        print('Consulta colega 2 :',consultac2)
        print('Consulta colega 3 :',consultac3)
